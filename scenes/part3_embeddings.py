"""
Part 3: Text-to-Vector Conversion
Slides 21-28: Tokens, embeddings, Word2Vec, and modern approaches
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


class Slide21_TokensDefinition(LLMSlide):
    """Slide 21: Tokens Definition"""

    def construct(self):
        title = self.add_title("Converting text to vectors: tokens")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "A token is a small unit of text that a model processes",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        definition.shift(UP * 2)
        self.play(Write(definition), run_time=0.7)

        # Bullet points
        bullets = [
            "A token can be a word, sub-word, or character",
            "In English: 1 token ≈ 4-5 characters",
            "Tokenization varies by LLM and algorithm"
        ]

        bullet_objects = self.create_bullet_list(bullets, font_size=SMALL_FONT_SIZE)
        bullet_objects.shift(UP * 0.5)

        for bullet in bullet_objects:
            self.play(FadeIn(bullet, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        # Examples
        example1 = Text("Brian is in the kitchen.", font_size=BODY_FONT_SIZE, color=WHITE)
        tokens1 = VGroup(*[
            Text(t, font_size=SMALL_FONT_SIZE, color=ACCENT_CYAN)
            for t in ["Brian", "|", "is", "|", "in", "|", "the", "|", "kitchen", "|", "."]
        ]).arrange(RIGHT, buff=0.1)

        example2 = Text("Intergovernmentalization", font_size=BODY_FONT_SIZE, color=WHITE)
        tokens2 = VGroup(*[
            Text(t, font_size=SMALL_FONT_SIZE, color=ACCENT_ORANGE)
            for t in ["Inter", "|", "governmental", "|", "ization"]
        ]).arrange(RIGHT, buff=0.1)

        examples = VGroup(
            VGroup(example1, tokens1).arrange(DOWN, buff=0.2),
            VGroup(example2, tokens2).arrange(DOWN, buff=0.2)
        ).arrange(DOWN, buff=0.4)
        examples.shift(DOWN * 1.2)

        self.wait(0.3)
        self.play(FadeIn(examples), run_time=0.8)
        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide22_EmbeddingsDefinition(LLMSlide):
    """Slide 22: Embeddings Concept"""

    def construct(self):
        title = self.add_title("Converting text to vectors: embeddings")
        self.play(Write(title), run_time=0.5)

        # Definition
        definition = Text(
            "An embedding is a vector representing a word",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN,
            weight=BOLD
        )
        definition.shift(UP * 2.5)
        self.play(Write(definition), run_time=0.7)

        # Key concepts
        concepts = [
            "Similar words → similar vectors",
            "Uses cosine similarity to measure closeness",
            "High-dimensional space (100s-1000s of dimensions)"
        ]

        concept_objects = self.create_bullet_list(concepts, font_size=BODY_FONT_SIZE)
        concept_objects.shift(UP * 0.8)

        for concept in concept_objects:
            self.play(FadeIn(concept), run_time=0.4)
            self.wait(0.1)

        # 3D visualization example
        axes = ThreeDAxes(
            x_range=[-5, 15],
            y_range=[-5, 15],
            z_range=[-5, 15],
            x_length=4,
            y_length=4,
            z_length=4
        )
        axes.shift(DOWN * 1.5 + LEFT * 2)

        # Example vectors
        dog_point = Dot3D([10, 3, 2], color=PRIMARY_BLUE, radius=0.1)
        cat_point = Dot3D([10, 3, 1], color=PRIMARY_BLUE, radius=0.1)
        skateboard_point = Dot3D([-3, 3, 2], color=ACCENT_RED, radius=0.1)

        dog_label = Text("dog", font_size=TINY_FONT_SIZE, color=PRIMARY_BLUE)
        dog_label.move_to(axes.c2p(10, 3, 2) + RIGHT * 0.3)

        cat_label = Text("cat", font_size=TINY_FONT_SIZE, color=PRIMARY_BLUE)
        cat_label.move_to(axes.c2p(10, 3, 1) + RIGHT * 0.3)

        skateboard_label = Text("skateboard", font_size=TINY_FONT_SIZE, color=ACCENT_RED)
        skateboard_label.move_to(axes.c2p(-3, 3, 2) + LEFT * 0.5)

        # Note
        note = Text(
            "GPT-4: 3072 dimensions!",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_YELLOW
        )
        note.to_edge(RIGHT).shift(DOWN)

        self.wait(0.3)
        self.add_fixed_in_frame_mobjects(axes)
        self.play(Create(axes), run_time=0.5)
        self.play(
            FadeIn(dog_point), FadeIn(dog_label),
            FadeIn(cat_point), FadeIn(cat_label),
            FadeIn(skateboard_point), FadeIn(skateboard_label),
            run_time=0.8
        )
        self.play(FadeIn(note), run_time=0.4)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide23_EmbeddingsGeneration(LLMSlide):
    """Slide 23: Embeddings Generation Methods"""

    def construct(self):
        title = self.add_title("Embeddings: How are they generated?")
        self.play(Write(title), run_time=0.5)

        # Two approaches
        modern_box = create_box(
            "Modern Way:\nDuring LLM training",
            color=ACCENT_GREEN,
            width=5,
            height=2
        )
        modern_box.shift(LEFT * 3 + UP)

        historical_box = create_box(
            "Historical Way:\nPre-trained algorithms\n(Word2Vec, GloVe, FastText)",
            color=ACCENT_ORANGE,
            width=5,
            height=2
        )
        historical_box.shift(RIGHT * 3 + UP)

        self.play(FadeIn(modern_box, shift=RIGHT), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(historical_box, shift=LEFT), run_time=0.6)

        # Example process
        process_text = Text(
            "Example: Training on sentences containing 'bat'",
            font_size=BODY_FONT_SIZE,
            color=WHITE
        )
        process_text.shift(DOWN * 0.5)

        arrow = Arrow(UP * 0.3, DOWN * 1.5, color=ACCENT_CYAN)

        result = Text(
            "Output: Embedding vector [14.2, 32.0, 0.01, -2.5, ...]",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_CYAN,
            font="Monospace"
        )
        result.shift(DOWN * 2)

        self.wait(0.3)
        self.play(Write(process_text), run_time=0.6)
        self.play(GrowArrow(arrow), run_time=0.4)
        self.play(FadeIn(result), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide24_Word2VecTraditional(LLMSlide):
    """Slide 24: Traditional Word2Vec Method"""

    def construct(self):
        title = self.add_title("Traditional Method: Word2Vec")
        self.play(Write(title), run_time=0.5)

        # Problem statement
        problem = Text(
            'Problem: "bat" has multiple meanings',
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_ORANGE
        )
        problem.shift(UP * 2)
        self.play(Write(problem), run_time=0.6)

        # Training sentences
        sentences = [
            "A bat flew into the cave",
            "He swung the bat and hit a home run"
        ]

        sentence_objects = VGroup()
        for sent in sentences:
            text = Text(sent, font_size=SMALL_FONT_SIZE, color=WHITE)
            sentence_objects.add(text)

        sentence_objects.arrange(DOWN, buff=0.3).shift(UP * 0.5)

        for sent in sentence_objects:
            self.play(FadeIn(sent), run_time=0.4)
            self.wait(0.1)

        # Process
        process = Text(
            "→ Scans all sentences with 'bat'\n→ Creates single vector",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN,
            line_spacing=1.3
        )
        process.shift(DOWN * 0.8)

        result = Text(
            "Result: [14.2, 32.0, 0.01, -2.5, 18.7, ...]",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_GREEN,
            font="Monospace"
        )
        result.shift(DOWN * 1.8)

        issue = Text(
            "⚠️ Same embedding for both meanings!",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_RED
        )
        issue.shift(DOWN * 2.6)

        self.wait(0.3)
        self.play(Write(process), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(result), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(issue), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide25_Word2VecMethods(LLMSlide):
    """Slide 25: CBOW vs Skip-gram"""

    def construct(self):
        title = self.add_title("Word2Vec: CBOW vs Skip-Gram")
        self.play(Write(title), run_time=0.5)

        # Example sentence
        sentence = Text(
            "The car drives fast on the freeway",
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        sentence.shift(UP * 2.5)
        self.play(Write(sentence), run_time=0.6)

        # CBOW (left)
        cbow_title = Text("CBOW", font_size=HEADING_FONT_SIZE, color=ACCENT_GREEN, weight=BOLD)
        cbow_title.shift(LEFT * 4 + UP * 1)

        cbow_desc = Text(
            "Context → Target word\n\nPros: Fast, efficient\nCons: Loses info on rare words",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        cbow_desc.next_to(cbow_title, DOWN, buff=0.3)

        # Skip-gram (right)
        skip_title = Text("Skip-Gram", font_size=HEADING_FONT_SIZE, color=ACCENT_ORANGE, weight=BOLD)
        skip_title.shift(RIGHT * 4 + UP * 1)

        skip_desc = Text(
            "Target word → Context\n\nPros: Better for rare words\nCons: Slower to train",
            font_size=SMALL_FONT_SIZE,
            color=WHITE,
            line_spacing=1.2
        )
        skip_desc.next_to(skip_title, DOWN, buff=0.3)

        self.wait(0.3)
        self.play(FadeIn(VGroup(cbow_title, cbow_desc), shift=RIGHT), run_time=0.6)
        self.wait(0.2)
        self.play(FadeIn(VGroup(skip_title, skip_desc), shift=LEFT), run_time=0.6)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide26_TransformerEmbeddings(LLMSlide):
    """Slide 26: Modern Transformer Approach"""

    def construct(self):
        title = self.add_title("Modern Approach: Transformers")
        self.play(Write(title), run_time=0.5)

        subtitle = Text(
            "✨ Different vector based on context!",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_GREEN,
            weight=BOLD
        )
        subtitle.shift(UP * 2.2)
        self.play(FadeIn(subtitle), run_time=0.5)

        # Example 1: Animal
        ex1 = Text("A bat flew into the cave", font_size=BODY_FONT_SIZE, color=WHITE)
        ex1.shift(UP * 0.8 + LEFT * 3)

        embedding1 = Text(
            "bat → [25, 5, 18, ...]",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_CYAN,
            font="Monospace"
        )
        embedding1.next_to(ex1, DOWN, buff=0.2)

        context1 = Text("(animal meaning)", font_size=TINY_FONT_SIZE, color=ACCENT_GREEN)
        context1.next_to(embedding1, DOWN, buff=0.1)

        # Example 2: Sports equipment
        ex2 = Text("He swung the bat", font_size=BODY_FONT_SIZE, color=WHITE)
        ex2.shift(UP * 0.8 + RIGHT * 3)

        embedding2 = Text(
            "bat → [8, 42, 3, ...]",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_ORANGE,
            font="Monospace"
        )
        embedding2.next_to(ex2, DOWN, buff=0.2)

        context2 = Text("(sports meaning)", font_size=TINY_FONT_SIZE, color=ACCENT_GREEN)
        context2.next_to(embedding2, DOWN, buff=0.1)

        # Comparison box
        comparison = Text(
            "Word2Vec: Static embedding (same vector always)\nTransformers: Dynamic embedding (context-aware)",
            font_size=SMALL_FONT_SIZE,
            color=ACCENT_YELLOW,
            line_spacing=1.3
        )
        comparison.to_edge(DOWN, buff=0.8)

        self.wait(0.3)
        self.play(FadeIn(VGroup(ex1, embedding1, context1), shift=RIGHT), run_time=0.6)
        self.wait(0.3)
        self.play(FadeIn(VGroup(ex2, embedding2, context2), shift=LEFT), run_time=0.6)
        self.wait(0.4)
        self.play(FadeIn(comparison), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide27_BatDisambiguation(LLMSlide):
    """Slide 27: Context Disambiguation Question"""

    def construct(self):
        # Large question mark
        question_mark = Text("?", font_size=120, color=ACCENT_YELLOW, weight=BOLD)
        question_mark.shift(UP * 1)

        # Question
        question = Text(
            'How do we determine which meaning of "bat" to use?',
            font_size=HEADING_FONT_SIZE,
            color=WHITE
        )
        question.shift(DOWN * 0.5)

        # Example
        example = Text(
            '"A bat flew into the cave"',
            font_size=BODY_FONT_SIZE,
            color=ACCENT_CYAN
        )
        example.shift(DOWN * 1.5)

        self.play(FadeIn(question_mark, scale=1.5), run_time=0.8)
        self.wait(0.3)
        self.play(Write(question), run_time=0.7)
        self.wait(0.3)
        self.play(FadeIn(example), run_time=0.5)

        self.wait(PAUSE_TIME)
        self.next_slide()


class Slide28_AttentionIntroduction(LLMSlide):
    """Slide 28: Attention Mechanism Introduction"""

    def construct(self):
        title = self.add_title("The Attention Mechanism")
        self.play(Write(title), run_time=0.5)

        # Definition box
        definition = Text(
            "To capture semantic context, we use the\ncore strength of an LLM: ATTENTION",
            font_size=HEADING_FONT_SIZE,
            color=ACCENT_CYAN,
            weight=BOLD,
            line_spacing=1.3
        )
        def_box = SurroundingRectangle(definition, color=ACCENT_CYAN, buff=0.4, stroke_width=4)
        def_group = VGroup(def_box, definition)
        def_group.shift(UP * 1.5)

        self.play(Create(def_box), Write(definition), run_time=1)

        # Key points
        points = [
            "✓ Used by Transformer models",
            "✓ Looks at each token to determine importance",
            "✓ Captures relationships between words"
        ]

        point_objects = self.create_bullet_list(points, color=WHITE, font_size=BODY_FONT_SIZE)
        point_objects.shift(DOWN * 0.3)

        for point in point_objects:
            self.play(FadeIn(point, shift=RIGHT), run_time=0.4)
            self.wait(0.1)

        # Example visualization
        sentence = Text(
            "He took the mighty bat and hit a home run",
            font_size=SMALL_FONT_SIZE,
            color=WHITE
        )
        sentence.to_edge(DOWN, buff=1.2)

        # Highlight "bat"
        bat_highlight = Rectangle(
            width=0.6,
            height=0.4,
            stroke_color=ACCENT_YELLOW,
            stroke_width=3
        )
        bat_highlight.move_to(sentence.get_center() + LEFT * 0.5)

        self.wait(0.3)
        self.play(Write(sentence), run_time=0.6)
        self.wait(0.2)
        self.play(Create(bat_highlight), run_time=0.3)

        self.wait(PAUSE_TIME)
        self.next_slide()
