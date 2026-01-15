"""
LLM Explained - Interactive Presentation
Complete presentation on Large Language Models

This file imports all slide scenes from the different parts and makes them available for rendering.

To render all slides:
    manim slides.py -qh

To render specific scenes:
    manim slides.py Slide1_TitleIntroduction -qh

To present:
    manim-slides present
"""

# Part 1: Foundations & Prompt Engineering (Slides 1-10)
from scenes.part1_foundations import (
    Slide1_TitleIntroduction,
    Slide2_CommunicationRules,
    Slide3_CourseSummary,
    Slide4_PromptEngineering,
    Slide5_PromptComponents,
    Slide6_ComponentsExample,
    Slide7_PromptBestPractices,
    Slide8_ContentCreationPrompts,
    Slide9_ChatGPTInternetAccess,
    Slide10_PartTransition,
)

# Part 2: History, Definition & RNNs (Slides 12-20)
from scenes.part2_history import (
    Slide12_LLMDefinition,
    Slide13_HistoricalTimeline,
    Slide14_RNNIntroduction,
    Slide15_RNNSequential,
    Slide16_TimelineContinued,
    Slide17_UseCases,
    Slide18_ToolsArchitectureTitle,
    Slide19_NLPSteps,
    Slide20_Word2VecIntroduction,
)

# Part 3: Text-to-Vector Conversion (Slides 21-28)
from scenes.part3_embeddings import (
    Slide21_TokensDefinition,
    Slide22_EmbeddingsDefinition,
    Slide23_EmbeddingsGeneration,
    Slide24_Word2VecTraditional,
    Slide25_Word2VecMethods,
    Slide26_TransformerEmbeddings,
    Slide27_BatDisambiguation,
    Slide28_AttentionIntroduction,
)

# Part 4: Attention Mechanism (Slides 29-31)
from scenes.part4_attention import (
    Slide29_MultiHeadAttention,
    Slide30_AttentionMechanismDeep,
    Slide31_GroupedQueryAttention,
)

# Part 5: Text Generation Process (Slides 32-41)
from scenes.part5_generation import (
    Slide32_TextGenerationTitle,
    Slide33_ProbabilityBasedGeneration,
    Slide34_EmbeddingPositionalEncoding,
    Slide35_QueryKeyValue,
    Slide40_ArchitectureSummary,
    Slide41_PredictionLayer,
)

# Part 6: Overall Architecture (Slides 42-43)
from scenes.part6_architecture import (
    Slide42_TransformerArchitecture,
)

# Part 7: LLM Challenges & Solutions (Slides 44-55)
from scenes.part7_challenges import (
    Slide44_ChallengesTitle,
    Slide45_ChallengesOverview,
    Slide46_Hallucinations,
    Slide47_QuantizationQuestion,
    Slide51_CostsAnalysis,
    Slide52_PromptInjection,
    Slide53_RLHF,
)

# Part 8: API Parameters (Slides 56-60)
from scenes.part8_parameters import (
    Slide56_TemperatureParameter,
    Slide57_TopPSampling,
    Slide58_TopKSampling,
    Slide59_SystemPrompt,
    Slide60_HuggingFaceIntro,
)

# Part 9: Hugging Face & Conclusion (Slides 61-65)
from scenes.part9_huggingface import (
    Slide61_DemoPlaceholder,
    Slide62_ConclusionTitle,
    Slide63_QuestionsAndFeedback,
    Slide64_NextDates,
    Slide65_ThankYou,
)

# List of all scenes in order
ALL_SCENES = [
    # Part 1
    Slide1_TitleIntroduction,
    Slide2_CommunicationRules,
    Slide3_CourseSummary,
    Slide4_PromptEngineering,
    Slide5_PromptComponents,
    Slide6_ComponentsExample,
    Slide7_PromptBestPractices,
    Slide8_ContentCreationPrompts,
    Slide9_ChatGPTInternetAccess,
    Slide10_PartTransition,
    # Part 2
    Slide12_LLMDefinition,
    Slide13_HistoricalTimeline,
    Slide14_RNNIntroduction,
    Slide15_RNNSequential,
    Slide16_TimelineContinued,
    Slide17_UseCases,
    Slide18_ToolsArchitectureTitle,
    Slide19_NLPSteps,
    Slide20_Word2VecIntroduction,
    # Part 3
    Slide21_TokensDefinition,
    Slide22_EmbeddingsDefinition,
    Slide23_EmbeddingsGeneration,
    Slide24_Word2VecTraditional,
    Slide25_Word2VecMethods,
    Slide26_TransformerEmbeddings,
    Slide27_BatDisambiguation,
    Slide28_AttentionIntroduction,
    # Part 4
    Slide29_MultiHeadAttention,
    Slide30_AttentionMechanismDeep,
    Slide31_GroupedQueryAttention,
    # Part 5
    Slide32_TextGenerationTitle,
    Slide33_ProbabilityBasedGeneration,
    Slide34_EmbeddingPositionalEncoding,
    Slide35_QueryKeyValue,
    Slide40_ArchitectureSummary,
    Slide41_PredictionLayer,
    # Part 6
    Slide42_TransformerArchitecture,
    # Part 7
    Slide44_ChallengesTitle,
    Slide45_ChallengesOverview,
    Slide46_Hallucinations,
    Slide47_QuantizationQuestion,
    Slide51_CostsAnalysis,
    Slide52_PromptInjection,
    Slide53_RLHF,
    # Part 8
    Slide56_TemperatureParameter,
    Slide57_TopPSampling,
    Slide58_TopKSampling,
    Slide59_SystemPrompt,
    Slide60_HuggingFaceIntro,
    # Part 9
    Slide61_DemoPlaceholder,
    Slide62_ConclusionTitle,
    Slide63_QuestionsAndFeedback,
    Slide64_NextDates,
    Slide65_ThankYou,
]

# Scene names for command-line rendering
SCENE_NAMES = [scene.__name__ for scene in ALL_SCENES]

if __name__ == "__main__":
    print(f"LLM Explained Presentation - {len(ALL_SCENES)} slides")
    print("\nTo render all scenes:")
    print("  manim slides.py -qh " + " ".join(SCENE_NAMES[:3]) + " ...")
    print("\nTo convert to HTML:")
    print("  manim-slides convert " + " ".join(SCENE_NAMES[:3]) + " index.html")
