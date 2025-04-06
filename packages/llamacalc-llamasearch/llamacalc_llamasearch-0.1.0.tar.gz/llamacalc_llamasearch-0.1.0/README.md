# LlamaCalc

[![PyPI version](https://img.shields.io/pypi/v/llamacalc.svg)](https://pypi.org/project/llamacalc/)
[![Python Versions](https://img.shields.io/pypi/pyversions/llamacalc.svg)](https://pypi.org/project/llamacalc/)
[![License](https://img.shields.io/github/license/llamasearch/llamacalc.svg)](https://llamasearch.ai

**LlamaCalc** is an advanced relevance scoring tool for evaluating how well answers address questions, specifically designed for assessing LLM-generated responses.

![LlamaCalc Demo](https://llamasearch.ai

## Features

- **Multi-Factor Scoring**: Evaluates answer relevance based on proximity, concept coverage, conciseness, and logical flow
- **MLX Acceleration**: Optimized for Apple Silicon using the MLX framework, with fallback to NumPy
- **Command-Line Interface**: Interactive and colorful CLI powered by Rich
- **Batch Processing**: Evaluate multiple question-answer pairs at once
- **Caching**: In-memory and persistent disk caching for faster repeated evaluations
- **Customizable Weights**: Fine-tune the importance of different scoring components
- **Python API**: Easy integration into your Python applications

## Installation

```bash
# Basic installation
pip install llamacalc

# With interactive UI features
pip install llamacalc[ui]

# With MLX acceleration (for Apple Silicon)
pip install llamacalc[mlx]

# With development dependencies
pip install llamacalc[dev]
```

## Quick Start

### Command Line

```bash
# Simple usage
llamacalc --question "What is Python?" --answer "Python is a high-level programming language known for its readability and versatility."

# Interactive mode
llamacalc --interactive

# Batch processing
llamacalc --batch-file qa_pairs.json --json --output-file results.json

# Custom weights
llamacalc -q "What is Python?" -a "Python is a programming language." --proximity-weight 0.4 --coverage-weight 0.3 --conciseness-weight 0.1 --logical-flow-weight 0.2
```

### Python API

```python
from llamacalc import calculate_relevance_score

# Calculate a score
result = calculate_relevance_score(
    question="What is Python?",
    answer="Python is a versatile programming language used in web development, data science, and AI."
)

# Display results
print(f"Total Score: {result.total_score:.2f}")
print(f"Proximity Score: {result.proximity_score:.2f}")
print(f"Coverage Score: {result.coverage_score:.2f}")
print(f"Conciseness Score: {result.conciseness_score:.2f}")
print(f"Logical Flow Score: {result.logical_flow_score:.2f}")

# Custom weights
weights = {
    "proximity": 0.4,
    "coverage": 0.3,
    "conciseness": 0.1,
    "logical_flow": 0.2
}
custom_result = calculate_relevance_score(
    question="What is Python?",
    answer="Python is a programming language.",
    weights=weights
)
```

## Scoring Methodology

LlamaCalc evaluates relevance using four components:

1. **Proximity Score (default weight: 0.35)**: Measures how directly the answer addresses the question using vector similarity.

2. **Coverage Score (default weight: 0.30)**: Evaluates how well the answer covers key concepts from the question.

3. **Conciseness Score (default weight: 0.15)**: Assesses whether the answer is appropriately detailed without being too verbose or too brief.

4. **Logical Flow Score (default weight: 0.20)**: Analyzes the logical structure and coherence of the answer.

The total score is a weighted sum of these components. Scores range from 0.0 to 1.0, with higher scores indicating better relevance.

## Advanced Usage

### Batch Processing

Process multiple question-answer pairs:

```python
from llamacalc import batch_calculate_relevance

qa_pairs = [
    ("What is Python?", "Python is a programming language."),
    ("How does a neural network work?", "Neural networks process data through layers of interconnected nodes."),
    # Add more pairs...
]

results = batch_calculate_relevance(qa_pairs, max_workers=4)

for result in results:
    print(f"Score: {result.total_score:.2f} - Q: {result.question[:30]}...")
```

### Using Caching

```python
from llamacalc import calculate_relevance_score
from llamacalc.cache import MemoryCache, DiskCache

# Memory cache (faster, not persistent)
memory_cache = MemoryCache(max_size=1000, ttl=3600)  # 1 hour TTL

# Check cache first
cached_result = memory_cache.get(question, answer)
if cached_result:
    print("Cache hit!")
    result = cached_result
else:
    # Calculate and cache
    result = calculate_relevance_score(question, answer)
    memory_cache.put(result)

# Persistent disk cache
disk_cache = DiskCache(cache_dir="~/.my_app_cache", ttl=86400*7)  # 1 week TTL
disk_cache.put(result)
```

## Performance Optimization

LlamaCalc automatically uses MLX for accelerated computation if available:

```python
from llamacalc.core import HAS_MLX

print(f"Using MLX acceleration: {HAS_MLX}")
```

For large batches, consider adjusting the number of worker threads:

```python
from llamacalc import batch_calculate_relevance

# Use 8 worker threads for large batches
results = batch_calculate_relevance(large_qa_batch, max_workers=8)
```

## Contributing

Contributions are welcome! Please check our [Contributing Guidelines](CONTRIBUTING.md) for more details.

## License

LlamaCalc is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- LlamaCalc is developed by the [LlamaSearch.AI](https://llamasearch.ai team
- Special thanks to the MLX team for their excellent framework
- Logo design by LlamaSearch.AI
