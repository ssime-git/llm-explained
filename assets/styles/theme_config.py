"""
Theme configuration for LLM Explained presentation.
Defines colors, fonts, and styling constants used throughout the slides.
"""

from manim import *

# ============================================================================
# COLOR PALETTE
# ============================================================================

# Primary colors (main content)
PRIMARY_BLUE = "#1F77B4"       # Formulas, main text
DARK_BLUE = "#1a1a2e"          # Dark background
ACCENT_CYAN = "#17BECF"        # Highlights, key concepts
ACCENT_TURQUOISE = "#16c7c7"   # Alternative highlight

# Secondary colors (emphasis)
ACCENT_PURPLE = "#9467BD"      # Alternative highlighting
ACCENT_ORANGE = "#FF7F0E"      # Important numbers
ACCENT_GREEN = "#2CA02C"       # Correct/positive
ACCENT_RED = "#D62728"         # Incorrect/negative
ACCENT_YELLOW = "#FFD700"      # Warnings, highlights

# Neutral colors
LIGHT_GRAY = "#E0E0E0"
MEDIUM_GRAY = "#808080"
DARK_GRAY = "#404040"
BG_GRAY = "#F5F5F5"

# ============================================================================
# FONT SETTINGS
# ============================================================================

TITLE_FONT_SIZE = 60
SUBTITLE_FONT_SIZE = 40
HEADING_FONT_SIZE = 36
BODY_FONT_SIZE = 28
SMALL_FONT_SIZE = 24
TINY_FONT_SIZE = 20

# ============================================================================
# LAYOUT CONSTANTS
# ============================================================================

TITLE_Y_POS = 3.0              # Y position for slide titles
CONTENT_Y_START = 2.0          # Y position where content starts
CONTENT_SPACING = 0.5          # Vertical spacing between content elements
SIDE_MARGIN = 0.5              # Horizontal margin from edges

# ============================================================================
# ANIMATION TIMING
# ============================================================================

FADE_IN_TIME = 0.5
FADE_OUT_TIME = 0.5
TRANSITION_TIME = 0.3
PAUSE_TIME = 1.0
SLIDE_WAIT_TIME = 2.0

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def get_title_style():
    """Returns Text configuration for slide titles."""
    return {
        "font_size": TITLE_FONT_SIZE,
        "color": ACCENT_CYAN,
        "weight": BOLD
    }

def get_subtitle_style():
    """Returns Text configuration for subtitles."""
    return {
        "font_size": SUBTITLE_FONT_SIZE,
        "color": WHITE
    }

def get_heading_style():
    """Returns Text configuration for headings."""
    return {
        "font_size": HEADING_FONT_SIZE,
        "color": PRIMARY_BLUE,
        "weight": BOLD
    }

def get_body_style():
    """Returns Text configuration for body text."""
    return {
        "font_size": BODY_FONT_SIZE,
        "color": WHITE
    }

def get_code_style():
    """Returns Text configuration for code blocks."""
    return {
        "font": "Monospace",
        "font_size": SMALL_FONT_SIZE,
        "color": ACCENT_GREEN
    }

def create_gradient_background(top_color=DARK_BLUE, bottom_color=ACCENT_CYAN, opacity=0.3):
    """
    Creates a gradient background rectangle.

    Args:
        top_color: Color at the top
        bottom_color: Color at the bottom
        opacity: Opacity of the gradient

    Returns:
        Rectangle with gradient fill
    """
    bg = Rectangle(
        width=config.frame_width,
        height=config.frame_height,
        fill_opacity=opacity,
        stroke_width=0
    )
    bg.set_sheen_direction(DOWN)
    bg.set_color([top_color, bottom_color])
    return bg

def create_box(text, color=PRIMARY_BLUE, width=5, height=1, font_size=BODY_FONT_SIZE):
    """
    Creates a styled box with text inside.

    Args:
        text: Text content
        color: Border and text color
        width: Box width
        height: Box height
        font_size: Text font size

    Returns:
        VGroup containing box and text
    """
    box = Rectangle(
        width=width,
        height=height,
        stroke_color=color,
        stroke_width=3,
        fill_opacity=0.1,
        fill_color=color
    )

    text_obj = Text(text, font_size=font_size, color=color)
    text_obj.move_to(box.get_center())

    # Scale text if it's too wide for the box
    if text_obj.width > box.width * 0.9:
        text_obj.scale((box.width * 0.9) / text_obj.width)

    return VGroup(box, text_obj)

