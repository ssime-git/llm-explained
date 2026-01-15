"""
Part 1: Foundations & Prompt Engineering
Slides 1-11: Introduction, communication rules, prompt engineering basics
"""

from manim import *
from manim_slides import Slide
import sys
import os

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.custom_scenes import *
from utils.animations import *
from assets.styles.theme_config import *


class Slide1_TitleIntroduction(TitleSlide):
    """
    Slide 1: Title Slide
    Main introduction to the LLM presentation
    """

    def construct(self):
        # Gradient background
        self.add_gradient_background(DARK_BLUE, ACCENT_CYAN, opacity=0.3)

        # Decorative curved shape
        curve = Arc(radius=2, start_angle=0, angle=TAU, color=ACCENT_CYAN, stroke_width=5)
        curve.shift(UP * 0.5)

        # Main title
        title = Text("Introduction to LLMs", font_size=TITLE_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        title.move_to(ORIGIN)

        # Subtitle
        subtitle = Text("Large Language Models Explained", font_size=SUBTITLE_FONT_SIZE, color=WHITE)
        subtitle.next_to(title, DOWN, buff=0.5)

        # Bottom text
        bottom_text = Text("Interactive Presentation", font_size=BODY_FONT_SIZE, color=LIGHT_GRAY)
        bottom_text.to_edge(DOWN, buff=1)

        # Animations
        self.play(Create(curve), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(title, shift=DOWN), run_time=0.8)
        self.play(FadeIn(subtitle), run_time=0.6)
        self.play(FadeIn(bottom_text), run_time=0.5)
        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide2_CommunicationRules(LLMSlide):
    """
    Slide 2: Communication Rules Reminder
    Three key rules for the presentation
    """

    def construct(self):
        # Title
        title = self.add_title("Quick reminder of the rules")
        self.play(Write(title), run_time=0.5)

        # Three columns with icons and text
        columns = []

        # Column 1: Lightning bolt + validate presence
        lightning = VGroup(
            Line(UP * 0.3 + LEFT * 0.1, DOWN * 0.1, color=ACCENT_YELLOW, stroke_width=6),
            Line(DOWN * 0.1, DOWN * 0.3 + RIGHT * 0.1, color=ACCENT_YELLOW, stroke_width=6)
        )
        text1 = Text("VALIDATE YOUR\nPRESENCE", font_size=SMALL_FONT_SIZE, color=WHITE).scale(0.8)
        text1.next_to(lightning, DOWN, buff=0.3)
        col1 = VGroup(lightning, text1)

        # Column 2: Camera + activate camera
        camera = VGroup(
            Rectangle(width=0.6, height=0.4, color=ACCENT_CYAN, stroke_width=4),
            Circle(radius=0.15, color=ACCENT_CYAN, stroke_width=4).shift(RIGHT * 0.1)
        )
        text2 = Text("ACTIVATE YOUR\nCAMERA", font_size=SMALL_FONT_SIZE, color=WHITE).scale(0.8)
        text2.next_to(camera, DOWN, buff=0.3)
        col2 = VGroup(camera, text2)

        # Column 3: People + respect communication
        people = VGroup(
            Circle(radius=0.15, color=ACCENT_GREEN, stroke_width=4).shift(LEFT * 0.2 + UP * 0.1),
            Circle(radius=0.15, color=ACCENT_GREEN, stroke_width=4).shift(RIGHT * 0.2 + UP * 0.1),
            Circle(radius=0.15, color=ACCENT_GREEN, stroke_width=4).shift(DOWN * 0.2)
        )
        text3 = Text("RESPECT ALL\nCOMMUNICATION RULES", font_size=SMALL_FONT_SIZE, color=WHITE).scale(0.8)
        text3.next_to(people, DOWN, buff=0.3)
        col3 = VGroup(people, text3)

        # Arrange columns
        columns_group = VGroup(col1, col2, col3).arrange(RIGHT, buff=1.5)
        columns_group.shift(DOWN * 0.5)

        # Animate columns appearing
        self.wait(0.3)
        self.play(FadeIn(col1, shift=UP), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(col2, shift=UP), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(col3, shift=UP), run_time=0.6)
        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide3_CourseSummary(LLMSlide):
    """
    Slide 3: Course Summary
    5 main topics of the presentation
    """

    def construct(self):
        # Title
        title = self.add_title("SUMMARY")
        self.play(Write(title), run_time=0.5)

        # 5 numbered items
        items = [
            "Concepts of prompt engineering",
            "History, definition and role of LLMs",
            "LLM tools: token, embedding, attention, text generation",
            "The difficulties of an LLM",
            "LLM API exploration and Hugging Face"
        ]

        numbered_items = VGroup()
        for i, item_text in enumerate(items, 1):
            item_obj = create_numbered_box(i, item_text, color=ACCENT_CYAN, font_size=BODY_FONT_SIZE)
            numbered_items.add(item_obj)

        numbered_items.arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        numbered_items.move_to(ORIGIN).shift(DOWN * 0.3)

        # Animate items appearing
        self.wait(0.3)
        for item in numbered_items:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide4_PromptEngineering(LLMSlide):
    """
    Slide 4: Prompt Engineering Introduction
    Definition and key concepts
    """

    def construct(self):
        # Title
        title = self.add_title("Prompt Engineering")
        self.play(Write(title), run_time=0.5)

        # Center definition box
        definition = Text(
            "Prompt: instruction or input text\ngiven to an LLM",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN,
            line_spacing=1.2
        )
        def_box = SurroundingRectangle(definition, color=ACCENT_CYAN, buff=0.3, stroke_width=3)
        def_group = VGroup(def_box, definition)
        def_group.move_to(ORIGIN)

        # Left box: Increase performance
        left_text = Text("Increase\nperformance", font_size=BODY_FONT_SIZE, color=WHITE)
        left_box = SurroundingRectangle(left_text, color=ACCENT_GREEN, buff=0.3)
        left_group = VGroup(left_box, left_text)
        left_group.move_to(LEFT * 4 + UP * 0.5)

        # Right box: Provoke specific response
        right_text = Text("Provoke a specific\ntype of response", font_size=BODY_FONT_SIZE, color=WHITE)
        right_box = SurroundingRectangle(right_text, color=ACCENT_ORANGE, buff=0.3)
        right_group = VGroup(right_box, right_text)
        right_group.move_to(RIGHT * 4 + UP * 0.5)

        # Bottom text
        bottom_text = Text(
            "The better the prompt, the more accurate\nand contextually relevant the LLM output",
            font_size=SMALL_FONT_SIZE,
            color=LIGHT_GRAY,
            line_spacing=1.2
        )
        bottom_text.to_edge(DOWN, buff=0.8)

        # Animations
        self.wait(0.2)
        self.play(FadeIn(left_group, shift=RIGHT), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(right_group, shift=LEFT), run_time=0.5)
        self.wait(0.3)
        self.play(Create(def_box), Write(definition), run_time=0.8)
        self.wait(0.4)
        self.play(FadeIn(bottom_text), run_time=0.5)
        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide5_PromptComponents(LLMSlide):
    """
    Slide 5: Essential Components of Prompts
    6 key components
    """

    def construct(self):
        # Title
        title = self.add_title("Essential components of a prompt")
        self.play(Write(title), run_time=0.5)

        # 6 components
        components = [
            ("TASK", "What do you want ChatGPT to do?"),
            ("CONTEXT", "What contextual or situational information should ChatGPT consider?"),
            ("EXAMPLE", "Can you give an example to illustrate your expectations?"),
            ("PERSONALITY", "What role or voice should ChatGPT adopt?"),
            ("FORMAT", "How should the response be structured?"),
            ("TONE", "What style should the answer reflect?")
        ]

        component_objects = VGroup()
        for i, (comp_name, comp_desc) in enumerate(components, 1):
            # Component number and name
            num_circle = Circle(radius=0.25, fill_opacity=1, fill_color=ACCENT_CYAN, stroke_width=0)
            num_text = Text(str(i), font_size=SMALL_FONT_SIZE, color=WHITE, weight=BOLD)
            num_text.move_to(num_circle.get_center())

            name_text = Text(comp_name, font_size=BODY_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)

            desc_text = Text(comp_desc, font_size=SMALL_FONT_SIZE, color=LIGHT_GRAY)

            # Arrange
            comp_header = VGroup(num_circle, num_text, name_text).arrange(RIGHT, buff=0.2)
            comp_full = VGroup(comp_header, desc_text).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

            component_objects.add(comp_full)

        component_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        component_objects.scale(0.7).shift(DOWN * 0.2)

        # Animate components
        self.wait(0.2)
        for comp in component_objects:
            self.play(FadeIn(comp, shift=RIGHT), run_time=0.3)
            self.wait(0.05)

        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide6_ComponentsExample(LLMSlide):
    """
    Slide 6: Prompt Components Example
    Example showing each component in action
    """

    def construct(self):
        # Title
        title = self.add_title("Prompt Components: Example")
        self.play(Write(title), run_time=0.5)

        # Example for each component
        examples = [
            ("1. TASK", "Write a short article", ACCENT_CYAN),
            ("2. CONTEXT", "About the benefits of green tea", ACCENT_GREEN),
            ("3. EXAMPLE", "Green tea, originally from China,\nis praised for its health benefits...", ACCENT_ORANGE),
            ("4. PERSONALITY", "A nutritionist", ACCENT_PURPLE),
            ("5. FORMAT", "Introduction, 3 benefits, conclusion", PRIMARY_BLUE),
            ("6. TONE", "Informative but captivating", ACCENT_YELLOW)
        ]

        example_objects = VGroup()
        for label, example, color in examples:
            label_text = Text(label, font_size=SMALL_FONT_SIZE, color=color, weight=BOLD)
            example_text = Text(example, font_size=SMALL_FONT_SIZE, color=WHITE)

            example_box = VGroup(label_text, example_text).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
            example_objects.add(example_box)

        example_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        example_objects.scale(0.8).shift(DOWN * 0.2)

        # Animate examples
        self.wait(0.2)
        for example in example_objects:
            self.play(FadeIn(example), run_time=0.3)
            self.wait(0.05)

        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide7_PromptBestPractices(LLMSlide):
    """
    Slide 7: Prompt Best Practices
    4 key properties of good prompts
    """

    def construct(self):
        # Title
        title = self.add_title("Prompt best practices")
        self.play(Write(title), run_time=0.5)

        # Left box: Increase performance
        left_box = Rectangle(
            width=3,
            height=1.5,
            fill_opacity=0.2,
            fill_color=ACCENT_TURQUOISE,
            stroke_color=ACCENT_TURQUOISE,
            stroke_width=3
        )
        left_text = Text("Increase\nperformance", font_size=BODY_FONT_SIZE, color=WHITE)
        left_text.move_to(left_box.get_center())
        left_group = VGroup(left_box, left_text)
        left_group.to_edge(LEFT, buff=1).shift(UP * 1)

        # Center: "A prompt must be:"
        center_text = Text("A prompt must be:", font_size=HEADING_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        center_text.shift(UP * 1.5)

        # Four properties
        properties = ["Short", "Clear", "Precise", "Directive"]
        prop_objects = VGroup()
        for prop in properties:
            prop_text = Text(prop, font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
            prop_objects.add(prop_text)

        prop_objects.arrange(DOWN, buff=0.3)
        prop_objects.next_to(center_text, DOWN, buff=0.5)

        # Right: Example code box
        example_code = """Act like a productivity coach.
Give me the 7 best ways to
increase productivity in the
workplace in bullet point form."""

        code_box = Rectangle(
            width=4.5,
            height=2.5,
            fill_opacity=0.9,
            fill_color=DARK_GRAY,
            stroke_color=ACCENT_GREEN,
            stroke_width=2
        )
        code_text = Text(example_code, font_size=SMALL_FONT_SIZE, color=WHITE, line_spacing=1.3, font="Monospace")
        code_text.move_to(code_box.get_center())
        code_group = VGroup(code_box, code_text)
        code_group.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.5)

        # Animations
        self.wait(0.2)
        self.play(FadeIn(left_group, shift=RIGHT), run_time=0.5)
        self.wait(0.2)
        self.play(Write(center_text), run_time=0.5)
        self.wait(0.2)

        for prop in prop_objects:
            self.play(FadeIn(prop, shift=UP), run_time=0.3)
            self.wait(0.05)

        self.wait(0.3)
        self.play(FadeIn(code_group), run_time=0.6)

        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide8_ContentCreationPrompts(LLMSlide):
    """
    Slide 8: Prompts for Content Creation
    Example prompts for various content types
    """

    def construct(self):
        # Title and subtitle
        title = self.add_title("Prompts for content creation")
        self.play(Write(title), run_time=0.5)

        subtitle = Text("Examples of prompts for email content creation", font_size=BODY_FONT_SIZE, color=LIGHT_GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Three example prompts
        examples = [
            "Write a cover letter for a\nmajor digital company.",
            "Write a short follow-up e-mail\nto check if a potential customer\nmissed the previous e-mail.",
            "Write a Monday motivational\npost for LinkedIn. Target\naudience: sales and marketing\nmanagers."
        ]

        example_boxes = VGroup()
        for i, example_text in enumerate(examples):
            box = Rectangle(
                width=3.5,
                height=2,
                stroke_color=ACCENT_CYAN,
                stroke_width=2,
                fill_opacity=0.1,
                fill_color=ACCENT_CYAN
            )
            text = Text(example_text, font_size=SMALL_FONT_SIZE, color=WHITE, line_spacing=1.2)
            text.move_to(box.get_center())

            if text.height > box.height * 0.9:
                text.scale((box.height * 0.9) / text.height)

            example_boxes.add(VGroup(box, text))

        example_boxes.arrange(RIGHT, buff=0.4)
        example_boxes.shift(DOWN * 0.5)

        # Animate examples
        self.wait(0.3)
        for example in example_boxes:
            self.play(FadeIn(example, shift=UP), run_time=0.4)
            self.wait(0.1)

        # Bottom question
        arrow = Arrow(UP, DOWN, color=ACCENT_ORANGE).scale(0.5)
        question = Text("How can we improve them?", font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE)
        question_group = VGroup(arrow, question).arrange(RIGHT, buff=0.2)
        question_group.to_edge(DOWN, buff=0.5)

        self.wait(0.3)
        self.play(FadeIn(question_group), run_time=0.5)

        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide9_ChatGPTInternetAccess(LLMSlide):
    """
    Slide 9: ChatGPT Internet Access
    Examples using internet access
    """

    def construct(self):
        # Title
        title = Text("ChatGPT internet access", font_size=TITLE_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        # Subtitle
        subtitle = Text(
            "→ ChatGPT now has Internet access!",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_GREEN
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Example prompts in a 2x3 grid
        prompts = [
            "Are there any upcoming\nevents in my area?",
            "Write a summary of\ntoday's news.",
            "Find the 3 best movies\nat the cinema.",
            "Give me the latest\nin Data Science.",
            "Sum up this article:\nURL_OF_THE_PAGE",
            "Check the accuracy of:\nINFORMATIONS_TO_CHECK"
        ]

        prompt_objects = VGroup()
        for prompt_text in prompts:
            box = Rectangle(
                width=3.5,
                height=1.2,
                stroke_color=PRIMARY_BLUE,
                stroke_width=2,
                fill_opacity=0.15,
                fill_color=PRIMARY_BLUE
            )
            text = Text(prompt_text, font_size=TINY_FONT_SIZE, color=WHITE, line_spacing=1.1)
            text.move_to(box.get_center())

            if text.width > box.width * 0.9:
                text.scale((box.width * 0.9) / text.width)

            prompt_objects.add(VGroup(box, text))

        # Arrange in 2x3 grid
        row1 = VGroup(*prompt_objects[:3]).arrange(RIGHT, buff=0.3)
        row2 = VGroup(*prompt_objects[3:]).arrange(RIGHT, buff=0.3)
        grid = VGroup(row1, row2).arrange(DOWN, buff=0.3)
        grid.shift(DOWN * 0.3)

        # Animate prompts appearing
        self.wait(0.3)
        for prompt in prompt_objects:
            self.play(FadeIn(prompt), run_time=0.2)
            self.wait(0.05)

        self.wait(PAUSE_TIME)

        self.next_slide()


class Slide10_PartTransition(TitleSlide):
    """
    Slide 10: Part Transition
    Transition to Part 2
    """

    def construct(self):
        # Background color transition
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color=DARK_BLUE,
            stroke_width=0
        )
        self.add(bg)

        # Transition title
        transition_text = Text(
            "History, definition and\nrole of LLMs",
            font_size=TITLE_FONT_SIZE,
            color=ACCENT_CYAN,
            weight=BOLD,
            line_spacing=1.3
        )
        transition_text.move_to(ORIGIN)

        self.play(FadeIn(transition_text, scale=1.2), run_time=1)
        self.wait(PAUSE_TIME)

        self.next_slide()
