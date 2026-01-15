"""
Part 5: Text Generation Process
Slides 32-41: Complete text generation pipeline
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


class Slide32_TextGenerationTitle(TitleSlide):
    """Slide 32: Text Generation Title"""

    def construct(self):
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color=DARK_BLUE,
            stroke_width=0
        )
        self.add(bg)

        title = Text("Text Generation", font_size=TITLE_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        self.play(FadeIn(title, scale=1.2), run_time=1)
        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide33_ProbabilityBasedGeneration(LLMSlide):
    """Slide 33: Text Generation based on probabilities"""

    def construct(self):
        title = self.add_title("Text Generation based on probabilities")
        self.play(Write(title), run_time=0.5)

        # Context
        context = Text('"I heard a dog"', font_size=HEADING_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        context.shift(UP * 2)
        self.play(Write(context), run_time=0.5)

        # Probability distribution
        words_probs = [
            ("bark", 0.87, ACCENT_GREEN),
            ("outside", 0.35, PRIMARY_BLUE),
            (".", 0.31, PRIMARY_BLUE),
            ("in", 0.09, LIGHT_GRAY),
            ("run", 0.04, LIGHT_GRAY),
            ("near", 0.04, LIGHT_GRAY)
        ]

        prob_objects = VGroup()
        for word, prob, color in words_probs:
            bar_width = prob * 5
            bar = Rectangle(
                width=bar_width,
                height=0.3,
                fill_opacity=0.8,
                fill_color=color,
                stroke_width=1,
                stroke_color=WHITE
            )
            word_text = Text(word, font_size=SMALL_FONT_SIZE, color=WHITE)
            prob_text = Text(f"{prob:.2f}", font_size=SMALL_FONT_SIZE, color=color, weight=BOLD)

            row = VGroup(word_text, bar, prob_text).arrange(RIGHT, buff=0.2)
            prob_objects.add(row)

        prob_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(DOWN * 0.2)

        for prob_row in prob_objects:
            self.play(FadeIn(prob_row), run_time=0.3)
            self.wait(0.05)

        # Question
        question = Text(
            "How do we go from embeddings to probabilities?",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_ORANGE
        )
        question.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        self.play(FadeIn(question), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide34_EmbeddingPositionalEncoding(LLMSlide):
    """Slide 34: Token embedding + positional encoding"""

    def construct(self):
        title = self.add_title("Token Embedding + Positional Encoding")
        self.play(Write(title), run_time=0.5)

        # Example tokens with positions
        tokens = ["I", "heard", "a", "dog", "???"]
        positions = [1, 2, 3, 4, 5]

        token_rows = VGroup()
        for token, pos in zip(tokens, positions):
            pos_text = Text(f"Pos {pos}", font_size=SMALL_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
            token_text = Text(token, font_size=BODY_FONT_SIZE, color=WHITE, weight=BOLD)

            if token == "???":
                embedding_text = Text("???", font_size=SMALL_FONT_SIZE, color=ACCENT_YELLOW)
            else:
                # Example embedding
                embedding = f"[{pos}, {pos*2}, {pos+3}, {pos*3}]"
                embedding_text = Text(embedding, font_size=TINY_FONT_SIZE, color=ACCENT_CYAN, font="Monospace")

            row = VGroup(pos_text, token_text, embedding_text).arrange(RIGHT, buff=0.4)
            token_rows.add(row)

        token_rows.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(DOWN * 0.3)

        for row in token_rows:
            self.play(FadeIn(row, shift=RIGHT), run_time=0.3)
            self.wait(0.05)

        # Explanation
        explanation = Text(
            "Position encoding helps the model understand word order",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_GREEN
        )
        explanation.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        self.play(FadeIn(explanation), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide35_QueryKeyValue(FormulaSlide):
    """Slide 35-39: Attention Calculation Steps (combined)"""

    def construct(self):
        title = self.add_title("Attention Calculation: Q, K, V Matrices")
        self.play(Write(title), run_time=0.5)

        # Step 1: Q, K, V matrices
        step1 = Text("Step 1: Transform embeddings to Q, K, V", font_size=BODY_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        step1.shift(UP * 2)
        self.play(Write(step1), run_time=0.6)

        # Example matrices
        Q_label = Text("Q (Query)", font_size=SMALL_FONT_SIZE, color=ACCENT_GREEN)
        K_label = Text("K (Key)", font_size=SMALL_FONT_SIZE, color=ACCENT_ORANGE)
        V_label = Text("V (Value)", font_size=SMALL_FONT_SIZE, color=ACCENT_PURPLE)

        Q_matrix = Text("[[0.8, 1.2],\n [1.0, 0.9]]", font_size=TINY_FONT_SIZE, font="Monospace", color=WHITE)
        K_matrix = Text("[[0.9, 1.1],\n [1.1, 0.8]]", font_size=TINY_FONT_SIZE, font="Monospace", color=WHITE)
        V_matrix = Text("[[2.1, 3.2],\n [2.8, 3.5]]", font_size=TINY_FONT_SIZE, font="Monospace", color=WHITE)

        matrices = VGroup(
            VGroup(Q_label, Q_matrix).arrange(DOWN, buff=0.2),
            VGroup(K_label, K_matrix).arrange(DOWN, buff=0.2),
            VGroup(V_label, V_matrix).arrange(DOWN, buff=0.2)
        ).arrange(RIGHT, buff=0.8).shift(UP * 0.3)

        self.play(FadeIn(matrices), run_time=0.8)
        self.wait(0.5)
        self.next_slide()

        # Step 2: Attention scores
        self.play(FadeOut(step1), run_time=0.3)
        step2 = Text("Step 2: Calculate Attention Scores", font_size=BODY_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        step2.shift(UP * 2)
        self.play(Write(step2), run_time=0.6)

        formula = MathTex(r"\text{Scores} = \frac{Q \cdot K^T}{\sqrt{d_k}}", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE)
        formula.shift(DOWN * 0.5)

        self.play(Write(formula), run_time=0.8)
        self.wait(0.5)
        self.next_slide()

        # Step 3: Softmax
        self.play(FadeOut(step2), FadeOut(formula), run_time=0.3)
        step3 = Text("Step 3: Apply Softmax", font_size=BODY_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        step3.shift(UP * 2)
        self.play(Write(step3), run_time=0.6)

        softmax = MathTex(r"\text{Attention} = \text{softmax}(\text{Scores})", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN)
        softmax.shift(DOWN * 0.5)

        self.play(Write(softmax), run_time=0.8)
        self.wait(0.5)
        self.next_slide()

        # Step 4: Weighted sum
        self.play(FadeOut(step3), FadeOut(softmax), run_time=0.3)
        step4 = Text("Step 4: Weighted Sum with V", font_size=BODY_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        step4.shift(UP * 2)
        self.play(Write(step4), run_time=0.6)

        weighted_sum = MathTex(r"\text{Output} = \text{Attention} \cdot V", font_size=HEADING_FONT_SIZE, color=ACCENT_PURPLE)
        weighted_sum.shift(DOWN * 0.5)

        self.play(Write(weighted_sum), run_time=0.8)
        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide40_ArchitectureSummary(LLMSlide):
    """Slide 40: Overall Architecture Summary"""

    def construct(self):
        title = self.add_title("Overall Transformer Architecture")
        self.play(Write(title), run_time=0.5)

        # Simple architecture diagram
        encoder_box = Rectangle(width=3, height=5, color=ACCENT_GREEN, stroke_width=4)
        encoder_box.shift(LEFT * 3.5)
        encoder_label = Text("ENCODER", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        encoder_label.next_to(encoder_box, UP, buff=0.2)

        decoder_box = Rectangle(width=3, height=5, color=ACCENT_ORANGE, stroke_width=4)
        decoder_box.shift(RIGHT * 3.5)
        decoder_label = Text("DECODER", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        decoder_label.next_to(decoder_box, UP, buff=0.2)

        # Connection arrow
        connection = Arrow(encoder_box.get_right(), decoder_box.get_left(), color=ACCENT_CYAN, stroke_width=4)

        # Labels
        input_label = Text("Input", font_size=SMALL_FONT_SIZE, color=WHITE)
        input_label.next_to(encoder_box, DOWN, buff=0.3)

        output_label = Text("Output", font_size=SMALL_FONT_SIZE, color=WHITE)
        output_label.next_to(decoder_box, DOWN, buff=0.3)

        self.play(Create(encoder_box), Write(encoder_label), run_time=0.6)
        self.wait(0.2)
        self.play(GrowArrow(connection), run_time=0.5)
        self.wait(0.2)
        self.play(Create(decoder_box), Write(decoder_label), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(input_label), FadeIn(output_label), run_time=0.4)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide41_PredictionLayer(LLMSlide):
    """Slide 41: Prediction Layer"""

    def construct(self):
        title = self.add_title("Text Generation: Prediction Layer")
        self.play(Write(title), run_time=0.5)

        # Flow diagram
        steps = [
            ("Contextual Embedding", "[4, 10, 3, 2, 5]", ACCENT_CYAN),
            ("Feed Forward Network", "↓", WHITE),
            ("Linear Layer", "↓", WHITE),
            ("Softmax", "↓", WHITE),
            ("Probabilities", "bark: 0.87\nrun: 0.09\neat: 0.04", ACCENT_GREEN)
        ]

        flow = VGroup()
        for step_name, step_val, color in steps:
            if "↓" in step_val:
                arrow = Text(step_val, font_size=HEADING_FONT_SIZE, color=color)
                flow.add(arrow)
            else:
                step_text = Text(step_name, font_size=BODY_FONT_SIZE, color=color, weight=BOLD)
                val_text = Text(step_val, font_size=SMALL_FONT_SIZE, color=WHITE, font="Monospace", line_spacing=1.2)
                step_group = VGroup(step_text, val_text).arrange(DOWN, buff=0.2)
                box = SurroundingRectangle(step_group, color=color, buff=0.2, stroke_width=3)
                flow.add(VGroup(box, step_group))

        flow.arrange(DOWN, buff=0.2).shift(DOWN * 0.2)

        for step in flow:
            self.play(FadeIn(step), run_time=0.4)
            self.wait(0.1)

        self.wait(PAUSE_TIME)
        self.next_slide()
