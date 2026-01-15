"""
Part 8: API Parameters
Slides 56-60: Temperature, top-p, top-k, system prompts, Hugging Face
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
        definition.shift(UP * 2.2)
        self.play(Write(definition), run_time=0.7)

        # Low temperature visualization
        low_temp_label = Text("Low Temperature\n(T < 1)", font_size=BODY_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD, line_spacing=1.2)
        low_temp_label.shift(LEFT * 4 + UP * 0.8)

        low_temp_desc = Text(
            "Deterministic\nLess variation",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        low_temp_desc.next_to(low_temp_label, DOWN, buff=0.3)

        # High temperature visualization
        high_temp_label = Text("High Temperature\n(T > 1)", font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD, line_spacing=1.2)
        high_temp_label.shift(RIGHT * 4 + UP * 0.8)

        high_temp_desc = Text(
            "Creative\nMore variation",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        high_temp_desc.next_to(high_temp_label, DOWN, buff=0.3)

        # Visual representation (probability bars)
        # Low temp - peaked distribution
        low_bars = VGroup(*[
            Rectangle(
                width=0.3,
                height=[0.5, 3.0, 0.8, 0.3, 0.2][i],
                fill_opacity=0.8,
                fill_color=ACCENT_GREEN,
                stroke_width=1,
                stroke_color=WHITE
            ).shift(DOWN * 1.5 + LEFT * 4 + RIGHT * i * 0.4)
            for i in range(5)
        ])

        # High temp - flat distribution
        high_bars = VGroup(*[
            Rectangle(
                width=0.3,
                height=[1.5, 1.8, 1.6, 1.4, 1.3][i],
                fill_opacity=0.8,
                fill_color=ACCENT_ORANGE,
                stroke_width=1,
                stroke_color=WHITE
            ).shift(DOWN * 1.5 + RIGHT * 4 + RIGHT * i * 0.4)
            for i in range(5)
        ])

        self.wait(0.3)
        self.play(FadeIn(VGroup(low_temp_label, low_temp_desc), shift=RIGHT), run_time=0.6)
        self.play(FadeIn(low_bars), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(VGroup(high_temp_label, high_temp_desc), shift=LEFT), run_time=0.6)
        self.play(FadeIn(high_bars), run_time=0.5)

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
        definition.shift(UP * 2.2)
        self.play(Write(definition), run_time=0.7)

        # Example
        example_label = Text('Example: "The cat"', font_size=HEADING_FONT_SIZE, color=WHITE, weight=BOLD)
        example_label.shift(UP * 1.2)
        self.play(Write(example_label), run_time=0.5)

        # Probability table
        words_probs = [
            ("meows", 0.30),
            ("sleeps", 0.25),
            ("eats", 0.24),
            ("plays", 0.16),
            ("is", 0.05)
        ]

        cumulative = 0
        prob_rows = VGroup()
        for word, prob in words_probs:
            cumulative += prob

            word_text = Text(word, font_size=SMALL_FONT_SIZE, color=WHITE)
            prob_text = Text(f"{prob:.2f}", font_size=SMALL_FONT_SIZE, color=ACCENT_CYAN)
            cumul_text = Text(f"Σ={cumulative:.2f}", font_size=SMALL_FONT_SIZE, color=ACCENT_ORANGE)

            # Highlight if within top-p=0.8
            if cumulative <= 0.8:
                color = ACCENT_GREEN
                check = Text("✓", font_size=SMALL_FONT_SIZE, color=color)
            else:
                color = ACCENT_RED
                check = Text("✗", font_size=SMALL_FONT_SIZE, color=color)

            row = VGroup(word_text, prob_text, cumul_text, check).arrange(RIGHT, buff=0.5)
            prob_rows.add(row)

        prob_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN * 0.3)

        # Threshold line
        threshold_text = Text(
            "If top_p = 0.8, only first 3 tokens considered",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_YELLOW,
            weight=BOLD
        )
        threshold_text.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        for row in prob_rows:
            self.play(FadeIn(row), run_time=0.3)
            self.wait(0.1)

        self.wait(0.3)
        self.play(FadeIn(threshold_text), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide58_TopKSampling(LLMSlide):
    """Slide 58: Top-k Sampling"""

    def construct(self):
        title = self.add_title("Top-k Sampling")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Limits selection to k most probable tokens",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2.2)
        self.play(Write(definition), run_time=0.7)

        # Analogy
        analogy = Text(
            "Like choosing only from the top candies in a jar",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_YELLOW
        )
        analogy.shift(UP * 1.3)
        self.play(FadeIn(analogy), run_time=0.6)

        # Example
        example_label = Text("If top_k = 2:", font_size=HEADING_FONT_SIZE, color=WHITE, weight=BOLD)
        example_label.shift(UP * 0.3)
        self.play(Write(example_label), run_time=0.5)

        # Token list
        tokens = [
            ("meows", 0.30, True),
            ("sleeps", 0.25, True),
            ("eats", 0.24, False),
            ("plays", 0.16, False),
            ("is", 0.05, False)
        ]

        token_objects = VGroup()
        for word, prob, included in tokens:
            word_text = Text(word, font_size=BODY_FONT_SIZE, color=WHITE)
            prob_text = Text(f"{prob:.2f}", font_size=BODY_FONT_SIZE, color=ACCENT_CYAN)

            if included:
                status = Text("✓ Included", font_size=SMALL_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
                row_color = ACCENT_GREEN
            else:
                status = Text("✗ Excluded", font_size=SMALL_FONT_SIZE, color=ACCENT_RED)
                row_color = ACCENT_RED

            row = VGroup(word_text, prob_text, status).arrange(RIGHT, buff=0.5)
            box = SurroundingRectangle(row, color=row_color, buff=0.15, stroke_width=2)

            token_objects.add(VGroup(box, row))

        token_objects.arrange(DOWN, buff=0.2).shift(DOWN * 1)

        for token_obj in token_objects:
            self.play(FadeIn(token_obj), run_time=0.3)
            self.wait(0.05)

        # Note
        note = Text(
            "Pros: More coherent | Cons: Less creative",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_ORANGE
        )
        note.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        self.play(FadeIn(note), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide59_SystemPrompt(LLMSlide):
    """Slide 59: System Prompt (Metaprompt)"""

    def construct(self):
        title = self.add_title("System Prompt (Metaprompt)")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Sets behavior parameters for the entire conversation",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2.2)
        self.play(Write(definition), run_time=0.7)

        # Key properties
        properties = [
            "✓ Valid for entire conversation",
            "✓ Not visible to end user",
            "✓ Set by LLM provider"
        ]

        prop_objects = self.create_bullet_list(properties, font_size=BODY_FONT_SIZE)
        prop_objects.shift(UP * 0.8)

        for prop in prop_objects:
            self.play(FadeIn(prop, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        # Example
        example_label = Text("Example:", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        example_label.shift(DOWN * 0.3)

        example_code = """You are a friendly and helpful assistant.
