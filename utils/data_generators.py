"""
Data generators for LLM Explained presentation.
Provides functions to generate data for visualizations.
"""

import numpy as np


def generate_embedding_vectors(words, dimensions=3):
    """
    Generates random embedding vectors for words.

    Args:
        words: List of words
        dimensions: Number of dimensions

    Returns:
        Dictionary mapping words to embedding vectors
    """
    np.random.seed(42)  # For reproducibility
    embeddings = {}

    for word in words:
        embeddings[word] = np.random.randn(dimensions) * 10

    return embeddings


def generate_similar_embeddings(word_pairs, dimensions=3):
    """
    Generates embedding vectors where specified pairs are similar.

    Args:
        word_pairs: List of (word1, word2) tuples that should be similar
        dimensions: Number of dimensions

    Returns:
        Dictionary mapping words to embedding vectors
    """
    np.random.seed(42)
    embeddings = {}

    for word1, word2 in word_pairs:
        # Generate base vector
        base = np.random.randn(dimensions) * 10

        # Add slight variation for second word
        variation = np.random.randn(dimensions) * 2

        embeddings[word1] = base
        embeddings[word2] = base + variation

    return embeddings


def generate_attention_scores(source_tokens, target_tokens, pattern='default'):
    """
    Generates attention scores between source and target tokens.

    Args:
        source_tokens: List of source tokens
        target_tokens: List of target tokens
        pattern: Type of attention pattern ('default', 'diagonal', 'causal')

    Returns:
        2D numpy array of attention scores
    """
    n_source = len(source_tokens)
    n_target = len(target_tokens)

    if pattern == 'diagonal':
        # Attention focuses on corresponding positions
        scores = np.eye(max(n_source, n_target))[:n_source, :n_target]
        scores += np.random.randn(n_source, n_target) * 0.1

    elif pattern == 'causal':
        # Can only attend to previous tokens
        scores = np.tril(np.ones((n_source, n_target)))
        scores += np.random.randn(n_source, n_target) * 0.1

    else:  # default
        # Random attention with some structure
        scores = np.random.rand(n_source, n_target)

    # Normalize to sum to 1 per row (softmax-like)
    scores = np.exp(scores)
    scores = scores / scores.sum(axis=1, keepdims=True)

    return scores


def generate_probability_distribution(words, top_word_index=0, sharpness=2.0):
    """
    Generates a probability distribution over words.

    Args:
        words: List of words
        top_word_index: Index of word with highest probability
        sharpness: How peaked the distribution is (higher = more peaked)

    Returns:
        List of probabilities
    """
    n = len(words)
    logits = np.random.randn(n)

    # Make the top word have highest logit
    logits[top_word_index] += sharpness

    # Softmax
    exp_logits = np.exp(logits)
    probs = exp_logits / exp_logits.sum()

    return probs.tolist()


def generate_qkv_matrices(hidden_dim=4, num_tokens=4):
    """
    Generates Query, Key, Value matrices for attention demonstration.

    Args:
        hidden_dim: Hidden dimension size
        num_tokens: Number of tokens

    Returns:
        Tuple of (Q, K, V) matrices as numpy arrays
    """
    np.random.seed(42)

    Q = np.random.randn(num_tokens, hidden_dim)
    K = np.random.randn(num_tokens, hidden_dim)
    V = np.random.randn(num_tokens, hidden_dim)

    return Q, K, V


def calculate_attention(Q, K, V, scale=True):
    """
    Calculates attention output given Q, K, V matrices.

    Args:
        Q: Query matrix
        K: Key matrix
        V: Value matrix
        scale: Whether to scale by sqrt(d_k)

    Returns:
        Tuple of (attention_scores, attention_weights, output)
    """
    # Attention scores: Q @ K^T
    scores = np.matmul(Q, K.T)

    # Scale
    if scale:
        d_k = K.shape[1]
        scores = scores / np.sqrt(d_k)

    # Softmax
    exp_scores = np.exp(scores - scores.max(axis=1, keepdims=True))
    weights = exp_scores / exp_scores.sum(axis=1, keepdims=True)

    # Output: weights @ V
    output = np.matmul(weights, V)

    return scores, weights, output


def generate_positional_encoding(max_length=10, d_model=4):
    """
    Generates sinusoidal positional encoding.

    Args:
        max_length: Maximum sequence length
        d_model: Model dimension

    Returns:
        Positional encoding matrix
    """
    pos_encoding = np.zeros((max_length, d_model))

    position = np.arange(max_length)[:, np.newaxis]
    div_term = np.exp(np.arange(0, d_model, 2) * -(np.log(10000.0) / d_model))

    pos_encoding[:, 0::2] = np.sin(position * div_term)
    pos_encoding[:, 1::2] = np.cos(position * div_term)

    return pos_encoding


def generate_example_sentence_embedding(sentence, embedding_dim=5):
    """
    Generates example embeddings for a sentence.

    Args:
        sentence: Input sentence (string)
        embedding_dim: Embedding dimension

    Returns:
        Tuple of (tokens, embeddings, positional_encodings)
    """
    # Simple tokenization (split by space)
    tokens = sentence.split()

    # Generate random embeddings
    np.random.seed(hash(sentence) % 2**32)
    embeddings = np.random.randint(1, 11, size=(len(tokens), embedding_dim))

    # Generate positional encodings (simplified as integers)
    positional_encodings = np.arange(1, len(tokens) + 1)

    return tokens, embeddings, positional_encodings


