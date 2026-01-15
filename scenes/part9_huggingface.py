"""
Part 9: Hugging Face & Conclusion
Slides 61-65: Demo, conclusion, next steps
"""

from manim import *
from manim_slides import Slide
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.custom_scenes import *
from utils.animations import *
from assets.styles.theme_config import *


class Slide61_DemoPlaceholder(LLMSlide):
    """Slide 61: Demo Placeholder"""

    def construct(self):
        title = self.add_title("DEMO")
        self.play(Write(title), run_time=0.5)

        # Demo topics
        topics = [
            "📞 Calling the ChatGPT API",
            "🤗 Using Hugging Face models",
            "🔧 Parameter tuning examples"
        ]

        topic_objects = self.create_bullet_list(topics, font_size=HEADING_FONT_SIZE)
        topic_objects.shift(UP * 0.5)

        for topic in topic_objects:
            self.play(FadeIn(topic, shift=RIGHT), run_time=0.5)
            self.wait(0.2)

        # Placeholder
        placeholder = Text(
            "Live demonstration will be shown here",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_YELLOW
        )
        placeholder.shift(DOWN * 1.5)

        self.wait(0.3)
        self.play(FadeIn(placeholder), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide62_ConclusionTitle(TitleSlide):
    """Slide 62: Conclusion Title"""

    def construct(self):
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color=DARK_BLUE,
            stroke_width=0
        )
        self.add(bg)

        title = Text("CONCLUSION", font_size=TITLE_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        self.play(FadeIn(title, scale=1.2), run_time=1)
        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide63_QuestionsAndFeedback(LLMSlide):
    """Slide 63: Questions & Feedback"""

    def construct(self):
        title = self.add_title("CONCLUSION")
        self.play(Write(title), run_time=0.5)

        # Questions box
        questions_icon = Text("?", font_size=80, color=ACCENT_CYAN, weight=BOLD)
        questions_icon.shift(LEFT * 4 + UP * 0.5)

        questions_text = Text(
            "Questions &\nFeedback",
            font_size=HEADING_FONT_SIZE,
            color=WHITE,
            weight=BOLD,
            line_spacing=1.2
        )
        questions_text.next_to(questions_icon, DOWN, buff=0.3)

        # What's next box
        next_icon = Text("→", font_size=80, color=ACCENT_ORANGE, weight=BOLD)
        next_icon.shift(RIGHT * 4 + UP * 0.5)

        next_text = Text(
            "What's Next?",
            font_size=HEADING_FONT_SIZE,
            color=WHITE,
            weight=BOLD
        )
        next_text.next_to(next_icon, DOWN, buff=0.3)

        next_items = [
            "The next dates",
            "Training objectives"
        ]

        next_list = self.create_bullet_list(next_items, font_size=BODY_FONT_SIZE)
        next_list.next_to(next_text, DOWN, buff=0.4)

        self.wait(0.3)
        self.play(FadeIn(VGroup(questions_icon, questions_text), shift=RIGHT), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(VGroup(next_icon, next_text, next_list), shift=LEFT), run_time=0.7)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide64_NextDates(LLMSlide):
    """Slide 64: Next Dates"""

    def construct(self):
        title = self.add_title("NEXT DATES")
        self.play(Write(title), run_time=0.5)

        # Calendar icon (simple)
        calendar = VGroup(
            Rectangle(width=3, height=2.5, color=ACCENT_CYAN, stroke_width=4),
            Line(LEFT * 1.5, LEFT * 1.5 + UP * 0.3, color=ACCENT_CYAN, stroke_width=4),
            Line(RIGHT * 1.5, RIGHT * 1.5 + UP * 0.3, color=ACCENT_CYAN, stroke_width=4),
            Text("📅", font_size=80)
        )
        calendar.shift(UP * 0.5)

        # Next session info
        next_session = Text(
            "Next Session:\nAdvanced LLM Topics",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN,
            weight=BOLD,
            line_spacing=1.3
        )
        next_session.shift(DOWN * 1.5)

        self.play(FadeIn(calendar, scale=1.2), run_time=0.8)
        self.wait(0.3)
        self.play(FadeIn(next_session), run_time=0.6)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide65_ThankYou(TitleSlide):
    """Slide 65: Final Slide / Thank You"""

    def construct(self):
        # Gradient background
        self.add_gradient_background(DARK_BLUE, ACCENT_CYAN, opacity=0.3)

        # Thank you message
        thank_you = Text(
            "Thank You!",
            font_size=TITLE_FONT_SIZE,
            color=ACCENT_CYAN,
            weight=BOLD
        )
        thank_you.shift(UP * 1)

        # Subtitle
        subtitle = Text(
            "Introduction to Large Language Models",
            font_size=HEADING_FONT_SIZE,
            color=WHITE
        )
        subtitle.next_to(thank_you, DOWN, buff=0.5)

        # Footer
        footer = Text(
            "Interactive Presentation powered by Manim Slides",
            font_size=BODY_FONT_SIZE,
            color=LIGHT_GRAY
        )
        footer.to_edge(DOWN, buff=1)

        # Star decorations
        stars = VGroup(*[
            Text("✨", font_size=60).shift(UP * 2.5 + LEFT * (3 - i * 1.5))
            for i in range(5)
        ])

        self.play(FadeIn(thank_you, scale=1.3), run_time=1)
        self.wait(0.3)
        self.play(FadeIn(subtitle), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(stars), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(footer), run_time=0.5)

        self.wait(PAUSE_TIME * 2)
        self.next_slide()
