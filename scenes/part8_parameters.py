"""
Part 8: API Parameters
Slides 56-60: Temperature, top-p, top-k, system prompts
"""

from manim import *
from manim_slides import Slide
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.custom_scenes import *
from utils.animations import *
from utils.data_generators import *
from assets.styles.theme_config import *


class Slide56_TemperatureParameter(LLMSlide):
    """Slide 56: Temperature Parameter"""

    def construct(self):
        title = self.add_title("Temperature Parameter")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Controls the level of randomness in word selection",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2.5)
        self.play(Write(definition), run_time=0.7)

        # Low temperature
        low_temp = Text("Low Temperature (< 1)", font_size=HEADING_FONT_SIZE, color=PRIMARY_BLUE, weight=BOLD)
        low_temp.shift(LEFT * 3.5 + UP * 1)

        low_desc = Text(
            "Deterministic\nLess variation\nMore predictable",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        low_desc.next_to(low_temp, DOWN, buff=0.3)

        # High temperature
        high_temp = Text("High Temperature (> 1)", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        high_temp.shift(RIGHT * 3.5 + UP * 1)

        high_desc = Text(
            "Creative\nMore variation\nLess predictable",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        high_desc.next_to(high_temp, DOWN, buff=0.3)

        # Visualization curves
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1, 0.2],
            x_length=3,
            y_length=1.5,
            tips=False
        )

        # Low temp curve (sharp peak)
        low_curve = axes.plot(lambda x: np.exp(-((x-2)**2)*5), color=PRIMARY_BLUE)
        low_axes = VGroup(axes.copy(), low_curve).shift(LEFT * 3.5 + DOWN * 1.5).scale(0.8)

        # High temp curve (flat distribution)
        high_curve = axes.plot(lambda x: 0.5 + 0.1*np.sin(x), color=ACCENT_ORANGE)
        high_axes = VGroup(axes.copy(), high_curve).shift(RIGHT * 3.5 + DOWN * 1.5).scale(0.8)

        self.wait(0.3)
        self.play(FadeIn(VGroup(low_temp, low_desc, low_axes), shift=RIGHT), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(VGroup(high_temp, high_desc, high_axes), shift=LEFT), run_time=0.7)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide57_TopPSampling(LLMSlide):
    """Slide 57: Top-p (Nucleus Sampling)"""

    def construct(self):
        title = self.add_title("Top-p (Nucleus Sampling)")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Selects tokens whose cumulative probability exceeds threshold p",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2.5)
        self.play(Write(definition), run_time=0.7)

        # Example: "The cat ___"
        example = Text('"The cat ___"', font_size=HEADING_FONT_SIZE, color=WHITE, weight=BOLD)
        example.shift(UP * 1.5)
        self.play(Write(example), run_time=0.5)

        # Probability distribution
        words_probs = [
            ("meows", 0.30),
            ("sleeps", 0.25),
            ("eats", 0.24),
            ("plays", 0.16),
            ("is", 0.05)
        ]

        # Calculate cumulative
        cumsum = 0
        prob_rows = VGroup()

        for word, prob in words_probs:
            cumsum += prob
            color = ACCENT_GREEN if cumsum <= 0.8 else LIGHT_GRAY

            word_text = Text(word, font_size=BODY_FONT_SIZE, color=color, weight=BOLD)
            prob_text = Text(f"{prob:.2f}", font_size=SMALL_FONT_SIZE, color=color)
            cumsum_text = Text(f"({cumsum:.2f})", font_size=TINY_FONT_SIZE, color=color)

            bar = Rectangle(
                width=prob * 8,
                height=0.25,
                fill_opacity=0.8,
                fill_color=color,
                stroke_width=0
            )

            row = VGroup(word_text, bar, prob_text, cumsum_text).arrange(RIGHT, buff=0.2)
            prob_rows.add(row)

        prob_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.15).shift(DOWN * 0.2)

        # Threshold line
        threshold_line = DashedLine(LEFT * 5, RIGHT * 5, color=ACCENT_ORANGE, stroke_width=3)
        threshold_line.shift(DOWN + UP * 0.5)

        threshold_label = Text("top_p = 0.8", font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        threshold_label.next_to(threshold_line, RIGHT, buff=0.2)

        self.wait(0.3)
        for row in prob_rows:
            self.play(FadeIn(row), run_time=0.3)
            self.wait(0.05)

        self.wait(0.3)
        self.play(Create(threshold_line), Write(threshold_label), run_time=0.6)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide58_TopKSampling(LLMSlide):
    """Slide 58: Top-k Sampling"""

    def construct(self):
        title = self.add_title("Top-k Sampling")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Limits selection to the k most probable tokens",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2.5)
        self.play(Write(definition), run_time=0.7)

        # Analogy
        analogy = Text(
            'Like choosing only the top candies from a jar 🍬',
            font_size=BODY_FONT_SIZE,
            color=ACCENT_YELLOW
        )
        analogy.shift(UP * 1.7)
        self.play(FadeIn(analogy), run_time=0.5)

        # Example with k=2
        example = Text('If top_k = 2: "The cat ___"', font_size=HEADING_FONT_SIZE, color=WHITE)
        example.shift(UP * 0.8)
        self.play(Write(example), run_time=0.5)

        # Words
        words = [
            ("meows", 0.30, True),
            ("sleeps", 0.25, True),
            ("eats", 0.24, False),
            ("plays", 0.16, False),
            ("is", 0.05, False)
        ]

        word_rows = VGroup()
        for word, prob, included in words:
            color = ACCENT_GREEN if included else DARK_GRAY
            opacity = 1.0 if included else 0.3

            word_text = Text(word, font_size=BODY_FONT_SIZE, color=color, weight=BOLD)
            prob_text = Text(f"{prob:.2f}", font_size=SMALL_FONT_SIZE, color=color)
            status = Text("✓" if included else "✗", font_size=HEADING_FONT_SIZE, color=color)

            row = VGroup(word_text, prob_text, status).arrange(RIGHT, buff=0.5)
            row.set_opacity(opacity)
            word_rows.add(row)

        word_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN * 0.3)

        for row in word_rows:
            self.play(FadeIn(row), run_time=0.3)
            self.wait(0.05)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide59_SystemPrompt(LLMSlide):
    """Slide 59: System Prompt"""

    def construct(self):
        title = self.add_title("System Prompt (Metaprompt)")
        self.play(Write(title), run_time=0.5)

        # Properties
        properties = Text(
            "• Valid for entire conversation\n• Not visible to end user\n• Set by LLM, not modifiable",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN,
            line_spacing=1.3
        )
        properties.shift(UP * 1.8)
        self.play(FadeIn(properties), run_time=0.7)

        # Example
        example_label = Text("Example:", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        example_label.shift(UP * 0.3)

        example_box = Rectangle(
            width=10,
            height=1.5,
            fill_opacity=0.9,
            fill_color=DARK_GRAY,
            stroke_color=ACCENT_GREEN,
            stroke_width=2
        )
        example_box.shift(DOWN * 0.5)

        example_text = Text(
            '"You are a friendly and helpful assistant.\nAnswer questions concisely and clearly."',
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.3,
            font="Monospace"
        )
        example_text.move_to(example_box.get_center())

        self.wait(0.3)
        self.play(Write(example_label), run_time=0.5)
        self.wait(0.2)
        self.play(Create(example_box), Write(example_text), run_time=0.7)

        # Additional parameters
        params = Text(
            "Other parameters: max_tokens, model, role",
            font_size=BODY_FONT_SIZE,
            color=LIGHT_GRAY
        )
        params.to_edge(DOWN, buff=1)

        self.wait(0.3)
        self.play(FadeIn(params), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide60_HuggingFaceIntro(CodeSlide):
    """Slide 60: Hugging Face Introduction"""

    def construct(self):
        title = self.add_title("Hugging Face Platform")
        self.play(Write(title), run_time=0.5)

        # Features
        features = [
            "🤗 Open-source library (BERT, GPT, T5, LLaMA...)",
            "📚 10,000+ datasets for NLP, vision, audio",
            "☁️ Cloud API for using models without local GPU"
        ]

        feature_objects = self.create_bullet_list(features, font_size=BODY_FONT_SIZE)
        feature_objects.shift(UP * 1.5)

        for feature in feature_objects:
            self.play(FadeIn(feature, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        # Code example
        code = '''from transformers import pipeline

model_name = "facebook/opt-1.3b"
generator = pipeline("text-generation", 
                     model=model_name)

output = generator("AI is transforming",
                   max_length=50)
print(output[0]['generated_text'])'''

        code_block = self.create_code_block(code, language="python", title="Example Usage")
        code_block.scale(0.7).shift(DOWN * 0.8)

        self.wait(0.3)
        self.play(FadeIn(code_block), run_time=0.8)

        self.wait(PAUSE_TIME)
        self.next_slide()
