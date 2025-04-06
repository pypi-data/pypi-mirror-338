#!/usr/bin/env python3
"""
LlamaCalc: Advanced Relevance Score Calculator with Llama Theme
====================================================================
A sophisticated tool that evaluates relevance of answers to questions
using MLX for accelerated computation, rich visualizations,
and charming llama-themed interfaces.

Optimized for Apple Silicon M3 Max, but runs anywhere.
"""

import sys
import time
import threading
import argparse
import functools
from typing import Dict, List, Tuple, Optional, Any, Union, Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
import random
import json
import os
from datetime import datetime
from rich.layout import Layout
from rich.spinner import Spinner
from rich.text import Text
from rich.panel import Panel

# Third-party imports
try:
    import mlx.core as mx
    import mlx.nn as nn
    HAS_MLX = True
except ImportError:
    print("⚠️  MLX not found. Falling back to NumPy for computations.")
    import numpy as mx
    HAS_MLX = False

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.table import Table
    from rich.text import Text
    from rich.prompt import Prompt, Confirm
    from rich.markdown import Markdown
    from rich.syntax import Syntax
    from rich.live import Live
    from rich.layout import Layout
    HAS_RICH = True
except ImportError:
    print("⚠️  Rich library not found. Falling back to basic terminal output.")
    HAS_RICH = False

# Cache configuration
CACHE_SIZE = 1000  # How many Q&A pairs to cache


# ASCII Art and UI Constants
LLAMA_ASCII = r"""
         [bright_white]    ＿＿＿
         [bright_white]  ／  　　 ＼＼
         [bright_white] / 　　  　 ⌒ ＼＼
         [bright_white]|  　　　    　 |  [yellow]LlamaCalc[/yellow]
         [bright_white]＼    ⌒  　/⌒ /
         [bright_white] ＼＿＿＿_／  /
         [bright_white] / /　      ＼＼
         [bright_white]/ /　   ＿＿＿  ＼＼  
         [bright_white]＼＼  /　    　＼ [bright_yellow]╱╱[/bright_yellow]
         [bright_white] ＼＼/　    　　[bright_yellow]╱╱[/bright_yellow]  
         [bright_white]  ＼[bright_yellow]/ / / / /[/bright_yellow]
"""

LLAMA_FRAMES = [
    r"""
         [bright_white]    ＿＿＿_
         [bright_white]  ／  　　 ＼＼
         [bright_white] / 　　  　 ⌒ ＼＼
         [bright_white]|  　　　    　 |  
         [bright_white]＼    ⌒  　/⌒ /
         [bright_white] ＼＿＿＿_／  /
         [bright_white] / /　      ＼＼
         [bright_white]/ /　   ＿＿＿  ＼＼  
         [bright_white]＼＼  /　    　＼ [bright_yellow]╱╱[/bright_yellow]
         [bright_white] ＼＼/　    　　[bright_yellow]╱╱[/bright_yellow]  
         [bright_white]    [bright_yellow]╱  ╱  ╱[/bright_yellow]
    """,
    r"""
         [bright_white]    ＿＿＿_
         [bright_white]  ／  　　 ＼＼
         [bright_white] / 　　  　 ⌒ ＼＼
         [bright_white]|  　　　    　 |  
         [bright_white]＼    ⌒  　/⌒ /
         [bright_white] ＼＿＿＿_／  /
         [bright_white] / /　      ＼＼
         [bright_white]/ /　   ＿＿＿  ＼＼  
         [bright_white]＼＼  /　    　＼ [bright_yellow]╱╱[/bright_yellow]
         [bright_white] ＼＼/　    　　[bright_yellow]╱╱[/bright_yellow]  
         [bright_white]  [bright_yellow]╱  ╱  ╱[/bright_yellow]
    """,
    r"""
         [bright_white]    ＿＿＿_
         [bright_white]  ／  　　 ＼＼
         [bright_white] / 　　  　 ⌒ ＼＼
         [bright_white]|  　　　    　 |  
         [bright_white]＼    ⌒  　/⌒ /
         [bright_white] ＼＿＿＿_／  /
         [bright_white] / /　      ＼＼
         [bright_white]/ /　   ＿＿＿  ＼＼  
         [bright_white]＼＼  /　    　＼ [bright_yellow]╱[/bright_yellow]
         [bright_white] ＼＼/　    　　[bright_yellow]╱[/bright_yellow]  
         [bright_white][bright_yellow]    ╱  ╱  ╱[/bright_yellow]
    """
]


