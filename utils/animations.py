"""
Custom animation functions for LLM Explained presentation.
Provides reusable animation patterns.
"""

from manim import *
import sys
import os

# Add assets to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'assets'))
from styles.theme_config import *


def slide_in_from_left(mobject, run_time=0.5):
    """Slides an object in from the left."""
    mobject.save_state()
    mobject.shift(LEFT * config.frame_width)
    return Restore(mobject, run_time=run_time)


def slide_in_from_right(mobject, run_time=0.5):
    """Slides an object in from the right."""
    mobject.save_state()
    mobject.shift(RIGHT * config.frame_width)
    return Restore(mobject, run_time=run_time)


def slide_in_from_top(mobject, run_time=0.5):
    """Slides an object in from the top."""
    mobject.save_state()
    mobject.shift(UP * config.frame_height)
    return Restore(mobject, run_time=run_time)


def slide_in_from_bottom(mobject, run_time=0.5):
    """Slides an object in from the bottom."""
    mobject.save_state()
    mobject.shift(DOWN * config.frame_height)
    return Restore(mobject, run_time=run_time)


def pulse_animation(mobject, scale_factor=1.2, color=ACCENT_YELLOW, run_time=0.5):
    """
    Creates a pulse animation (scale up and down).

    Args:
        mobject: Object to pulse
        scale_factor: How much to scale
        color: Optional color change
        run_time: Animation duration

    Returns:
        Succession of animations
    """
    return Succession(
        mobject.animate.scale(scale_factor).set_color(color),
        mobject.animate.scale(1/scale_factor).set_color(WHITE),
        run_time=run_time
    )


def glow_animation(mobject, color=ACCENT_YELLOW, intensity=3, run_time=1):
    """
    Creates a glowing effect animation.

    Args:
        mobject: Object to make glow
        color: Glow color
        intensity: Glow intensity
        run_time: Animation duration

    Returns:
        Animation sequence
    """
    return Succession(
        ApplyMethod(mobject.set_stroke, color, intensity, 0.8, {"background": True}, run_time=run_time/2),
        ApplyMethod(mobject.set_stroke, WHITE, 0, 0, run_time=run_time/2)
    )


def highlight_box_animation(mobject, color=ACCENT_YELLOW, buff=0.1, run_time=0.5):
    """
    Creates a highlighting box around an object.

    Args:
        mobject: Object to highlight
        color: Highlight color
        buff: Buffer around object
        run_time: Animation duration

    Returns:
        Tuple of (highlight_box, create_animation, uncreate_animation)
    """
    box = SurroundingRectangle(mobject, color=color, buff=buff, stroke_width=4)
    return box, Create(box, run_time=run_time), Uncreate(box, run_time=run_time)


def typewriter_text(text_obj, run_time=None):
    """
    Creates a typewriter effect for text.

    Args:
        text_obj: Text object to animate
        run_time: Optional run time (defaults to length-based)

    Returns:
        AddTextLetterByLetter animation
    """
    if run_time is None:
        run_time = len(text_obj.text) * 0.05  # 0.05 seconds per character

    return AddTextLetterByLetter(text_obj, run_time=run_time)


def fade_transition(scene, from_mobjects, to_mobjects, run_time=0.5):
    """
    Fades out one set of objects and fades in another.

    Args:
        scene: The scene object
        from_mobjects: Objects to fade out
        to_mobjects: Objects to fade in
        run_time: Transition duration

    Returns:
        AnimationGroup
    """
    return AnimationGroup(
        FadeOut(*from_mobjects, run_time=run_time),
        FadeIn(*to_mobjects, run_time=run_time)
    )


def stagger_fade_in(mobjects, lag_ratio=0.2, run_time=1):
    """
    Fades in multiple objects with staggered timing.

    Args:
        mobjects: List of mobjects to fade in
        lag_ratio: Delay between each object
        run_time: Total animation time

    Returns:
        AnimationGroup
    """
    return AnimationGroup(
        *[FadeIn(mob) for mob in mobjects],
        lag_ratio=lag_ratio,
        run_time=run_time
    )


def stagger_write(mobjects, lag_ratio=0.2, run_time=1):
    """
    Writes multiple objects with staggered timing.

    Args:
        mobjects: List of mobjects to write
        lag_ratio: Delay between each object
        run_time: Total animation time

    Returns:
        AnimationGroup
    """
    return AnimationGroup(
        *[Write(mob) for mob in mobjects],
        lag_ratio=lag_ratio,
        run_time=run_time
    )


def emphasize_word(text_obj, word_indices, color=ACCENT_ORANGE, run_time=0.3):
    """
    Emphasizes specific words in a text object.

    Args:
        text_obj: Text object
        word_indices: List of word indices to emphasize
        color: Emphasis color
        run_time: Animation duration

    Returns:
        AnimationGroup
    """
    animations = []
    for idx in word_indices:
        if idx < len(text_obj):
            animations.append(
                text_obj[idx].animate.set_color(color).scale(1.2)
            )

    return AnimationGroup(*animations, run_time=run_time)


def draw_connecting_line(obj1, obj2, color=WHITE, stroke_width=2, buff=0.1):
    """
    Draws a line connecting two objects.

    Args:
        obj1: First object
        obj2: Second object
        color: Line color
        stroke_width: Line thickness
        buff: Buffer from objects

    Returns:
        Line object
    """
    line = Line(
        obj1.get_center(),
        obj2.get_center(),
        color=color,
        stroke_width=stroke_width,
        buff=buff
    )
    return line


