# LLM Explained: Interactive Presentation

[![Deploy static content to Pages](../../actions/workflows/deploy_pages.yml/badge.svg)](../../actions/workflows/deploy_pages.yml)

An interactive, animated presentation about **Large Language Models (LLMs)** and their text generation process, built with [Manim Slides](https://manim-slides.eertmans.be/) and automatically deployed to GitHub Pages.

## 🎯 About

This presentation transforms complex LLM concepts into engaging, step-by-step visualizations covering:

- **Prompt Engineering** - Best practices for creating effective prompts
- **History & Evolution** - From MLPs to Transformers and GPT
- **Tokenization & Embeddings** - How text becomes vectors
- **Attention Mechanism** - The core of modern LLMs
- **Text Generation** - Complete generation pipeline
- **Transformer Architecture** - Encoder-decoder structure
- **Challenges & Solutions** - Hallucinations, quantization, costs
- **API Parameters** - Temperature, top-p, top-k sampling
- **Practical Tools** - Hugging Face and deployment

## 📊 Presentation Structure

The presentation consists of **65 slides** organized into **9 parts**:

| Part | Slides | Topic |
|------|--------|-------|
| 1 | 1-11 | Foundations & Prompt Engineering |
| 2 | 12-20 | History, Definition & RNNs |
| 3 | 21-28 | Text-to-Vector Conversion |
| 4 | 29-31 | Attention Mechanism |
| 5 | 32-41 | Text Generation Process |
| 6 | 42-43 | Overall Architecture |
| 7 | 44-55 | LLM Challenges & Solutions |
| 8 | 56-60 | API Parameters |
| 9 | 61-65 | Hugging Face & Conclusion |

## 🚀 Quick Start

### View Online

The presentation is automatically deployed to GitHub Pages:

🔗 **[View Live Presentation](#)** _(will be available after first deployment)_

### Local Development

**Prerequisites:**
- Python 3.9+
- LaTeX distribution (for mathematical formulas)
- FFmpeg

**Setup:**

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/llm-explained.git
cd llm-explained

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Render Slides:**

```bash
# Render all slides (high quality)
manim slides.py -qh Slide1_TitleIntroduction Slide2_CommunicationRules ...

# Render specific part (e.g., Part 1)
manim scenes/part1_foundations.py -qh Slide1_TitleIntroduction

# Quick preview (low quality, faster)
manim slides.py -ql Slide1_TitleIntroduction
```

**Present Locally:**

```bash
# Convert to HTML
manim-slides convert Slide1_TitleIntroduction Slide2_CommunicationRules ... index.html

# Interactive presentation (Qt)
manim-slides present
```

## 📁 Project Structure

```
llm-explained/
├── .github/
│   └── workflows/
│       └── deploy_pages.yml      # GitHub Actions deployment
├── scenes/
│   ├── part1_foundations.py      # Slides 1-11
│   ├── part2_history.py          # Slides 12-20
│   ├── part3_embeddings.py       # Slides 21-28
│   ├── part4_attention.py        # Slides 29-31
│   ├── part5_generation.py       # Slides 32-41
│   ├── part6_architecture.py     # Slides 42-43
│   ├── part7_challenges.py       # Slides 44-55
│   ├── part8_parameters.py       # Slides 56-60
│   ├── part9_huggingface.py      # Slides 61-65
│   └── __init__.py
├── assets/
│   ├── images/                   # Image assets
│   ├── data/                     # Data for visualizations
│   └── styles/
│       └── theme_config.py       # Colors, fonts, styling
├── utils/
│   ├── custom_scenes.py          # Base scene classes
│   ├── animations.py             # Reusable animations
│   ├── data_generators.py        # Data generation utilities
│   └── __init__.py
├── slides.py                     # Main presentation file
├── requirements.txt              # Python dependencies
├── README.md                     # This file
└── LICENSE.md                    # MIT License
```

## 🎨 Key Features

### Mathematical Visualizations
- Step-by-step formula derivations
- Attention score calculations
- Probability distributions
- Matrix operations (Q, K, V)

### Interactive Elements
- Timeline animations (1960-2023 ML history)
- 3D embedding space visualization
- RNN sequential processing
- Transformer architecture diagrams

### Code Examples
- Python code with syntax highlighting
- Hugging Face transformers usage
- API parameter demonstrations

### Educational Design
- Progressive disclosure of information
- Color-coded concepts
- Clear visual hierarchy
- Consistent styling throughout

## 🛠️ Technologies Used

- **[Manim Community Edition](https://www.manim.community/)** - Mathematical animation engine
- **[Manim Slides](https://manim-slides.eertmans.be/)** - Slide-based presentation framework
- **[GitHub Actions](https://github.com/features/actions)** - Automated rendering and deployment
- **[GitHub Pages](https://pages.github.com/)** - Free hosting
- **Python 3.9+** - Programming language
- **LaTeX** - Mathematical typesetting

## 🔧 Configuration

### Rendering Quality

Edit quality settings in individual scene files or use command-line flags:

```bash
-ql   # Low quality (854x480, 15 fps) - Fast preview
-qm   # Medium quality (1280x720, 30 fps)
-qh   # High quality (1920x1080, 60 fps) - Production
-qk   # 4K quality (3840x2160, 60 fps)
```

### Theme Customization

Modify colors and styling in `assets/styles/theme_config.py`:

```python
# Primary colors
PRIMARY_BLUE = "#1F77B4"
ACCENT_CYAN = "#17BECF"
ACCENT_ORANGE = "#FF7F0E"
# ... and more
```

### GitHub Actions

The deployment workflow is configured in `.github/workflows/deploy_pages.yml`. Key settings:

- **FILE**: `slides.py` (source file)
- **MANIM**: `manim` (renderer to use)
- **SCENES**: Space-separated list of all scene names
- **USES_TEX**: `true` (enable LaTeX support)

## 📚 Content Overview

### Part 1: Prompt Engineering
Learn the essential components of effective prompts: task, context, example, personality, format, and tone. Includes real-world examples and best practices.

### Part 2: History & RNNs
Explore the evolution from MLPs to Transformers, understand Recurrent Neural Networks, and discover major milestones in NLP history.

### Part 3: Embeddings
Deep dive into tokenization, vector representations, Word2Vec (CBOW & Skip-gram), and modern context-aware embeddings with Transformers.

### Part 4: Attention Mechanism
Understand the core innovation behind modern LLMs: multi-head attention, semantic relationships, and Grouped Query Attention (GQA).

### Part 5: Text Generation
Complete walkthrough of the generation pipeline: positional encoding, Q-K-V matrices, attention scores, softmax, and probability prediction.

### Part 6: Architecture
Visual breakdown of the complete Transformer architecture with encoder-decoder structure and layer-by-layer explanation.

### Part 7: Challenges
Address real-world issues: hallucinations, prompt injection, quantization techniques (FP16 to INT8), environmental costs, and RLHF training.

### Part 8: API Parameters
Master temperature, top-p (nucleus sampling), top-k sampling, and system prompts for controlling LLM behavior.

### Part 9: Tools & Conclusion
Practical introduction to Hugging Face, code demonstrations, and next steps for continued learning.

## 🤝 Contributing

Contributions are welcome! Feel free to:

- Report bugs or suggest improvements via [Issues](../../issues)
- Submit pull requests with enhancements
- Add new slides or visualizations
- Improve documentation

**Development workflow:**

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-slide`
3. Make changes and test locally: `manim your_scene.py -ql YourScene`
4. Commit with clear messages: `git commit -m "Add attention mechanism visualization"`
5. Push and create a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- **Manim Community** - For the incredible animation framework
- **Jérome Eertmans** - Creator of Manim Slides
- **DataScientest** - Original LLM course content inspiration
- **Open Source Community** - For all the tools and libraries

## 📞 Contact

For questions, suggestions, or collaboration:

- **Issues**: [GitHub Issues](../../issues)
- **Discussions**: [GitHub Discussions](../../discussions)

---

**Built with ❤️ using Manim Slides**

*Transform complex concepts into beautiful, interactive presentations*