# ============ Data Models ============

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


# ============ Caching Mechanism ============

class LRUCache:
    """Thread-safe LRU cache for relevance scores."""
    
    def __init__(self, capacity: int = CACHE_SIZE):
        self.capacity = capacity
        self.cache: Dict[Tuple[str, str], RelevanceResult] = {}
        self.order: List[Tuple[str, str]] = []
        self.lock = threading.RLock()
    
    def get(self, question: str, answer: str) -> Optional[RelevanceResult]:
        """Get cached relevance result if it exists."""
        with self.lock:
            key = (question, answer)
            if key not in self.cache:
                return None
            
            # Move to most recently used
            self.order.remove(key)
            self.order.append(key)
            
            return self.cache[key]
    
    def put(self, question: str, answer: str, result: RelevanceResult) -> None:
        """Store relevance result in cache."""
        with self.lock:
            key = (question, answer)
            
            # If key exists, update and move to most recently used
            if key in self.cache:
                self.order.remove(key)
            # If at capacity, remove least recently used
            elif len(self.cache) >= self.capacity:
                lru_key = self.order.pop(0)
                del self.cache[lru_key]
                
            # Add new entry
            self.cache[key] = result
            self.order.append(key)
    
    def clear(self) -> None:
        """Clear all cached results."""
        with self.lock:
            self.cache.clear()
            self.order.clear()
    
    def save_to_file(self, filepath: str) -> None:
        """Save cache to JSON file."""
        with self.lock:
            data = {
                "capacity": self.capacity,
                "entries": [
                    {
                        "question": q,
                        "answer": a,
                        "result": result.to_dict()
                    } for (q, a), result in self.cache.items()
                ]
            }
            
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=2)
    
    def load_from_file(self, filepath: str) -> None:
        """Load cache from JSON file."""
        if not os.path.exists(filepath):
            return
        
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        with self.lock:
            self.capacity = data.get("capacity", self.capacity)
            self.cache.clear()
            self.order.clear()
            
            for entry in data.get("entries", []):
                q = entry["question"]
                a = entry["answer"]
                result = RelevanceResult.from_dict(entry["result"])
                key = (q, a)
                self.cache[key] = result
                self.order.append(key)


# Initialize the global cache
relevance_cache = LRUCache()


# ============ Core Scoring Functions ============

@functools.lru_cache(maxsize=128)
def extract_key_concepts(text: str) -> List[str]:
    """
    Extract key concepts from text using simple NLP techniques.
    
    Args:
        text: The text to extract concepts from
        
    Returns:
        List of key concept strings
    """
    # This is a simplified implementation
    # In a real-world scenario, we might use more sophisticated NLP
    words = text.lower().split()
    # Filter out common stop words (simplified list)
    stop_words = {"the", "a", "an", "and", "is", "are", "in", "of", "to", "for"}
    concepts = [w for w in words if w not in stop_words and len(w) > 2]
    
    # Get unique concepts, preserving order of first appearance
    seen = set()
    unique_concepts = [c for c in concepts if not (c in seen or seen.add(c))]
    
    return unique_concepts


def text_to_vector(text: str) -> mx.array:
    """
    Convert text to a simple bag-of-words numerical vector.
    
    Args:
        text: Input text
        
    Returns:
        MLX/NumPy array representing the text
    """
    # Simple bag of words implementation
    # In production, you'd use embeddings from a model
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Convert to an array of counts
    vector = mx.array(list(word_count.values()), dtype=mx.float32)
    
    # Normalize to unit length for better comparison
    norm = mx.sqrt(mx.sum(vector * vector))
    if norm > 0:
        vector = vector / norm
    
    return vector


def compute_proximity_score(question: str, answer: str) -> float:
    """
    Measure how directly the answer addresses the question.
    
    Args:
        question: The original question
        answer: The answer to evaluate
        
    Returns:
        Proximity score between 0.0 and 1.0
    """
    # Convert to vectors
    q_vector = text_to_vector(question)
    a_vector = text_to_vector(answer)
    
    # Calculate cosine similarity
    # If vectors are very small, default to mid-range score
    if len(q_vector) < 2 or len(a_vector) < 2:
        return 0.5
    
    # Extend the shorter vector with zeros if needed
    if len(q_vector) < len(a_vector):
        q_vector = mx.concatenate([q_vector, mx.zeros(len(a_vector) - len(q_vector))])
    elif len(a_vector) < len(q_vector):
        a_vector = mx.concatenate([a_vector, mx.zeros(len(q_vector) - len(a_vector))])
    
    # Compute dot product
    dot_product = mx.sum(q_vector * a_vector)
    
    # Scale the score, biasing upward for answers that include question content
    raw_score = float(dot_product)
    return min(1.0, max(0.0, raw_score * 0.8 + 0.2))