def create_numbered_box(number, text, color=PRIMARY_BLUE, box_size=0.5, font_size=BODY_FONT_SIZE):
    """
    Creates a box with a number and associated text.

    Args:
        number: Number to display
        text: Text content
        color: Color theme
        box_size: Size of the number box
        font_size: Text font size

    Returns:
        VGroup containing number box and text
    """
    # Number box
    num_box = Square(side_length=box_size, fill_opacity=1, fill_color=color, stroke_width=0)
    num_text = Text(str(number), font_size=font_size * 0.7, color=WHITE, weight=BOLD)
    num_text.move_to(num_box.get_center())

    # Text
    content_text = Text(text, font_size=font_size, color=WHITE)

    # Arrange
    group = VGroup(num_box, num_text, content_text).arrange(RIGHT, buff=0.3)

    return group

def create_arrow_with_label(start, end, label_text, color=WHITE, label_pos="above"):
    """
    Creates an arrow with a label.

    Args:
        start: Starting point
        end: Ending point
        label_text: Text for the label
        color: Arrow color
        label_pos: Position of label ("above", "below", "left", "right")

    Returns:
        VGroup containing arrow and label
    """
    arrow = Arrow(start, end, color=color, buff=0)
    label = Text(label_text, font_size=SMALL_FONT_SIZE, color=color)

    # Position label
    if label_pos == "above":
        label.next_to(arrow, UP, buff=0.1)
    elif label_pos == "below":
        label.next_to(arrow, DOWN, buff=0.1)
    elif label_pos == "left":
        label.next_to(arrow, LEFT, buff=0.1)
    elif label_pos == "right":
        label.next_to(arrow, RIGHT, buff=0.1)

    return VGroup(arrow, label)

def create_timeline_point(year, event, color=ACCENT_CYAN):
    """
    Creates a timeline point with year and event.

    Args:
        year: Year label
        event: Event description
        color: Point color

    Returns:
        VGroup containing point and labels
    """
    point = Dot(color=color, radius=0.1)
    year_text = Text(str(year), font_size=SMALL_FONT_SIZE, color=color)
    event_text = Text(event, font_size=SMALL_FONT_SIZE, color=WHITE)

    year_text.next_to(point, DOWN, buff=0.2)
    event_text.next_to(point, UP, buff=0.2)

    return VGroup(point, year_text, event_text)

def create_probability_bar(word, probability, max_width=3, color=PRIMARY_BLUE):
    """
    Creates a probability bar visualization.

    Args:
        word: Word label
        probability: Probability value (0-1)
        max_width: Maximum width of the bar
        color: Bar color

    Returns:
        VGroup containing label and bar
    """
    # Word label
    label = Text(word, font_size=BODY_FONT_SIZE, color=WHITE)

    # Probability bar
    bar_width = max_width * probability
    bar = Rectangle(
        width=bar_width,
        height=0.3,
        fill_opacity=0.8,
        fill_color=color,
        stroke_width=0
    )

    # Probability text
    prob_text = Text(f"{probability:.2f}", font_size=SMALL_FONT_SIZE, color=WHITE)

    # Arrange
    group = VGroup(label, bar, prob_text).arrange(RIGHT, buff=0.2, aligned_edge=LEFT)

    return group

# ============================================================================
# SPECIAL EFFECTS
# ============================================================================

def create_glow_effect(mobject, color=ACCENT_YELLOW, intensity=2):
    """
    Adds a glow effect to a mobject.

    Args:
        mobject: The mobject to add glow to
        color: Glow color
        intensity: Glow intensity

    Returns:
        The mobject with glow added
    """
    mobject.set_stroke(color=color, width=intensity, opacity=0.5, background=True)
    return mobject