Answer questions concisely and clearly."""

        code_box = Rectangle(
            width=10,
            height=1.2,
            fill_opacity=0.9,
            fill_color=DARK_GRAY,
            stroke_color=ACCENT_GREEN,
            stroke_width=2
        )
        code_text = Text(example_code, font_size=SMALL_FONT_SIZE, color=WHITE, line_spacing=1.3, font="Monospace")
        code_text.move_to(code_box.get_center())
        code_group = VGroup(code_box, code_text)
        code_group.next_to(example_label, DOWN, buff=0.3)

        self.wait(0.3)
        self.play(Write(example_label), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(code_group), run_time=0.6)

        # Additional parameters
        params = Text(
            "Other parameters: max_tokens, model, role",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_YELLOW
        )
        params.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        self.play(FadeIn(params), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide60_HuggingFaceIntro(CodeSlide):
    """Slide 60: Hugging Face Introduction"""

    def construct(self):
        title = self.add_title("Hugging Face: LLM Toolkit")
        self.play(Write(title), run_time=0.5)

        # Key features
        features = [
            "🤗 Open-source transformers library",
            "📚 10,000+ datasets (NLP, vision, audio)",
            "☁️ Cloud API (no local GPU needed)"
        ]

        feature_objects = self.create_bullet_list(features, font_size=BODY_FONT_SIZE)
        feature_objects.shift(UP * 1.8)

        for feature in feature_objects:
            self.play(FadeIn(feature, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        # Code example
        code_example = """from transformers import pipeline

model_name = "facebook/opt-1.3b"
generator = pipeline("text-generation", 
                    model=model_name)

prompt = "AI is transforming the world because"
output = generator(prompt, max_length=50)
print(output[0]['generated_text'])"""

        code_label = Text("Example:", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        code_label.shift(UP * 0.2)

        code_box = Rectangle(
            width=11,
            height=3,
            fill_opacity=0.95,
            fill_color=DARK_GRAY,
            stroke_color=ACCENT_GREEN,
            stroke_width=3
        )
        code_text = Text(
            code_example,
            font_size=TINY_FONT_SIZE + 2,
            color=ACCENT_GREEN,
            line_spacing=1.2,
            font="Monospace"
        )
        code_text.move_to(code_box.get_center())

        if code_text.width > code_box.width * 0.95:
            code_text.scale((code_box.width * 0.95) / code_text.width)

        code_group = VGroup(code_box, code_text)
        code_group.next_to(code_label, DOWN, buff=0.3)

        self.wait(0.3)
        self.play(Write(code_label), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(code_group), run_time=0.7)

        # Note
        note = Text(
            "Visit: huggingface.co",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        note.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        self.play(FadeIn(note), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()
