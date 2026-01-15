"""
Part 7: LLM Challenges & Solutions
Slides 44-55: Challenges, quantization, costs, RLHF
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


class Slide44_ChallengesTitle(TitleSlide):
    """Slide 44: The Challenges Title"""

    def construct(self):
        bg = Rectangle(
            width=config.frame_width,
            height=config.frame_height,
            fill_opacity=1,
            fill_color=DARK_BLUE,
            stroke_width=0
        )
        self.add(bg)

        title = Text("The Challenges of an LLM", font_size=TITLE_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        self.play(FadeIn(title, scale=1.2), run_time=1)
        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide45_ChallengesOverview(LLMSlide):
    """Slide 45: Challenges Overview"""

    def construct(self):
        title = self.add_title("LLM Challenges")
        self.play(Write(title), run_time=0.5)

        challenges = [
            ("🗣️", "Very long conversations"),
            ("⚠️", "Hallucinations"),
            ("🔒", "Prompt injection"),
            ("©️", "Copyright issues"),
            ("🔐", "Personal data"),
            ("💰", "Financial & environmental costs")
        ]

        challenge_boxes = VGroup()
        for icon, challenge_text in challenges:
            icon_text = Text(icon, font_size=HEADING_FONT_SIZE)
            text = Text(challenge_text, font_size=BODY_FONT_SIZE, color=WHITE)

            content = VGroup(icon_text, text).arrange(DOWN, buff=0.2)
            box = SurroundingRectangle(content, color=ACCENT_ORANGE, buff=0.3, stroke_width=3)

            challenge_boxes.add(VGroup(box, content))

        # Arrange in 2x3 grid
        row1 = VGroup(*challenge_boxes[:3]).arrange(RIGHT, buff=0.4)
        row2 = VGroup(*challenge_boxes[3:]).arrange(RIGHT, buff=0.4)
        grid = VGroup(row1, row2).arrange(DOWN, buff=0.4).shift(DOWN * 0.2)

        for box in challenge_boxes:
            self.play(FadeIn(box), run_time=0.3)
            self.wait(0.05)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide46_Hallucinations(LLMSlide):
    """Slide 46: Hallucinations"""

    def construct(self):
        title = self.add_title("Challenge: Hallucinations")
        self.play(Write(title), run_time=0.5)

        # Problem
        problem_label = Text("Problem:", font_size=HEADING_FONT_SIZE, color=ACCENT_RED, weight=BOLD)
        problem_label.shift(UP * 2 + LEFT * 4)

        problem_text = Text(
            "Generation of false or\ninconsistent content",
            font_size=BODY_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        problem_text.next_to(problem_label, DOWN, buff=0.2)

        # Reason
        reason_label = Text("Reason:", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        reason_label.shift(UP * 2 + RIGHT * 2)

        reason_text = Text(
            "Insufficient training data\nModel design limitations",
            font_size=BODY_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        reason_text.next_to(reason_label, DOWN, buff=0.2)

        # Solution
        solution_label = Text("Solution:", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        solution_label.shift(DOWN * 0.5)

        solution_text = Text(
            "• Give LLM option not to respond\n• Ask for evidence before answering\n• Use retrieval-augmented generation (RAG)",
            font_size=BODY_FONT_SIZE,
            color=WHITE,
            line_spacing=1.3
        )
        solution_text.next_to(solution_label, DOWN, buff=0.3)

        self.play(FadeIn(VGroup(problem_label, problem_text), shift=RIGHT), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(VGroup(reason_label, reason_text), shift=LEFT), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(VGroup(solution_label, solution_text), shift=UP), run_time=0.6)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide47_QuantizationQuestion(LLMSlide):
    """Slide 47-50: Quantization (combined)"""

    def construct(self):
        title = self.add_title("Which number takes MORE space in memory?")
        self.play(Write(title), run_time=0.5)

        # Question
        optionA = Text("A) 1.2", font_size=TITLE_FONT_SIZE, color=ACCENT_CYAN)
        optionA.shift(LEFT * 3 + UP * 0.5)

        optionB = Text("B) 28", font_size=TITLE_FONT_SIZE, color=ACCENT_ORANGE)
        optionB.shift(RIGHT * 3 + UP * 0.5)

        self.play(FadeIn(optionA), FadeIn(optionB), run_time=0.7)
        self.wait(1)
        self.next_slide()

        # Answer
        answer = Text("Answer: A) 1.2 takes MORE space!", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        answer.shift(DOWN * 0.5)

        self.play(FadeIn(answer, scale=1.2), run_time=0.8)
        self.wait(0.5)

        # Explanation
        explanation = Text(
            "Floating-point numbers (FP16/FP32) require more bits\nthan integers (INT8)",
            font_size=BODY_FONT_SIZE,
            color=WHITE,
            line_spacing=1.3
        )
        explanation.shift(DOWN * 1.8)

        self.play(FadeIn(explanation), run_time=0.6)
        self.wait(PAUSE_TIME)
        self.next_slide()

        # Quantization process
        self.play(FadeOut(VGroup(optionA, optionB, answer, explanation)), run_time=0.3)

        quant_title = Text("Quantization Process", font_size=HEADING_FONT_SIZE, color=ACCENT_CYAN, weight=BOLD)
        quant_title.shift(UP * 2.5)
        self.play(Write(quant_title), run_time=0.5)

        steps = [
            "1. Convert: 1.2 × 23.5 = 28.2 ≈ 28",
            "2. Store as INT8 (8 bits instead of 16)",
            "3. Convert back: 28 ÷ 23.5 = 1.19 ≈ 1.2",
            "Result: 50% memory saved!"
        ]

        step_objects = self.create_bullet_list(steps, font_size=BODY_FONT_SIZE)
        step_objects.shift(DOWN * 0.2)

        for step in step_objects:
            self.play(FadeIn(step, shift=RIGHT), run_time=0.5)
            self.wait(0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide51_CostsAnalysis(LLMSlide):
    """Slide 51: Financial and Environmental Costs"""

    def construct(self):
        title = self.add_title("Financial and Environmental Costs")
        self.play(Write(title), run_time=0.5)

        # Training costs
        training_label = Text("During Training:", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        training_label.shift(UP * 1.8 + LEFT * 4)

        training_costs = [
            "GPT-3: $5 million",
            "GPT-4: $50-100 million",
            "GPT-3 CO₂: 552 tons"
        ]

        training_list = self.create_bullet_list(training_costs, font_size=SMALL_FONT_SIZE)
        training_list.scale(0.9).next_to(training_label, DOWN, buff=0.3)

        # Query costs
        query_label = Text("At Query Stage:", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        query_label.shift(UP * 1.8 + RIGHT * 3)

        query_costs = [
            "10-100× more energy than Google search",
            "25 queries = 1 pint of water",
            "OpenAI: $700K daily maintenance"
        ]

        query_list = self.create_bullet_list(query_costs, font_size=SMALL_FONT_SIZE)
        query_list.scale(0.9).next_to(query_label, DOWN, buff=0.3)

        self.play(FadeIn(VGroup(training_label, training_list), shift=RIGHT), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(VGroup(query_label, query_list), shift=LEFT), run_time=0.6)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide52_PromptInjection(LLMSlide):
    """Slide 52: Prompt Injection"""

    def construct(self):
        title = self.add_title("Prompt Injection")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            'The "grandma trick": using a positive personality inappropriately',
            font_size=BODY_FONT_SIZE,
            color=ACCENT_RED
        )
        definition.shift(UP * 2)
        self.play(Write(definition), run_time=0.7)

        # Security measures
        security_title = Text("4 Key Security Measures:", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        security_title.shift(UP * 0.5)

        measures = [
            "1. Model: Use smallest model to minimize risks",
            "2. System: Use content filter for harmful content",
            "3. Metaprompts: Define behavior parameters",
            "4. UX: Provide transparent documentation"
        ]

        measure_objects = self.create_bullet_list(measures, font_size=SMALL_FONT_SIZE)
        measure_objects.next_to(security_title, DOWN, buff=0.4)

        self.wait(0.3)
        self.play(Write(security_title), run_time=0.6)
        self.wait(0.2)

        for measure in measure_objects:
            self.play(FadeIn(measure, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide53_RLHF(LLMSlide):
    """Slide 53-55: RLHF (combined)"""

    def construct(self):
        title = self.add_title("RLHF: Reinforcement Learning from Human Feedback")
        self.play(Write(title), run_time=0.5)

        # Question
        question = Text(
            "How to teach an LLM what humans expect from it?",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN
        )
        question.shift(UP * 2)
        self.play(Write(question), run_time=0.7)

        # Three steps
        steps = [
            ("1. Training an LLM", "Pre-train on large dataset", ACCENT_GREEN),
            ("2. Reward Model", "Humans rank model responses", ACCENT_ORANGE),
            ("3. RL Optimization", "Fine-tune using rewards", ACCENT_PURPLE)
        ]

        step_boxes = VGroup()
        for step_num, step_desc, color in steps:
            num_text = Text(step_num, font_size=BODY_FONT_SIZE, color=color, weight=BOLD)
            desc_text = Text(step_desc, font_size=SMALL_FONT_SIZE, color=WHITE)

            content = VGroup(num_text, desc_text).arrange(DOWN, buff=0.2)
            box = SurroundingRectangle(content, color=color, buff=0.3, stroke_width=3)

            step_boxes.add(VGroup(box, content))

        step_boxes.arrange(RIGHT, buff=0.5).shift(DOWN * 0.3)

        for box in step_boxes:
            self.play(FadeIn(box, shift=UP), run_time=0.5)
            self.wait(0.2)

        self.wait(PAUSE_TIME)
        self.next_slide()