def create_attention_connection(source, target, weight=1.0, max_width=3, color=ACCENT_CYAN):
    """
    Creates an attention mechanism connection visualization.

    Args:
        source: Source object
        target: Target object
        weight: Attention weight (0-1)
        max_width: Maximum line width
        color: Connection color

    Returns:
        Line with width proportional to attention weight
    """
    line = Line(
        source.get_center(),
        target.get_center(),
        color=color,
        stroke_width=weight * max_width,
        stroke_opacity=weight * 0.8
    )
    return line


def matrix_highlight_row(matrix, row_index, color=ACCENT_YELLOW, run_time=0.5):
    """
    Highlights a specific row in a matrix.

    Args:
        matrix: Matrix object
        row_index: Row to highlight
        color: Highlight color
        run_time: Animation duration

    Returns:
        Animation
    """
    row = matrix.get_rows()[row_index]
    return Indicate(row, color=color, run_time=run_time)


def matrix_highlight_col(matrix, col_index, color=ACCENT_YELLOW, run_time=0.5):
    """
    Highlights a specific column in a matrix.

    Args:
        matrix: Matrix object
        col_index: Column to highlight
        color: Highlight color
        run_time: Animation duration

    Returns:
        Animation
    """
    col = matrix.get_columns()[col_index]
    return Indicate(col, color=color, run_time=run_time)


def vector_to_point_animation(vector_mobject, point_mobject, color=ACCENT_CYAN, run_time=1):
    """
    Animates a vector as an arrow pointing to a location.

    Args:
        vector_mobject: Vector representation
        point_mobject: Point in space
        color: Arrow color
        run_time: Animation duration

    Returns:
        Arrow and animation
    """
    arrow = Arrow(
        ORIGIN,
        point_mobject.get_center(),
        color=color,
        buff=0
    )
    return arrow, GrowArrow(arrow, run_time=run_time)


def probability_distribution_animation(words, probabilities, colors=None, run_time=1):
    """
    Animates a probability distribution as bars.

    Args:
        words: List of words
        probabilities: List of probabilities (0-1)
        colors: Optional list of colors for each bar
        run_time: Animation duration

    Returns:
        VGroup of bars and GrowFromEdge animations
    """
    bars = VGroup()
    animations = []

    if colors is None:
        colors = [PRIMARY_BLUE] * len(words)

    max_height = 3
    for i, (word, prob, color) in enumerate(zip(words, probabilities, colors)):
        # Word label
        label = Text(word, font_size=SMALL_FONT_SIZE, color=WHITE)

        # Probability bar
        bar_height = prob * max_height
        bar = Rectangle(
            width=0.5,
            height=bar_height,
            fill_opacity=0.8,
            fill_color=color,
            stroke_width=1,
            stroke_color=WHITE
        )

        # Probability value
        prob_text = Text(f"{prob:.2f}", font_size=TINY_FONT_SIZE, color=WHITE)

        # Arrange
        bar_group = VGroup(label, bar, prob_text).arrange(DOWN, buff=0.1)
        bars.add(bar_group)

        # Animation
        animations.append(GrowFromEdge(bar, DOWN))

    bars.arrange(RIGHT, buff=0.5)

    return bars, AnimationGroup(*animations, lag_ratio=0.2, run_time=run_time)


def timeline_animation(events, start_year, end_year, run_time=2):
    """
    Creates a timeline animation.

    Args:
        events: List of (year, event_name) tuples
        start_year: Timeline start year
        end_year: Timeline end year
        run_time: Animation duration

    Returns:
        Timeline VGroup and animation sequence
    """
    # Create timeline
    timeline_length = config.frame_width * 0.8
    timeline = Line(
        LEFT * timeline_length / 2,
        RIGHT * timeline_length / 2,
        color=WHITE
    )

    # Create events
    event_objects = VGroup()
    animations = []

    year_range = end_year - start_year

    for year, event_name in events:
        # Calculate position
        progress = (year - start_year) / year_range
        x_pos = -timeline_length / 2 + progress * timeline_length

        # Event point
        point = Dot(color=ACCENT_CYAN, radius=0.08)
        point.move_to([x_pos, 0, 0])

        # Year label
        year_label = Text(str(year), font_size=SMALL_FONT_SIZE, color=ACCENT_CYAN)
        year_label.next_to(point, DOWN, buff=0.2)

        # Event label
        event_label = Text(event_name, font_size=SMALL_FONT_SIZE, color=WHITE)
        event_label.next_to(point, UP, buff=0.2)

        event_group = VGroup(point, year_label, event_label)
        event_objects.add(event_group)

        # Animations
        animations.append(FadeIn(event_group))

    timeline_group = VGroup(timeline, event_objects)

    # Create animation sequence
    timeline_anim = AnimationGroup(
        Create(timeline),
        AnimationGroup(*animations, lag_ratio=0.3),
        run_time=run_time
    )

    return timeline_group, timeline_anim


def word_tokenization_animation(sentence, tokens, run_time=1):
    """
    Animates word tokenization process.

    Args:
        sentence: Original sentence text
        tokens: List of tokens
        run_time: Animation duration

    Returns:
        Animation sequence
    """
    # Original sentence
    original = Text(sentence, font_size=BODY_FONT_SIZE, color=WHITE)

    # Tokenized version
    token_objects = []
    for token in tokens:
        token_box = Rectangle(
            width=len(token) * 0.15 + 0.3,
            height=0.5,
            stroke_color=ACCENT_CYAN,
            stroke_width=2,
            fill_opacity=0.1,
            fill_color=ACCENT_CYAN
        )
        token_text = Text(token, font_size=SMALL_FONT_SIZE, color=WHITE)
        token_text.move_to(token_box.get_center())
        token_obj = VGroup(token_box, token_text)
        token_objects.append(token_obj)

    tokenized = VGroup(*token_objects).arrange(RIGHT, buff=0.1)

    return original, tokenized, Transform(original, tokenized, run_time=run_time)