def compute_coverage_score(question: str, answer: str) -> float:
    """
    Check if the answer covers key concepts from the question.
    
    Args:
        question: The original question
        answer: The answer to evaluate
        
    Returns:
        Coverage score between 0.0 and 1.0
    """
    # Extract key concepts from the question
    key_concepts = extract_key_concepts(question)
    
    if not key_concepts:
        return 0.5  # If no key concepts, give a neutral score
    
    # Count how many key concepts appear in the answer
    answer_lower = answer.lower()
    covered_concepts = sum(1 for concept in key_concepts if concept in answer_lower)
    
    # Calculate coverage percentage
    coverage_percentage = covered_concepts / len(key_concepts)
    
    # Adjust score to reward covering the most important concepts
    # (Simplified: we assume earlier concepts are more important)
    if key_concepts and covered_concepts > 0:
        # Check if the most important concept (first one) is covered
        primary_coverage = float(key_concepts[0] in answer_lower)
        # Blend the primary coverage with the overall coverage
        return 0.4 * primary_coverage + 0.6 * coverage_percentage
    
    return coverage_percentage


def compute_conciseness_score(question: str, answer: str) -> float:
    """
    Evaluate how concise the answer is without losing information.
    
    Args:
        question: The original question
        answer: The answer to evaluate
        
    Returns:
        Conciseness score between 0.0 and 1.0
    """
    # Get key concepts for both question and answer
    question_concepts = extract_key_concepts(question)
    answer_concepts = extract_key_concepts(answer)
    
    # Count tokens (words) in the answer
    answer_tokens = len(answer.split())
    
    # Define ideal length range based on question complexity
    min_ideal_tokens = max(5, len(question_concepts) * 3)
    max_ideal_tokens = max(30, len(question_concepts) * 15)
    
    # Too short answers are penalized
    if answer_tokens < min_ideal_tokens:
        return max(0.0, answer_tokens / min_ideal_tokens)
    
    # Ideal range gets a high score
    if answer_tokens <= max_ideal_tokens:
        return 1.0
    
    # Too long answers get decreasing scores
    oversize_penalty = 1.0 - min(0.5, (answer_tokens - max_ideal_tokens) / (max_ideal_tokens * 2))
    
    # But ensure answers with lots of unique information aren't penalized too much
    information_density = len(set(answer_concepts)) / answer_tokens if answer_tokens else 0
    density_bonus = min(0.3, information_density * 10)
    
    return oversize_penalty + density_bonus