def generate_rnn_hidden_states(sequence_length=5, hidden_dim=3):
    """
    Generates example RNN hidden states.

    Args:
        sequence_length: Length of sequence
        hidden_dim: Hidden state dimension

    Returns:
        List of hidden state vectors
    """
    np.random.seed(42)
    hidden_states = []

    h = np.zeros(hidden_dim)  # Initial hidden state

    for _ in range(sequence_length):
        # Simulate RNN update
        h = np.tanh(np.random.randn(hidden_dim) + h)
        hidden_states.append(h.copy())

    return hidden_states


def generate_word2vec_context_window(sentence, target_index, window_size=2):
    """
    Generates context window for Word2Vec.

    Args:
        sentence: Input sentence (string)
        target_index: Index of target word
        window_size: Context window size

    Returns:
        Tuple of (target_word, context_words)
    """
    words = sentence.split()
    target_word = words[target_index]

    # Get context
    start = max(0, target_index - window_size)
    end = min(len(words), target_index + window_size + 1)

    context_words = words[start:target_index] + words[target_index+1:end]

    return target_word, context_words


def generate_transformer_layer_dims():
    """
    Generates typical transformer layer dimensions.

    Returns:
        Dictionary of dimension parameters
    """
    return {
        'd_model': 512,  # Model dimension
        'd_ff': 2048,    # Feed-forward dimension
        'n_heads': 8,    # Number of attention heads
        'd_k': 64,       # Key/Query dimension (d_model / n_heads)
        'd_v': 64,       # Value dimension
        'vocab_size': 50000,
        'max_seq_length': 512
    }


def generate_cost_comparison_data():
    """
    Generates LLM training cost comparison data.

    Returns:
        Dictionary of model costs
    """
    return {
        'GPT-3': {
            'training_cost_usd': 5_000_000,
            'training_energy_gwh': 1.287,
            'co2_tons': 552,
            'params_billions': 175
        },
        'GPT-4': {
            'training_cost_usd': 75_000_000,  # Estimated
            'training_energy_gwh': 10,  # Estimated
            'co2_tons': 4400,  # Estimated
            'params_billions': 1760  # Estimated
        },
        'DeepSeek': {
            'params_billions': 67,
            'size_fp16_gb': 130,
            'size_int8_gb': 65
        },
        'Claude-3': {
            'params_billions': 300,  # Estimated
            'size_fp16_gb': 600,
            'size_int8_gb': 300
        }
    }


def generate_quantization_example(original_value=1.2, scale_factor=23.5):
    """
    Generates quantization example data.

    Args:
        original_value: Original FP16 value
        scale_factor: Quantization scale factor

    Returns:
        Dictionary with quantization steps
    """
    # Quantize
    quantized = int(original_value * scale_factor)

    # Dequantize
    dequantized = quantized / scale_factor

    # Error
    error = abs(original_value - dequantized)

    return {
        'original': original_value,
        'scale_factor': scale_factor,
        'quantized': quantized,
        'dequantized': dequantized,
        'error': error,
        'error_percent': (error / original_value) * 100
    }


def generate_temperature_distribution(words, temperature=1.0):
    """
    Generates probability distribution with temperature scaling.

    Args:
        words: List of words
        temperature: Temperature parameter

    Returns:
        Dictionary mapping words to probabilities
    """
    np.random.seed(42)

    # Generate logits
    logits = np.random.randn(len(words))

    # Apply temperature
    logits = logits / temperature

    # Softmax
    exp_logits = np.exp(logits - logits.max())
    probs = exp_logits / exp_logits.sum()

    return dict(zip(words, probs.tolist()))


def generate_top_k_example(words, k=2):
    """
    Generates top-k sampling example.

    Args:
        words: List of words
        k: Number of top words to keep

    Returns:
        Tuple of (all_probs, top_k_words, top_k_probs)
    """
    probs = generate_probability_distribution(words, top_word_index=0)

    # Sort by probability
    sorted_indices = np.argsort(probs)[::-1]
    top_k_indices = sorted_indices[:k]

    top_k_words = [words[i] for i in top_k_indices]
    top_k_probs = [probs[i] for i in top_k_indices]

    return probs, top_k_words, top_k_probs


def generate_top_p_example(words, p=0.8):
    """
    Generates top-p (nucleus) sampling example.

    Args:
        words: List of words
        p: Cumulative probability threshold

    Returns:
        Tuple of (all_probs, selected_words, cumulative_prob)
    """
    probs = generate_probability_distribution(words, top_word_index=0)

    # Sort by probability
    sorted_indices = np.argsort(probs)[::-1]
    sorted_probs = [probs[i] for i in sorted_indices]

    # Find words that make up top-p probability mass
    cumsum = np.cumsum(sorted_probs)
    cutoff_index = np.searchsorted(cumsum, p) + 1

    selected_indices = sorted_indices[:cutoff_index]
    selected_words = [words[i] for i in selected_indices]
    selected_probs = [probs[i] for i in selected_indices]

    return probs, selected_words, selected_probs, cumsum[cutoff_index-1]
