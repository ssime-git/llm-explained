"""
Custom scene classes for LLM Explained presentation.
Provides base classes with common functionality for slide creation.
"""

from manim import *
from manim_slides import Slide
import sys
import os

# Add assets to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from styles.theme_config import *


class LLMSlide(Slide):
    """
    Base class for all LLM presentation slides.
    Provides common functionality and styling.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title_obj = None
        self.subtitle_obj = None

    def add_title(self, title_text, subtitle_text=None, color=ACCENT_CYAN):
        """
        Adds a title and optional subtitle to the slide.

        Args:
            title_text: Main title text
            subtitle_text: Optional subtitle text
            color: Title color

        Returns:
            VGroup containing title elements
        """
        self.title_obj = Text(title_text, **get_title_style(), color=color)
        self.title_obj.to_edge(UP, buff=0.5)

        if subtitle_text:
            self.subtitle_obj = Text(subtitle_text, **get_subtitle_style())
            self.subtitle_obj.next_to(self.title_obj, DOWN, buff=0.3)
            title_group = VGroup(self.title_obj, self.subtitle_obj)
        else:
            title_group = VGroup(self.title_obj)

        return title_group

    def add_gradient_background(self, top_color=DARK_BLUE, bottom_color=ACCENT_CYAN, opacity=0.2):
        """
        Adds a gradient background to the slide.

        Args:
            top_color: Top color of gradient
            bottom_color: Bottom color of gradient
            opacity: Background opacity
        """
        bg = create_gradient_background(top_color, bottom_color, opacity)
        self.add(bg)

    def highlight_word(self, text_obj, word_index, color=ACCENT_YELLOW):
        """
        Highlights a specific word in a Text object.

        Args:
            text_obj: Text object to highlight
            word_index: Index of word to highlight
            color: Highlight color

        Returns:
            Animation to highlight the word
        """
        return ApplyMethod(text_obj[word_index].set_color, color)

    def create_definition_box(self, definition_text, title=None):
        """
        Creates a styled definition box.

        Args:
            definition_text: Definition content
            title: Optional title for the definition

        Returns:
            VGroup containing the definition box
        """
        box = Rectangle(
            width=config.frame_width * 0.8,
            height=2,
            stroke_color=ACCENT_CYAN,
            stroke_width=3,
            fill_opacity=0.1,
            fill_color=ACCENT_CYAN
        )

        text = Text(definition_text, font_size=BODY_FONT_SIZE, color=WHITE)
        text.move_to(box.get_center())

        # Scale text if needed
        if text.width > box.width * 0.9:
            text.scale((box.width * 0.9) / text.width)

        group = VGroup(box, text)

        if title:
            title_text = Text(title, **get_heading_style())
            title_text.next_to(box, UP, buff=0.2)
            group = VGroup(title_text, box, text)

        return group

    def create_bullet_list(self, items, color=WHITE, font_size=BODY_FONT_SIZE):
        """
        Creates a bullet point list.

        Args:
            items: List of text items
            color: Text color
            font_size: Font size

        Returns:
            VGroup containing all bullet items
        """
        bullets = VGroup()

        for item in items:
            bullet = Text("•", font_size=font_size, color=color)
            text = Text(item, font_size=font_size, color=color)
            text.next_to(bullet, RIGHT, buff=0.2)
            bullet_group = VGroup(bullet, text)
            bullets.add(bullet_group)

        bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.3)

        return bullets

    def create_two_column_layout(self, left_content, right_content, gap=1):
        """
        Creates a two-column layout.

        Args:
            left_content: Mobject for left column
            right_content: Mobject for right column
            gap: Gap between columns

        Returns:
            VGroup containing both columns
        """
        left_content.move_to(LEFT * (config.frame_width / 4 + gap / 2))
        right_content.move_to(RIGHT * (config.frame_width / 4 + gap / 2))

        return VGroup(left_content, right_content)

    def create_three_column_layout(self, left_content, center_content, right_content):
        """
        Creates a three-column layout.

        Args:
            left_content: Mobject for left column
            center_content: Mobject for center column
            right_content: Mobject for right column

        Returns:
            VGroup containing all columns
        """
        columns = VGroup(left_content, center_content, right_content)
        columns.arrange(RIGHT, buff=0.5)

        return columns

    def fade_in_sequence(self, *mobjects, lag_ratio=0.3, run_time=FADE_IN_TIME):
        """
        Fades in multiple objects in sequence.

        Args:
            mobjects: Mobjects to fade in
            lag_ratio: Time delay between each object
            run_time: Total run time

        Returns:
            Animation
        """
        return AnimationGroup(
            *[FadeIn(mob) for mob in mobjects],
            lag_ratio=lag_ratio,
            run_time=run_time
        )

    def write_sequence(self, *mobjects, lag_ratio=0.3, run_time=1):
        """
        Writes multiple objects in sequence.

        Args:
            mobjects: Mobjects to write
            lag_ratio: Time delay between each object
            run_time: Total run time

        Returns:
            Animation
        """
        return AnimationGroup(
            *[Write(mob) for mob in mobjects],
            lag_ratio=lag_ratio,
            run_time=run_time
        )


class TitleSlide(LLMSlide):
    """
    Special slide class for title/transition slides.
    """

    def create_title_slide(self, main_title, subtitle=None, background=True):
        """
        Creates a complete title slide.

        Args:
            main_title: Main title text
            subtitle: Optional subtitle
            background: Whether to add gradient background

        Returns:
            VGroup containing title elements
        """
        if background:
            self.add_gradient_background()

        title = Text(main_title, font_size=TITLE_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)

        if subtitle:
            sub = Text(subtitle, **get_subtitle_style())
            title_group = VGroup(title, sub).arrange(DOWN, buff=0.5)
        else:
            title_group = VGroup(title)

        title_group.move_to(ORIGIN)

        return title_group


class FormulaSlide(LLMSlide):
    """
    Special slide class for mathematical formulas.
    """

    def create_formula_with_description(self, formula_tex, description_text, variable_descriptions=None):
        """
        Creates a formula with description and variable explanations.

        Args:
            formula_tex: LaTeX formula string
            description_text: Description of the formula
            variable_descriptions: Dict of variable names to descriptions

        Returns:
            VGroup containing formula and descriptions
        """
        # Formula
        formula = MathTex(formula_tex, font_size=HEADING_FONT_SIZE, color=ACCENT_CYAN)

        # Description
        description = Text(description_text, font_size=BODY_FONT_SIZE, color=WHITE)
        description.next_to(formula, DOWN, buff=0.5)

        group = VGroup(formula, description)

        # Variable descriptions
        if variable_descriptions:
            var_group = VGroup()
            for var, desc in variable_descriptions.items():
                var_text = MathTex(f"{var}:", font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE)
                desc_text = Text(desc, font_size=SMALL_FONT_SIZE, color=WHITE)
                var_line = VGroup(var_text, desc_text).arrange(RIGHT, buff=0.2)
                var_group.add(var_line)

            var_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            var_group.next_to(description, DOWN, buff=0.5)
            group.add(var_group)

        return group

    def reveal_formula_step_by_step(self, formula_parts):
        """
        Reveals a formula step by step.

        Args:
            formula_parts: List of formula parts to reveal sequentially

        Returns:
            List of animations
        """
        animations = []
        for part in formula_parts:
            animations.append(Write(part))

        return animations


class CodeSlide(LLMSlide):
    """
    Special slide class for code examples.
    """

    def create_code_block(self, code_text, language="python", title=None):
        """
        Creates a styled code block.

        Args:
            code_text: Code to display
            language: Programming language
            title: Optional title

        Returns:
            VGroup containing code block
        """
        # Code block with dark background
        bg = Rectangle(
            width=config.frame_width * 0.8,
            height=4,
            fill_opacity=0.9,
            fill_color=DARK_GRAY,
            stroke_color=ACCENT_GREEN,
            stroke_width=2
        )

        code = Code(
            code=code_text,
            language=language,
            font="Monospace",
            font_size=SMALL_FONT_SIZE,
            background="window",
            style="monokai"
        )

        code.move_to(bg.get_center())

        group = VGroup(bg, code)

        if title:
            title_text = Text(title, **get_heading_style())
            title_text.next_to(bg, UP, buff=0.3)
            group = VGroup(title_text, bg, code)

        return group