def compute_logical_flow_score(answer: str) -> float:
    """
    Assess the clarity and coherence of the explanation.
    
    Args:
        answer: The answer to evaluate
        
    Returns:
        Logical flow score between 0.0 and 1.0
    """
    # Split into sentences (simple approximation)
    sentences = [s.strip() for s in answer.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    
    if len(sentences) <= 1:
        return 0.7  # Single sentence answers get a decent but not perfect score
    
    # Look for transition words that indicate logical structure
    transition_words = [
        "first", "second", "third", "finally", "however", "therefore", 
        "thus", "consequently", "moreover", "because", "since", "so", "then"
    ]
    
    # Count sentences with transition words
    transition_count = sum(1 for s in sentences if any(t in s.lower() for t in transition_words))
    transition_score = min(1.0, transition_count / (len(sentences) - 1))
    
    # Reward answers with reasonable sentence lengths
    avg_sentence_length = sum(len(s.split()) for s in sentences) / len(sentences)
    length_score = 1.0 if 5 <= avg_sentence_length <= 20 else max(0.0, 1.0 - abs(avg_sentence_length - 12.5) / 12.5)
    
    # Check for extreme variation in sentence lengths (might indicate poor flow)
    if len(sentences) >= 3:
        lengths = [len(s.split()) for s in sentences]
        max_length = max(lengths)
        min_length = min(lengths)
        variation_penalty = min(1.0, (max_length - min_length) / 20.0) * 0.3
    else:
        variation_penalty = 0.0
    
    # Combine scores
    return (0.4 * transition_score + 0.6 * length_score) * (1.0 - variation_penalty)


def calculate_relevance_score(
    question: str, 
    answer: str, 
    weights: Optional[Dict[str, float]] = None
) -> RelevanceResult:
    """
    Calculate the overall relevance score for an answer.
    
    Args:
        question: The original question
        answer: The answer to evaluate
        weights: Optional custom weights for each component
        
    Returns:
        RelevanceResult object with all scores
    """
    # Check cache first
    cached_result = relevance_cache.get(question, answer)
    if cached_result:
        return cached_result
    
    # Default weights if none provided
    if weights is None:
        weights = {
            "proximity": 0.35,
            "coverage": 0.30,
            "conciseness": 0.15,
            "logical_flow": 0.20
        }
    
    start_time = time.time()
    
    # Calculate individual scores
    proximity = compute_proximity_score(question, answer)
    coverage = compute_coverage_score(question, answer)
    conciseness = compute_conciseness_score(question, answer)
    logical_flow = compute_logical_flow_score(answer)
    
    # Calculate weighted sum
    total_score = (
        weights["proximity"] * proximity +
        weights["coverage"] * coverage +
        weights["conciseness"] * conciseness +
        weights["logical_flow"] * logical_flow
    )
    
    # Ensure score is in range [0, 1]
    total_score = min(1.0, max(0.0, total_score))
    
    computation_time = time.time() - start_time
    
    # Create result object
    result = RelevanceResult(
        total_score=total_score,
        proximity_score=proximity,
        coverage_score=coverage,
        conciseness_score=conciseness,
        logical_flow_score=logical_flow,
        computation_time=computation_time,
        question=question,
        answer=answer
    )
    
    # Cache the result
    relevance_cache.put(question, answer, result)
    
    return result


def batch_calculate_relevance(qa_pairs: List[Tuple[str, str]], weights: Optional[Dict[str, float]] = None, 
                              max_workers: int = None) -> List[RelevanceResult]:
    """
    Calculate relevance scores for multiple Q&A pairs in parallel.
    
    Args:
        qa_pairs: List of (question, answer) tuples
        weights: Optional custom weights for each component
        max_workers: Maximum number of threads to use
        
    Returns:
        List of RelevanceResult objects
    """
    if not max_workers:
        # Default to number of cores or 4, whichever is less
        max_workers = min(4, os.cpu_count() or 4)
    
    results = []
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Create futures for each calculation
        futures = [
            executor.submit(calculate_relevance_score, question, answer, weights)
            for question, answer in qa_pairs
        ]
        
        # Collect results as they complete
        for future in futures:
            results.append(future.result())
    
    return results


# ============ UI Components ============

class LlamaUI:
    """Manages the colorful llama-themed user interface."""
    
    def __init__(self):
        self.console = Console() if HAS_RICH else None
        self.spinner_thread = None
        self.spinner_stop_event = threading.Event()
    
    def show_welcome(self):
        """Display the welcome splash screen."""
        if not HAS_RICH:
            print("\n=== Welcome to LlamaCalc ===")
            print("A relevance scoring tool")
            return
        
        # Create title
        title = Text()
        title.append("LlamaCalc ", style="bold yellow")
        title.append("Relevance Score Calculator", style="bright_white")
        
        # Create welcome panel
        panel = Panel(
            Markdown("*The ultimate relevance scoring tool with llama power 🦙*\n\n"
                    "Evaluate how well an answer responds to a question with AI precision."),
            title=title,
            border_style="yellow",
            padding=(1, 2)
        )
        
        # Display llama ASCII art and welcome panel
        self.console.print(LLAMA_ASCII)
        self.console.print(panel)
        self.console.print()
    
    def prompt_question(self) -> str:
        """Prompt the user for a question."""
        if not HAS_RICH:
            return input("Enter your question: ")
        
        return Prompt.ask("[bold green]Enter your question[/bold green]")
    
    def prompt_answer(self) -> str:
        """Prompt the user for an answer to evaluate."""
        if not HAS_RICH:
            return input("Enter the answer to evaluate: ")
        
        return Prompt.ask("[bold green]Enter the answer to evaluate[/bold green]")
    
    def confirm_action(self, message: str) -> bool:
        """Ask the user to confirm an action."""
        if not HAS_RICH:
            resp = input(f"{message} (y/n): ")
            return resp.lower() in ('y', 'yes')
        
        return Confirm.ask(f"[yellow]{message}[/yellow]")
    
    def start_thinking_animation(self, message: str = "Calculating relevance score..."):
        """Start an animated llama 'thinking' spinner in a separate thread."""
        if not HAS_RICH:
            print(message)
            return
        
        # Reset stop event
        self.spinner_stop_event.clear()
        
        # Define animation function
        def animate():
            with Live(refresh_per_second=4) as live:
                frame_idx = 0
                while not self.spinner_stop_event.is_set():
                    # Update animation frame
                    spinner_text = Text()
                    spinner_text.append(f"{message} ", style="bright_white")
                    spinner_text.append("🦙", style="yellow")
                    
                    # Convert text object to string for concatenation with frame
                    frame_content = Text.from_markup(LLAMA_FRAMES[frame_idx % len(LLAMA_FRAMES)])
                    frame_content.append("\n")
                    frame_content.append(spinner_text)
                    
                    live.update(Panel(frame_content))
                    
                    frame_idx += 1
                    time.sleep(0.25)
        
        # Start animation in separate thread
        self.spinner_thread = threading.Thread(target=animate)
        self.spinner_thread.daemon = True
        self.spinner_thread.start()
    
    def stop_thinking_animation(self):
        """Stop the thinking animation."""
        if self.spinner_thread and self.spinner_thread.is_alive():
            self.spinner_stop_event.set()
            self.spinner_thread.join(timeout=1.0)
            self.spinner_thread = None
    
    def display_result(self, result: RelevanceResult):
        """Display the relevance score result in a pretty format."""
        if not HAS_RICH:
            print(f"\nRelevance Score: {result.total_score:.2f}")
            print(f"Proximity: {result.proximity_score:.2f}")
            print(f"Coverage: {result.coverage_score:.2f}")
            print(f"Conciseness: {result.conciseness_score:.2f}")
            print(f"Logical Flow: {result.logical_flow_score:.2f}")
            print(f"Computation Time: {result.computation_time:.3f} seconds")
            return
        
        # Create score table
        table = Table(title="Score Breakdown", border_style="yellow")
        table.add_column("Component", style="cyan")
        table.add_column("Score", style="green")
        table.add_column("Rating", style="magenta")
        
        # Helper function to get rating text and style
        def get_rating(score):
            if score >= 0.85:
                return "Excellent", "green"
            elif score >= 0.7:
                return "Good", "green"
            elif score >= 0.5:
                return "Fair", "yellow"
            elif score >= 0.3:
                return "Poor", "red"
            else:
                return "Very Poor", "red"
        
        # Add rows to table
        components = [
            ("Total Score", result.total_score),
            ("Answer Proximity", result.proximity_score),
            ("Key Concept Coverage", result.coverage_score),
            ("Conciseness", result.conciseness_score),
            ("Logical Flow", result.logical_flow_score)
        ]
        
        for name, score in components:
            rating, style = get_rating(score)
            table.add_row(name, f"{score:.2f}", Text(rating, style=style))
        
        # Create feedback message based on total score
        if result.total_score >= 0.85:
            feedback = "[green]This answer is llama-tastic! 🦙 Top-notch response![/green]"
        elif result.total_score >= 0.7:
            feedback = "[green]A solid answer! The llama approves. 🦙👍[/green]"
        elif result.total_score >= 0.5:
            feedback = "[yellow]Not bad, but this llama thinks there's room for improvement. 🦙[/yellow]"
        elif result.total_score >= 0.3:
            feedback = "[red]This answer needs more hay (content). 🦙❌[/red]"
        else:
            feedback = "[red]Oh no! This llama is not impressed. Major improvements needed! 🦙😢[/red]"
        
        # Create result panel
        panel = Panel(
            Text.from_markup(f"{table}\n\n{feedback}\n\nComputation Time: {result.computation_time:.3f} seconds"),
            title="[bold yellow]LlamaCalc Result[/bold yellow]",
            border_style="yellow",
            padding=(1, 2)
        )
        
        self.console.print(panel)
    
    def display_batch_results(self, results: List[RelevanceResult]):
        """Display results for a batch of Q&A evaluations."""
        if not HAS_RICH:
            print(f"\nBatch Results ({len(results)} Q&A pairs):")
            for i, result in enumerate(results):
                print(f"\nPair {i+1}:")
                print(f"Q: {result.question[:50]}...")
                print(f"A: {result.answer[:50]}...")
                print(f"Score: {result.total_score:.2f}")
            return
        
        # Create results table
        table = Table(title=f"Batch Results ({len(results)} Q&A pairs)", border_style="yellow")
        table.add_column("#", style="cyan", justify="right")
        table.add_column("Question", style="green", max_width=30)
        table.add_column("Answer", style="blue", max_width=30)
        table.add_column("Score", style="magenta", justify="right")
        
        for i, result in enumerate(results):
            # Truncate long text
            q_short = result.question[:30] + "..." if len(result.question) > 30 else result.question
            a_short = result.answer[:30] + "..." if len(result.answer) > 30 else result.answer
            
            # Add results row
            score_color = "green" if result.total_score >= 0.7 else "yellow" if result.total_score >= 0.5 else "red"
            table.add_row(
                str(i+1),
                q_short,
                a_short,
                Text(f"{result.total_score:.2f}", style=score_color)
            )
        
        # Calculate summary statistics
        avg_score = sum(r.total_score for r in results) / len(results)
        best_idx = max(range(len(results)), key=lambda i: results[i].total_score)
        worst_idx = min(range(len(results)), key=lambda i: results[i].total_score)
        
        # First display the table
        self.console.print(Panel(
            table,
            title="[bold yellow]LlamaCalc Batch Results[/bold yellow]",
            border_style="yellow"
        ))
        
        # Then display summary
        summary = Text()
        summary.append("\n📊 Summary Statistics:\n", style="yellow")
        summary.append(f"Average Score: ", style="bright_white")
        summary.append(f"{avg_score:.2f}\n", style="green")
        
        # Add best and worst
        summary.append(f"Best Score: ", style="bright_white")
        summary.append(f"{results[best_idx].total_score:.2f} (Pair {best_idx+1})\n", style="green")
        summary.append(f"Worst Score: ", style="bright_white")
        summary.append(f"{results[worst_idx].total_score:.2f} (Pair {worst_idx+1})\n", style="red")
        
        self.console.print(Panel(
            summary,
            title="[bold yellow]Summary[/bold yellow]",
            border_style="yellow"
        ))
    
    def display_error(self, message: str):
        """Display an error message."""
        if not HAS_RICH:
            print(f"ERROR: {message}")
            return
        
        self.console.print(f"[bold red]ERROR:[/bold red] {message}")
    
    def display_info(self, message: str):
        """Display an informational message."""
        if not HAS_RICH:
            print(message)
            return
        
        self.console.print(f"[bright_yellow]INFO:[/bright_yellow] {message}")


# ============ Command Line Interface ============

def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="LlamaCalc: Advanced Relevance Score Calculator with Llama Theme",
        epilog="For more information, see the README file."
    )
    
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "-i", "--interactive", 
        action="store_true",
        help="Run in interactive mode (default)"
    )
    mode_group.add_argument(
        "-b", "--benchmark", 
        action="store_true",
        help="Run performance benchmark"
    )
    
    parser.add_argument(
        "-q", "--question",
        type=str,
        help="Question to evaluate"
    )
    parser.add_argument(
        "-a", "--answer",
        type=str,
        help="Answer to evaluate"
    )
    
    parser.add_argument(
        "-f", "--file",
        type=str,
        help="JSON file containing Q&A pairs to evaluate"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        help="Output file for results (JSON format)"
    )
    
    parser.add_argument(
        "-w", "--weights",
        type=str,
        help="Custom weights for scoring components (format: 'prox:0.35,cov:0.30,conc:0.15,flow:0.20')"
    )
    
    parser.add_argument(
        "-c", "--cache",
        type=str,
        help="Cache file to use for storing/loading results"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    
    args = parser.parse_args()
    
    # Default to interactive mode if no other mode specified
    if not (args.interactive or args.benchmark or args.question or args.file):
        args.interactive = True
    
    return args


def parse_weights(weights_str: str) -> Dict[str, float]:
    """
    Parse weights string into a dictionary.
    
    Args:
        weights_str: String in format 'prox:0.35,cov:0.30,conc:0.15,flow:0.20'
        
    Returns:
        Dictionary mapping score components to weights
    """
    if not weights_str:
        return None
    
    weights = {}
    components = {
        'prox': 'proximity',
        'cov': 'coverage',
        'conc': 'conciseness',
        'flow': 'logical_flow'
    }
    
    try:
        parts = weights_str.split(',')
        for part in parts:
            key, value = part.split(':')
            key = key.strip().lower()
            
            # Map abbreviated keys to full names
            if key in components:
                key = components[key]
            
            # Parse and validate weight
            weight = float(value)
            if weight < 0 or weight > 1:
                raise ValueError(f"Weight must be between 0 and 1: {weight}")
            
            weights[key] = weight
        
        # Normalize weights to sum to 1.0
        total = sum(weights.values())
        if total == 0:
            raise ValueError("Sum of weights cannot be zero")
        
        weights = {k: v / total for k, v in weights.items()}
        
        return weights
    except Exception as e:
        raise ValueError(f"Invalid weight format. Should be 'prox:0.35,cov:0.30,conc:0.15,flow:0.20'. Error: {e}")


def load_qa_pairs_from_file(filepath: str) -> List[Tuple[str, str]]:
    """
    Load question-answer pairs from a JSON file.
    
    Args:
        filepath: Path to JSON file
        
    Returns:
        List of (question, answer) tuples
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Expected format: {"pairs": [{"question": "...", "answer": "..."}, ...]}
        if not isinstance(data, dict) or 'pairs' not in data:
            raise ValueError("JSON file must contain a 'pairs' key with an array of Q&A objects")
        
        pairs = []
        for item in data['pairs']:
            if 'question' not in item or 'answer' not in item:
                continue
            pairs.append((item['question'], item['answer']))
        
        return pairs
    except Exception as e:
        raise ValueError(f"Failed to load Q&A pairs from file: {e}")


def save_results_to_file(results: List[RelevanceResult], filepath: str):
    """Save results to a JSON file."""
    data = {
        "results": [r.to_dict() for r in results],
        "timestamp": datetime.now().isoformat(),
        "count": len(results)
    }
    
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)


def run_benchmark():
    """Run a performance benchmark of the relevance scoring system."""
    ui = LlamaUI()
    ui.show_welcome()
    
    ui.display_info("Running LlamaCalc performance benchmark...")
    
    # Generate sample questions and answers of varying complexity
    benchmark_samples = [
        # Simple QA pairs
        ("What is the capital of France?", "Paris is the capital of France."),
        ("What color is the sky?", "The sky appears blue due to Rayleigh scattering of sunlight."),
        
        # Medium complexity
        (
            "How does photosynthesis work?",
            "Photosynthesis is the process by which plants convert light energy into chemical energy. "
            "Plants capture sunlight using chlorophyll and use it to convert water and carbon dioxide "
            "into glucose and oxygen."
        ),
        (
            "What causes climate change?",
            "Climate change is primarily caused by greenhouse gas emissions from burning fossil fuels "
            "and deforestation. These activities increase CO2 levels in the atmosphere, trapping more "
            "heat and raising global temperatures."
        ),
        
        # High complexity
        (
            "Explain quantum computing and its potential applications.",
            "Quantum computing leverages quantum mechanics principles like superposition and entanglement "
            "to perform computations. Unlike classical computers using bits (0 or 1), quantum computers use "
            "qubits that can exist in multiple states simultaneously. This enables them to solve certain "
            "problems exponentially faster than classical computers, with potential applications in "
            "cryptography, drug discovery, optimization problems, and material science."
        )
    ]
    
    # Create some intentionally poor answers for contrast
    poor_samples = [
        ("What is the capital of France?", "France is in Europe."),
        ("How does photosynthesis work?", "Plants grow using sunlight.")
    ]
    
    # Mix good and poor answers
    all_samples = benchmark_samples + poor_samples
    
    # Prepare for benchmark
    ui.display_info(f"Benchmarking with {len(all_samples)} Q&A pairs...")
    start_time = time.time()
    
    # Individual timing
    ui.start_thinking_animation("Benchmarking individual scoring performance...")
    individual_times = []
    
    for question, answer in all_samples:
        sample_start = time.time()
        result = calculate_relevance_score(question, answer)
        sample_time = time.time() - sample_start
        individual_times.append(sample_time)
    
    ui.stop_thinking_animation()
    
    # Batch timing
    ui.start_thinking_animation("Benchmarking batch scoring performance...")
    batch_start = time.time()
    batch_results = batch_calculate_relevance(all_samples)
    batch_time = time.time() - batch_start
    ui.stop_thinking_animation()
    
    # Calculate stats
    avg_individual = sum(individual_times) / len(individual_times)
    total_individual = sum(individual_times)
    speedup = total_individual / batch_time if batch_time > 0 else float('inf')
    
    # Display results
    total_time = time.time() - start_time
    ui.display_info(f"Benchmark completed in {total_time:.2f} seconds")
    
    if HAS_RICH:
        table = Table(title="Benchmark Results", border_style="yellow")
        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="green")
        
        table.add_row("Total Q&A Pairs", str(len(all_samples)))
        table.add_row("Average Individual Time", f"{avg_individual:.4f} seconds")
        table.add_row("Total Individual Time", f"{total_individual:.4f} seconds")
        table.add_row("Batch Processing Time", f"{batch_time:.4f} seconds")
        table.add_row("Parallel Speedup", f"{speedup:.2f}x")
        
        # Add system info
        table.add_row("MLX Acceleration", "Enabled" if HAS_MLX else "Disabled")
        table.add_row("Rich UI", "Enabled" if HAS_RICH else "Disabled")
        
        ui.console.print(Panel(table, title="[bold yellow]LlamaCalc Benchmark[/bold yellow]"))
    else:
        print("\n=== Benchmark Results ===")
        print(f"Total Q&A Pairs: {len(all_samples)}")
        print(f"Average Individual Time: {avg_individual:.4f} seconds")
        print(f"Total Individual Time: {total_individual:.4f} seconds")
        print(f"Batch Processing Time: {batch_time:.4f} seconds")
        print(f"Parallel Speedup: {speedup:.2f}x")
        print(f"MLX Acceleration: {'Enabled' if HAS_MLX else 'Disabled'}")
        print(f"Rich UI: {'Enabled' if HAS_RICH else 'Disabled'}")


def interactive_mode():
    """Run the interactive command-line interface."""
    ui = LlamaUI()
    ui.show_welcome()
    
    while True:
        # Get question and answer from user
        question = ui.prompt_question()
        if not question:
            ui.display_info("No question entered. Exiting.")
            break
        
        answer = ui.prompt_answer()
        if not answer:
            ui.display_info("No answer entered. Exiting.")
            break
        
        # Calculate relevance score
        ui.start_thinking_animation()
        result = calculate_relevance_score(question, answer)
        ui.stop_thinking_animation()
        
        # Display results
        ui.display_result(result)
        
        # Ask if user wants to continue
        if not ui.confirm_action("Evaluate another Q&A pair?"):
            break
    
    ui.display_info("Thank you for using LlamaCalc! 🦙")


def main():
    """Main entry point for the program."""
    try:
        args = parse_args()
        
        # Load cache if specified
        if args.cache:
            if os.path.exists(args.cache):
                relevance_cache.load_from_file(args.cache)
        
        # Parse custom weights if provided
        weights = None
        if args.weights:
            weights = parse_weights(args.weights)
        
        # Run in benchmark mode
        if args.benchmark:
            run_benchmark()
        
        # Run with single Q&A pair from command line
        elif args.question and args.answer:
            ui = LlamaUI()
            ui.show_welcome()
            
            ui.start_thinking_animation()
            result = calculate_relevance_score(args.question, args.answer, weights)
            ui.stop_thinking_animation()
            
            ui.display_result(result)
        
        # Run with Q&A pairs from file
        elif args.file:
            ui = LlamaUI()
            ui.show_welcome()
            
            ui.display_info(f"Loading Q&A pairs from {args.file}...")
            qa_pairs = load_qa_pairs_from_file(args.file)
            
            if not qa_pairs:
                ui.display_error("No valid Q&A pairs found in file.")
                return
            
            ui.display_info(f"Processing {len(qa_pairs)} Q&A pairs...")
            ui.start_thinking_animation(f"Evaluating {len(qa_pairs)} Q&A pairs...")
            
            results = batch_calculate_relevance(qa_pairs, weights)
            
            ui.stop_thinking_animation()
            ui.display_batch_results(results)
            
            if args.output:
                ui.display_info(f"Saving results to {args.output}...")
                save_results_to_file(results, args.output)
        
        # Run in interactive mode (default)
        else:
            interactive_mode()
        
        # Save cache if specified
        if args.cache:
            relevance_cache.save_to_file(args.cache)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user. Exiting.")
    except Exception as e:
        if 'ui' in locals():
            ui.display_error(f"An error occurred: {str(e)}")
        else:
            print(f"ERROR: {str(e)}")


if __name__ == "__main__":
    main()