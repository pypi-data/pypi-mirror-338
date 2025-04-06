"""
Core calculation functions for LlamaCalc.

This module contains the main scoring functions used to evaluate
the relevance of answers to questions.
"""

import time
import functools
from typing import Dict, List, Tuple, Optional, Any, Union
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime

# Try to import MLX for accelerated computation
try:
    import mlx.core as mx
    import mlx.nn as nn
    HAS_MLX = True
except ImportError:
    import numpy as mx
    HAS_MLX = False


@dataclass
class RelevanceResult:
    """Data class to store the results of a relevance evaluation."""
    total_score: float
    proximity_score: float
    coverage_score: float
    conciseness_score: float
    logical_flow_score: float
    computation_time: float
    question: str
    answer: str
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        return {
            "total_score": self.total_score,
            "proximity_score": self.proximity_score,
            "coverage_score": self.coverage_score,
            "conciseness_score": self.conciseness_score,
            "logical_flow_score": self.logical_flow_score,
            "computation_time": self.computation_time,
            "question": self.question,
            "answer": self.answer,
            "timestamp": self.timestamp.isoformat() if self.timestamp else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'RelevanceResult':
        """Create a RelevanceResult from a dictionary."""
        data_copy = data.copy()
        if "timestamp" in data_copy and data_copy["timestamp"]:
            data_copy["timestamp"] = datetime.fromisoformat(data_copy["timestamp"])
        return cls(**data_copy)


@functools.lru_cache(maxsize=128)
def extract_key_concepts(text: str) -> List[str]:
    """
    Extract key concepts from text using simple NLP techniques.
    
    Args:
        text: The input text to extract concepts from
        
    Returns:
        List of key concepts extracted from the text
    """
    # Simplified implementation - a real version would use more advanced NLP
    words = text.lower().split()
    return [word for word in words if len(word) > 3 and word.isalpha()]


def text_to_vector(text: str) -> mx.array:
    """
    Convert text to a simple vector representation.
    
    This is a simplified implementation. A production version would use
    a proper embedding model.
    
    Args:
        text: The input text to convert
        
    Returns:
        Vector representation of the text
    """
    # Simplified implementation - a real version would use proper embeddings
    words = text.lower().split()
    vector = mx.zeros(100)
    
    for i, word in enumerate(words[:100]):
        # Simple hash-based embedding
        hash_val = hash(word) % 100
        vector = vector.at[hash_val].add(1.0)
    
    # Normalize
    norm = mx.sqrt(mx.sum(vector * vector))
    if norm > 0:
        vector = vector / norm
        
    return vector


def compute_proximity_score(question: str, answer: str) -> float:
    """
    Compute how directly the answer addresses the question.
    
    Args:
        question: The question text
        answer: The answer text
        
    Returns:
        Proximity score between 0.0 and 1.0
    """
    q_vector = text_to_vector(question)
    a_vector = text_to_vector(answer)
    
    # Compute cosine similarity
    similarity = mx.sum(q_vector * a_vector)
    
    # Scale to 0.0-1.0 range
    score = float((similarity + 1.0) / 2.0)
    
    return min(max(score, 0.0), 1.0)


def compute_coverage_score(question: str, answer: str) -> float:
    """
    Compute how well the answer covers key concepts from the question.
    
    Args:
        question: The question text
        answer: The answer text
        
    Returns:
        Coverage score between 0.0 and 1.0
    """
    question_concepts = set(extract_key_concepts(question))
    answer_concepts = set(extract_key_concepts(answer))
    
    if not question_concepts:
        return 0.8  # Default score if no concepts found
    
    # Compute overlap
    overlap = question_concepts.intersection(answer_concepts)
    coverage = len(overlap) / len(question_concepts)
    
    # Apply a soft curve to reward partial coverage
    score = 0.4 + (0.6 * coverage)
    
    return min(max(score, 0.0), 1.0)


def compute_conciseness_score(question: str, answer: str) -> float:
    """
    Evaluate the conciseness of the answer.
    
    Args:
        question: The question text
        answer: The answer text
        
    Returns:
        Conciseness score between 0.0 and 1.0
    """
    question_length = len(question.split())
    answer_length = len(answer.split())
    
    # Expected answer length should be proportional to question length
    # but within reasonable bounds
    expected_min = max(question_length / 2, 10)
    expected_max = max(question_length * 3, 50)
    
    # Too short
    if answer_length < expected_min:
        score = 0.7 * (answer_length / expected_min)
    # Too long
    elif answer_length > expected_max:
        score = 0.7 * (expected_max / answer_length)
    # Just right
    else:
        position = (answer_length - expected_min) / (expected_max - expected_min)
        # Score highest in the middle of the expected range
        score = 0.7 + 0.3 * (1.0 - abs(position - 0.5) * 2)
    
    return min(max(score, 0.0), 1.0)


def compute_logical_flow_score(answer: str) -> float:
    """
    Evaluate the logical flow and coherence of the answer.
    
    Args:
        answer: The answer text
        
    Returns:
        Logical flow score between an 0.0 and 1.0
    """
    # This is a simplified implementation
    # A real version would analyze sentence transitions, coherence, etc.
    sentences = [s.strip() for s in answer.split(".") if s.strip()]
    
    if len(sentences) <= 1:
        return 0.5  # Single sentence answers get a middle score
    
    # Basic checks for logical flow
    score = 0.6  # Base score
    
    # Check for very short sentences (potential fragments)
    short_sentences = sum(1 for s in sentences if len(s.split()) < 3)
    if short_sentences > 0:
        score -= 0.1 * (short_sentences / len(sentences))
    
    # Check for sentence length variation (good for readability)
    lengths = [len(s.split()) for s in sentences]
    if lengths:
        avg_length = sum(lengths) / len(lengths)
        variation = sum(abs(l - avg_length) for l in lengths) / len(lengths)
        normalized_variation = min(variation / 5, 1.0)  # Normalize
        score += 0.1 * normalized_variation  # Some variation is good
    
    # Check for very long sentences (potential readability issues)
    long_sentences = sum(1 for s in sentences if len(s.split()) > 30)
    if long_sentences > 0:
        score -= 0.1 * (long_sentences / len(sentences))
    
    # Add a small bonus for multi-paragraph answers (often well-structured)
    paragraphs = [p for p in answer.split("\n\n") if p.strip()]
    if len(paragraphs) > 1:
        score += 0.1
    
    return min(max(score, 0.0), 1.0)


def calculate_relevance_score(
    question: str, 
    answer: str, 
    weights: Optional[Dict[str, float]] = None
) -> RelevanceResult:
    """
    Calculate the overall relevance score for an answer to a question.
    
    Args:
        question: The question text
        answer: The answer text
        weights: Optional dictionary of weights for each component score
                Default weights are:
                - proximity: 0.35
                - coverage: 0.30
                - conciseness: 0.15
                - logical_flow: 0.20
    
    Returns:
        RelevanceResult object containing all scores and metadata
    """
    # Default weights
    default_weights = {
        "proximity": 0.35,
        "coverage": 0.30,
        "conciseness": 0.15,
        "logical_flow": 0.20
    }
    
    # Use provided weights or defaults
    w = weights or default_weights
    
    # Normalize weights to sum to 1.0
    weight_sum = sum(w.values())
    if weight_sum != 1.0:
        w = {k: v / weight_sum for k, v in w.items()}
    
    start_time = time.time()
    
    # Compute individual scores
    proximity_score = compute_proximity_score(question, answer)
    coverage_score = compute_coverage_score(question, answer)
    conciseness_score = compute_conciseness_score(question, answer)
    logical_flow_score = compute_logical_flow_score(answer)
    
    # Compute weighted total
    total_score = (
        w["proximity"] * proximity_score +
        w["coverage"] * coverage_score +
        w["conciseness"] * conciseness_score +
        w["logical_flow"] * logical_flow_score
    )
    
    computation_time = time.time() - start_time
    
    # Create and return result object
    return RelevanceResult(
        total_score=total_score,
        proximity_score=proximity_score,
        coverage_score=coverage_score,
        conciseness_score=conciseness_score,
        logical_flow_score=logical_flow_score,
        computation_time=computation_time,
        question=question,
        answer=answer
    )


def batch_calculate_relevance(
    qa_pairs: List[Tuple[str, str]], 
    weights: Optional[Dict[str, float]] = None,
    max_workers: int = None
) -> List[RelevanceResult]:
    """
    Calculate relevance scores for a batch of question-answer pairs.
    
    Args:
        qa_pairs: List of (question, answer) tuples
        weights: Optional dictionary of weights for scoring components
        max_workers: Maximum number of threads to use
    
    Returns:
        List of RelevanceResult objects
    """
    if not qa_pairs:
        return []
    
    # Use threading to process in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for question, answer in qa_pairs:
            future = executor.submit(
                calculate_relevance_score,
                question=question,
                answer=answer,
                weights=weights
            )
            futures.append(future)
        
        # Collect results
        results = [future.result() for future in futures]
    
    return results 