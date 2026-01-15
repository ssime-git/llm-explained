"""
Part 6: Overall Architecture
Slides 42-43: Transformer architecture visualization
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

        # Simplified architecture diagram
        # Input
        input_box = Rectangle(width=2, height=0.6, color=ACCENT_CYAN, stroke_width=3)
        input_box.shift(LEFT * 4 + DOWN * 2.8)
        input_label = Text("Input\nEmbedding", font_size=TINY_FONT_SIZE, color=WHITE)
        input_label.move_to(input_box.get_center())

        # Encoder stack
        encoder_layers = VGroup()
        for i in range(3):
            # Multi-head attention
            mha = Rectangle(width=2, height=0.45, color=ACCENT_GREEN, stroke_width=2, fill_opacity=0.2, fill_color=ACCENT_GREEN)
            mha_label = Text("Multi-Head\nAttention", font_size=TINY_FONT_SIZE - 2, color=WHITE)
            mha_label.scale(0.7).move_to(mha.get_center())

            # Feed forward
            ff = Rectangle(width=2, height=0.45, color=ACCENT_ORANGE, stroke_width=2, fill_opacity=0.2, fill_color=ACCENT_ORANGE)
            ff_label = Text("Feed\nForward", font_size=TINY_FONT_SIZE - 2, color=WHITE)
            ff_label.scale(0.7).move_to(ff.get_center())

            layer = VGroup(VGroup(mha, mha_label), VGroup(ff, ff_label)).arrange(DOWN, buff=0.08)
            encoder_layers.add(layer)

        encoder_layers.arrange(DOWN, buff=0.15).scale(0.75)
        encoder_layers.next_to(input_box, UP, buff=0.25)

        encoder_box = SurroundingRectangle(encoder_layers, color=ACCENT_GREEN, buff=0.2, stroke_width=3)
        encoder_title = Text("ENCODER", font_size=BODY_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        encoder_title.next_to(encoder_box, UP, buff=0.1)

        # Decoder stack
        decoder_layers = VGroup()
        for i in range(3):
            # Masked multi-head attention
            mmha = Rectangle(width=2, height=0.35, color=ACCENT_PURPLE, stroke_width=2, fill_opacity=0.2, fill_color=ACCENT_PURPLE)
            mmha_label = Text("Masked MHA", font_size=TINY_FONT_SIZE - 4, color=WHITE)
            mmha_label.scale(0.6).move_to(mmha.get_center())

            # Cross attention
            ca = Rectangle(width=2, height=0.35, color=ACCENT_CYAN, stroke_width=2, fill_opacity=0.2, fill_color=ACCENT_CYAN)
            ca_label = Text("Cross Attn", font_size=TINY_FONT_SIZE - 4, color=WHITE)
            ca_label.scale(0.6).move_to(ca.get_center())

            # Feed forward
            ff = Rectangle(width=2, height=0.35, color=ACCENT_ORANGE, stroke_width=2, fill_opacity=0.2, fill_color=ACCENT_ORANGE)
            ff_label = Text("Feed Fwd", font_size=TINY_FONT_SIZE - 4, color=WHITE)
            ff_label.scale(0.6).move_to(ff.get_center())

            layer = VGroup(
                VGroup(mmha, mmha_label),
                VGroup(ca, ca_label),
                VGroup(ff, ff_label)
            ).arrange(DOWN, buff=0.04)
            decoder_layers.add(layer)

        decoder_layers.arrange(DOWN, buff=0.12).scale(0.65)
        decoder_layers.shift(RIGHT * 3.5 + DOWN * 0.3)

        decoder_box = SurroundingRectangle(decoder_layers, color=ACCENT_ORANGE, buff=0.2, stroke_width=3)
        decoder_title = Text("DECODER", font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        decoder_title.next_to(decoder_box, UP, buff=0.1)

        # Output
        output_box = Rectangle(width=2, height=0.6, color=ACCENT_CYAN, stroke_width=3)
        output_box.next_to(decoder_layers, DOWN, buff=0.3)
        output_label = Text("Output\nProbabilities", font_size=TINY_FONT_SIZE, color=WHITE)
        output_label.move_to(output_box.get_center())

        # Connections
        enc_to_dec = Arrow(
            encoder_box.get_right(),
            decoder_box.get_left(),
            color=ACCENT_CYAN,
            stroke_width=3
        )

        # Animate
        self.wait(0.2)
        self.play(FadeIn(VGroup(input_box, input_label)), run_time=0.4)
        self.wait(0.2)

        self.play(
            Create(encoder_box),
            Write(encoder_title),
            FadeIn(encoder_layers),
            run_time=0.8
        )
        self.wait(0.3)

        self.play(GrowArrow(enc_to_dec), run_time=0.5)
        self.wait(0.2)

        self.play(
            Create(decoder_box),
            Write(decoder_title),
            FadeIn(decoder_layers),
            run_time=0.8
        )
        self.wait(0.3)

        self.play(FadeIn(VGroup(output_box, output_label)), run_time=0.4)

        # Key components note
        note = Text(
            "Each layer includes:\n• Attention mechanism\n• Normalization\n• Residual connections",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_YELLOW,
            line_spacing=1.2
        )
        note.to_edge(DOWN, buff=0.5)

        self.wait(0.3)
        self.play(FadeIn(note), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()
