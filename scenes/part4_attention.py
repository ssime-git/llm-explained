"""
Part 4: Attention Mechanism
Slides 29-31: Multi-head attention and Grouped Query Attention
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


class Slide29_MultiHeadAttention(LLMSlide):
    """Slide 29: Multi-Head Attention"""

    def construct(self):
        title = self.add_title("Multi-Head Attention Mechanism")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Multiple attention heads capture different types of relationships",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2.2)
        self.play(Write(definition), run_time=0.7)

        # Example sentence
        sentence = Text(
            '"The jaguar hunts its prey in the dense jungle"',
            font_size=BODY_FONT_SIZE,
            color=WHITE
        )
        sentence.shift(UP * 1.3)
        self.play(FadeIn(sentence), run_time=0.5)

        # Three heads
        heads = [
            ("Head 1", "Syntactic relations\n(subject-verb)", ACCENT_GREEN),
            ("Head 2", "Semantic relations\n(predator-prey)", ACCENT_ORANGE),
            ("Head 3", "Environmental context\n(action-setting)", ACCENT_PURPLE)
        ]

        head_objects = VGroup()
        for head_name, head_desc, color in heads:
            title_text = Text(head_name, font_size=BODY_FONT_SIZE, color=color, weight=BOLD)
            desc_text = Text(head_desc, font_size=SMALL_FONT_SIZE, color=WHITE, line_spacing=1.2)

            head_content = VGroup(title_text, desc_text).arrange(DOWN, buff=0.2)
            box = SurroundingRectangle(head_content, color=color, buff=0.3, stroke_width=3)

            head_objects.add(VGroup(box, head_content))

        head_objects.arrange(RIGHT, buff=0.4).scale(0.8).shift(DOWN * 0.5)

        for head in head_objects:
            self.play(FadeIn(head, shift=UP), run_time=0.5)
            self.wait(0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide30_AttentionMechanismDeep(LLMSlide):
    """Slide 30: Attention Mechanism Deep Dive"""

    def construct(self):
        title = self.add_title("Attention: Capturing Context")
        self.play(Write(title), run_time=0.5)

        # Example sentence with attention visualization
        sentence = "He took the mighty bat and hit a home run"
        words = sentence.split()

        word_objects = VGroup()
        for word in words:
            word_text = Text(word, font_size=SMALL_FONT_SIZE, color=WHITE)
            word_objects.add(word_text)

        word_objects.arrange(RIGHT, buff=0.3).shift(UP * 1.5)

        self.play(Write(word_objects), run_time=0.8)

        # Highlight "bat"
        bat_index = 4
        bat_word = word_objects[bat_index]

        highlight = SurroundingRectangle(bat_word, color=ACCENT_YELLOW, buff=0.1, stroke_width=4)
        self.play(Create(highlight), run_time=0.3)

        # Attention connections
        important_words = [1, 3, 6, 8, 9]  # took, mighty, hit, home, run
        weights = [0.15, 0.25, 0.30, 0.15, 0.15]

        self.wait(0.3)

        for idx, weight in zip(important_words, weights):
            line = Line(
                bat_word.get_bottom(),
                word_objects[idx].get_top(),
                color=ACCENT_CYAN,
                stroke_width=weight * 10,
                stroke_opacity=weight
            )
            self.play(Create(line), run_time=0.2)

        # Explanation
        explanation = Text(
            "Attention weights determine which words are most relevant",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_GREEN
        )
        explanation.to_edge(DOWN, buff=1)

        self.wait(0.3)
        self.play(FadeIn(explanation), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide31_GroupedQueryAttention(LLMSlide):
    """Slide 31: Grouped Query Attention"""

    def construct(self):
        title = self.add_title("Grouped Query Attention (GQA)")
        self.play(Write(title), run_time=0.5)

        # Description
        desc = Text(
            "Optimization: Group attention heads to reduce computational cost",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        desc.shift(UP * 2)
        self.play(Write(desc), run_time=0.7)

        # Before: Multiple independent heads
        before_label = Text("Traditional MHA", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        before_label.shift(LEFT * 4 + UP * 0.5)

        heads_before = VGroup(*[
            Circle(radius=0.3, color=ACCENT_ORANGE, stroke_width=3).shift(DOWN * i * 0.7)
            for i in range(4)
        ])
        heads_before.next_to(before_label, DOWN, buff=0.5)

        # After: Grouped heads
        after_label = Text("Grouped Query Attention", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        after_label.shift(RIGHT * 3 + UP * 0.5)

        group1 = VGroup(*[
            Circle(radius=0.25, color=ACCENT_GREEN, stroke_width=3).shift(RIGHT * i * 0.6)
            for i in range(2)
        ])
        group2 = VGroup(*[
            Circle(radius=0.25, color=ACCENT_GREEN, stroke_width=3).shift(RIGHT * i * 0.6)
            for i in range(2)
        ])
        grouped = VGroup(group1, group2).arrange(DOWN, buff=0.5)
        grouped.next_to(after_label, DOWN, buff=0.5)

        # Benefits
        benefits = Text(
            "✓ Reduced memory\n✓ Faster computation\n✓ Similar performance",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.3
        )
        benefits.to_edge(DOWN, buff=1)

        self.wait(0.3)
        self.play(FadeIn(VGroup(before_label, heads_before), shift=RIGHT), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(VGroup(after_label, grouped), shift=LEFT), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(benefits), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()
