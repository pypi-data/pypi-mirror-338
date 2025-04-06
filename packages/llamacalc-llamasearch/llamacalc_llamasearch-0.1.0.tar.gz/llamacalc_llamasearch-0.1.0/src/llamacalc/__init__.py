"""
LlamaCalc: Advanced Relevance Score Calculator
==============================================

A sophisticated tool that evaluates the relevance of answers to questions
using multiple scoring factors, optimized computation, and a beautiful
llama-themed interface.
"""

__version__ = "0.1.0"

from llamacalc.core import (
    calculate_relevance_score,
    batch_calculate_relevance,
    RelevanceResult,
)
from llamacalc.cache import LRUCache

__all__ = [
    "calculate_relevance_score",
    "batch_calculate_relevance",
    "RelevanceResult",
    "LRUCache",
] 