"""
Part 2: History, Definition & RNNs
Slides 12-20: LLM history, definitions, and RNN architecture
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


class Slide12_LLMDefinition(LLMSlide):
    """Slide 12: Definition and role of an LLM"""

    def construct(self):
        title = self.add_title("Definition and role of an LLM")
        self.play(Write(title), run_time=0.5)

        # Three definition boxes
        definitions = [
            ("Large Language Model", "Language model trained on a very large database\n(e.g. Wikipedia), unlike SLM (Small Language Model)"),
            ("Generative AI model", "Consistent text generation"),
            ("Uses tools of NLP", "Transformers, attention mechanism,\nembeddings, etc.")
        ]

        def_boxes = VGroup()
        for def_title, def_text in definitions:
            title_text = Text(def_title, font_size=BODY_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
            desc_text = Text(def_text, font_size=SMALL_FONT_SIZE, color=WHITE, line_spacing=1.2)

            box_content = VGroup(title_text, desc_text).arrange(DOWN, buff=0.2)
            box = SurroundingRectangle(box_content, color=PRIMARY_BLUE, buff=0.3, stroke_width=3)

            def_boxes.add(VGroup(box, box_content))

        def_boxes.arrange(DOWN, buff=0.4).scale(0.8).shift(DOWN * 0.3)

        for def_box in def_boxes:
            self.play(FadeIn(def_box, shift=RIGHT), run_time=0.6)
            self.wait(0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide13_HistoricalTimeline(LLMSlide):
    """Slide 13: Historical Timeline of ML"""

    def construct(self):
        title = self.add_title("History of Machine Learning")
        self.play(Write(title), run_time=0.5)

        # Timeline events
        events = [
            (1960, "MLP"),
            (1989, "CNN"),
            (1995, "SVM"),
            (1995, "RNN"),
            (1997, "LSTM"),
            (2014, "GAN"),
            (2017, "Transformer"),
            (2018, "GPT-1")
        ]

        timeline_length = 10
        timeline = Line(LEFT * timeline_length/2, RIGHT * timeline_length/2, color=WHITE)
        timeline.shift(DOWN)

        self.play(Create(timeline), run_time=0.4)

        year_range = 2018 - 1960

        for year, event_name in events:
            progress = (year - 1960) / year_range
            x_pos = -timeline_length/2 + progress * timeline_length

            point = Dot(color=ACCENT_CYAN, radius=0.08).move_to([x_pos, -1, 0])
            year_label = Text(str(year), font_size=TINY_FONT_SIZE, color=ACCENT_CYAN)
            year_label.next_to(point, DOWN, buff=0.2)

            event_label = Text(event_name, font_size=SMALL_FONT_SIZE, color=WHITE, weight=BOLD)
            event_label.next_to(point, UP, buff=0.2)

            # Highlight Transformer and GPT-1
            if event_name in ["Transformer", "GPT-1"]:
                event_label.set_color(ACCENT_ORANGE)
                point.set_color(ACCENT_ORANGE).scale(1.5)

            event_group = VGroup(point, year_label, event_label)
            self.play(FadeIn(event_group), run_time=0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide14_RNNIntroduction(FormulaSlide):
    """Slide 14: RNN Introduction"""

    def construct(self):
        title = self.add_title("Recurrent Neural Network (RNN)")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "Designed to manage sequential data\nRetains a memory of previous states",
            font_size=BODY_FONT_SIZE,
            color=WHITE,
            line_spacing=1.3
        )
        definition.shift(UP * 1.5)

        self.play(Write(definition), run_time=0.7)

        # Formula
        formula = MathTex(
            r"h_t = f(W_h h_{t-1} + W_x x_t + b)",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN
        )
        formula.shift(UP * 0.2)

        self.wait(0.3)
        self.play(Write(formula), run_time=1)

        # Variable explanations
        variables = [
            (r"h_t", "hidden state at time t"),
            (r"x_t", "current input"),
            (r"W_h, W_x, b", "weights and bias"),
            (r"f", "activation function (tanh, ReLU)")
        ]

        var_objects = VGroup()
        for var, desc in variables:
            var_text = MathTex(f"{var}:", font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE)
            desc_text = Text(desc, font_size=SMALL_FONT_SIZE, color=WHITE)
            var_line = VGroup(var_text, desc_text).arrange(RIGHT, buff=0.3)
            var_objects.add(var_line)

        var_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        var_objects.next_to(formula, DOWN, buff=0.8)

        for var_line in var_objects:
            self.play(FadeIn(var_line), run_time=0.3)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide15_RNNSequential(LLMSlide):
    """Slide 15: RNN Sequential Processing"""

    def construct(self):
        title = Text(
            "RNNs store the past by reinjecting the previous state",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN
        )
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.7)

        # Example sentence
        sentence = "I've lived in New York for 10 years, so I speak good ___"
        sentence_text = Text(sentence, font_size=BODY_FONT_SIZE, color=WHITE)
        sentence_text.shift(UP * 1.5)

        self.play(Write(sentence_text), run_time=0.8)

        # RNN visualization
        words = sentence.split()[:7]  # First 7 words

        rnn_cells = VGroup()
        arrows = VGroup()

        for i, word in enumerate(words):
            # Cell
            cell = Circle(radius=0.3, color=ACCENT_CYAN, stroke_width=3)
            cell.shift(LEFT * 4 + RIGHT * i * 1.2 + DOWN)

            # Word label
            word_label = Text(word, font_size=TINY_FONT_SIZE, color=WHITE)
            word_label.next_to(cell, DOWN, buff=0.1)

            cell_group = VGroup(cell, word_label)
            rnn_cells.add(cell_group)

            # Recurrent arrow
            if i > 0:
                arrow = Arrow(
                    rnn_cells[i-1][0].get_right(),
                    cell.get_left(),
                    color=ACCENT_ORANGE,
                    buff=0.1,
                    stroke_width=3
                )
                arrows.add(arrow)

        # Animate
        self.wait(0.3)
        for i, cell_group in enumerate(rnn_cells):
            self.play(FadeIn(cell_group), run_time=0.2)
            if i > 0:
                self.play(GrowArrow(arrows[i-1]), run_time=0.15)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide16_TimelineContinued(LLMSlide):
    """Slide 16: Timeline Continued (focus on Transformer era)"""

    def construct(self):
        title = self.add_title("The Transformer Revolution")
        self.play(Write(title), run_time=0.5)

        # Key innovations text
        innovation_text = Text(
            "Revolutionizing Natural Language Processing",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_ORANGE,
            weight=BOLD
        )
        innovation_text.shift(UP * 1.5)

        self.play(Write(innovation_text), run_time=0.7)

        # Timeline 2017-2023
        timeline = Line(LEFT * 5, RIGHT * 5, color=WHITE).shift(DOWN * 0.5)
        self.play(Create(timeline), run_time=0.4)

        events = [
            (2017, "Transformer", ACCENT_ORANGE),
            (2018, "BERT", ACCENT_GREEN),
            (2018, "GPT-1", ACCENT_CYAN),
            (2019, "GPT-2", ACCENT_CYAN),
            (2020, "GPT-3", ACCENT_CYAN),
            (2022, "ChatGPT", ACCENT_YELLOW),
            (2023, "GPT-4", ACCENT_ORANGE)
        ]

        for year, name, color in events:
            x = -5 + ((year - 2017) / 6) * 10
            point = Dot(color=color, radius=0.12).move_to([x, -0.5, 0])
            year_text = Text(str(year), font_size=TINY_FONT_SIZE, color=color)
            year_text.next_to(point, DOWN, buff=0.2)
            name_text = Text(name, font_size=SMALL_FONT_SIZE, color=color, weight=BOLD)
            name_text.next_to(point, UP, buff=0.2)

            self.play(FadeIn(VGroup(point, year_text, name_text)), run_time=0.25)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide17_UseCases(LLMSlide):
    """Slide 17: LLM Use Cases"""

    def construct(self):
        title = self.add_title("Use cases")
        self.play(Write(title), run_time=0.5)

        # Header
        header = Text(
            "A wide range of applications are available:",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        header.shift(UP * 2)
        self.play(Write(header), run_time=0.5)

        # Use cases
        use_cases = [
            "🤖 Chatbots or virtual assistants",
            "🌐 Automated translation",
            "📊 Sentiment analysis",
            "🎤 Voice recognition",
            "📑 Classifications..."
        ]

        case_objects = VGroup()
        for case in use_cases:
            text = Text(case, font_size=BODY_FONT_SIZE, color=WHITE)
            case_objects.add(text)

        case_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        case_objects.shift(DOWN * 0.2)

        for case in case_objects:
            self.play(FadeIn(case, shift=RIGHT), run_time=0.3)
            self.wait(0.1)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide18_ToolsArchitectureTitle(TitleSlide):
    """Slide 18: Tools and Architecture Section Title"""

    def construct(self):
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color=DARK_BLUE,
            stroke_width=0
        )
        self.add(bg)

        title = Text(
            "Tools and Architecture",
            font_size=TITLE_FONT_SIZE,
            color=ACCENT_CYAN,
            weight=BOLD
        )

        self.play(FadeIn(title, scale=1.2), run_time=1)
        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide19_NLPSteps(LLMSlide):
    """Slide 19: NLP Steps Overview"""

    def construct(self):
        title = self.add_title("NLP Processing Steps")
        self.play(Write(title), run_time=0.5)

        # Two main steps
        steps = [
            ("1. Data Resources", [
                "Open source datasets",
                "Corporate data (doc, pdf...)",
                "Scraped from the Internet",
                "Social network APIs"
            ]),
            ("2. Word Representations", [
                "Reducing complexity: Stemming, Lemmatization",
                "Transform to vectors: Bag of Words, TF-IDF",
                "Word Embedding, Transformers"
            ])
        ]

        step_objects = VGroup()
        for step_title, step_items in steps:
            title_text = Text(step_title, font_size=BODY_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)

            items = VGroup()
            for item in step_items:
                bullet = Text("•", font_size=SMALL_FONT_SIZE, color=WHITE)
                item_text = Text(item, font_size=SMALL_FONT_SIZE, color=WHITE)
                item_line = VGroup(bullet, item_text).arrange(RIGHT, buff=0.2)
                items.add(item_line)

            items.arrange(DOWN, aligned_edge=LEFT, buff=0.15)

            step_content = VGroup(title_text, items).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            step_objects.add(step_content)

        step_objects.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        step_objects.scale(0.8).shift(DOWN * 0.2)

        for step in step_objects:
            self.play(FadeIn(step, shift=UP), run_time=0.6)
            self.wait(0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide20_Word2VecIntroduction(LLMSlide):
    """Slide 20: Word2Vec Introduction"""

    def construct(self):
        title = self.add_title("Converting text to vectors: Word2Vec")
        self.play(Write(title), run_time=0.5)

        subtitle = Text(
            "Introduced by Google in 2013",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        subtitle.next_to(title, DOWN, buff=0.3)
        self.play(FadeIn(subtitle), run_time=0.4)

        # Two approaches
        approaches = [
            ("CBOW", "Continuous Bag of Words", "Predicts target word\nfrom context"),
            ("Skip-gram", "Skip-gram", "Predicts context\nfrom target word")
        ]

        approach_boxes = VGroup()
        for name, full_name, desc in approaches:
            name_text = Text(name, font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
            full_text = Text(full_name, font_size=SMALL_FONT_SIZE, color=LIGHT_GRAY)
            desc_text = Text(desc, font_size=SMALL_FONT_SIZE, color=WHITE, line_spacing=1.2)

            content = VGroup(name_text, full_text, desc_text).arrange(DOWN, buff=0.2)
            box = SurroundingRectangle(content, color=PRIMARY_BLUE, buff=0.3, stroke_width=3)

            approach_boxes.add(VGroup(box, content))

        approach_boxes.arrange(RIGHT, buff=1).shift(DOWN * 0.5)

        for box in approach_boxes:
            self.play(FadeIn(box, shift=UP), run_time=0.6)
            self.wait(0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()
