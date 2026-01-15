"""
Part 6: Overall Architecture
Slides 42-43: Complete transformer architecture
"""

from manim import *
from manim_slides import Slide
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.custom_scenes import *
from utils.animations import *
from assets.styles.theme_config import *


class Slide42_TransformerArchitecture(LLMSlide):
    """Slide 42-43: Complete Transformer Architecture"""

    def construct(self):
        title = self.add_title("Complete Transformer Architecture")
        self.play(Write(title), run_time=0.5)

        # Stacked transformer blocks
        num_blocks = 3

        blocks = VGroup()
        for i in range(num_blocks):
            # Multi-head attention
            mha = Rectangle(width=3, height=0.6, color=ACCENT_CYAN, stroke_width=2)
            mha_text = Text("Multi-Head Attention", font_size=TINY_FONT_SIZE, color=WHITE)
            mha_text.move_to(mha.get_center())

            # Feed forward
            ff = Rectangle(width=3, height=0.6, color=ACCENT_ORANGE, stroke_width=2)
            ff_text = Text("Feed Forward", font_size=TINY_FONT_SIZE, color=WHITE)
            ff_text.move_to(ff.get_center())

            # Add & Norm layers
            norm1 = Rectangle(width=3, height=0.3, color=ACCENT_GREEN, stroke_width=1)
            norm1_text = Text("Add & Norm", font_size=TINY_FONT_SIZE * 0.7, color=WHITE)
            norm1_text.move_to(norm1.get_center())

            norm2 = Rectangle(width=3, height=0.3, color=ACCENT_GREEN, stroke_width=1)
            norm2_text = Text("Add & Norm", font_size=TINY_FONT_SIZE * 0.7, color=WHITE)
            norm2_text.move_to(norm2.get_center())

            block = VGroup(
                VGroup(mha, mha_text),
                VGroup(norm1, norm1_text),
                VGroup(ff, ff_text),
                VGroup(norm2, norm2_text)
            ).arrange(DOWN, buff=0.1)

            blocks.add(block)

        blocks.arrange(DOWN, buff=0.3).scale(0.9).shift(DOWN * 0.2)

        # Input and output
        input_box = Rectangle(width=3, height=0.5, color=PRIMARY_BLUE, stroke_width=3)
        input_text = Text("Input Embeddings", font_size=SMALL_FONT_SIZE, color=WHITE)
        input_text.move_to(input_box.get_center())
        input_group = VGroup(input_box, input_text)
        input_group.next_to(blocks, UP, buff=0.3)

        output_box = Rectangle(width=3, height=0.5, color=ACCENT_PURPLE, stroke_width=3)
        output_text = Text("Output Probabilities", font_size=SMALL_FONT_SIZE, color=WHITE)
        output_text.move_to(output_box.get_center())
        output_group = VGroup(output_box, output_text)
        output_group.next_to(blocks, DOWN, buff=0.3)

        # Animate
        self.play(FadeIn(input_group), run_time=0.5)
        self.wait(0.2)

        for block in blocks:
            self.play(FadeIn(block, shift=UP), run_time=0.4)
            self.wait(0.1)

        self.wait(0.2)
        self.play(FadeIn(output_group), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()
