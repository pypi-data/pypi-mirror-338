"""
Command-line interface for LlamaCalc.

This module provides the CLI entry point for the LlamaCalc tool.
"""

import sys
import argparse
import json
import textwrap
from typing import Dict, List, Optional, Any, Tuple
import time

try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    HAS_RICH = True
except ImportError:
    HAS_RICH = False

# Local imports
try:
    from .core import calculate_relevance_score, batch_calculate_relevance, RelevanceResult
    from .cache import MemoryCache
except ImportError:
    # For development before package structure is in place
    from core import calculate_relevance_score, batch_calculate_relevance, RelevanceResult
    from cache import MemoryCache


class LlamaUI:
    """Interactive UI for LlamaCalc using Rich."""
    
    def __init__(self):
        """Initialize the UI components."""
        if not HAS_RICH:
            print("The 'rich' package is required for the interactive UI.")
            print("Install it with: pip install rich")
            sys.exit(1)
        
        self.console = Console()
        self.cache = MemoryCache()
    
    def display_header(self):
        """Display the LlamaCalc header."""
        header = """
         _                         _____      _      
        | |                       / ____|    | |     
        | |     __ _ _ __ ___    | |     __ _| | ___ 
        | |    / _` | '_ ` _ \\   | |    / _` | |/ __|
        | |___| (_| | | | | | |  | |___| (_| | | (__ 
        |______\\__,_|_| |_| |_|   \\_____\\__,_|_|\\___|
                                                     
        """
        self.console.print(Panel(header, title="LlamaCalc", subtitle="v0.1.0"))
        self.console.print("Advanced relevance scoring for LLM outputs\n")
    
    def display_result(self, result: RelevanceResult):
        """
        Display a formatted result in the console.
        
        Args:
            result: The RelevanceResult to display
        """
        # Create a table for the scores
        table = Table(title="Relevance Scores")
        
        table.add_column("Component", style="cyan")
        table.add_column("Score", style="magenta")
        table.add_column("Weight", style="green")
        table.add_column("Contribution", style="yellow")
        
        # Default weights
        weights = {
            "Proximity": 0.35,
            "Coverage": 0.30,
            "Conciseness": 0.15,
            "Logical Flow": 0.20
        }
        
        # Add rows for each component
        table.add_row(
            "Proximity", 
            f"{result.proximity_score:.2f}",
            f"{weights['Proximity']:.2f}",
            f"{result.proximity_score * weights['Proximity']:.2f}"
        )
        table.add_row(
            "Coverage", 
            f"{result.coverage_score:.2f}",
            f"{weights['Coverage']:.2f}",
            f"{result.coverage_score * weights['Coverage']:.2f}"
        )
        table.add_row(
            "Conciseness", 
            f"{result.conciseness_score:.2f}",
            f"{weights['Conciseness']:.2f}",
            f"{result.conciseness_score * weights['Conciseness']:.2f}"
        )
        table.add_row(
            "Logical Flow", 
            f"{result.logical_flow_score:.2f}",
            f"{weights['Logical Flow']:.2f}",
            f"{result.logical_flow_score * weights['Logical Flow']:.2f}"
        )
        
        # Add a total row
        table.add_row(
            "TOTAL", 
            f"{result.total_score:.2f}",
            "1.00",
            f"{result.total_score:.2f}",
            style="bold"
        )
        
        # Display the question and answer
        self.console.print("\n[bold]Question:[/bold]")
        self.console.print(result.question)
        
        self.console.print("\n[bold]Answer:[/bold]")
        self.console.print(result.answer)
        
        # Display the scores
        self.console.print("\n[bold]Scores:[/bold]")
        self.console.print(table)
        
        # Display computation info
        self.console.print(f"\nComputation time: [italic]{result.computation_time*1000:.2f}ms[/italic]")
    
    def get_input(self, prompt: str) -> str:
        """Get user input with a styled prompt."""
        return self.console.input(f"[bold cyan]{prompt}[/bold cyan] ")
    
    def run_interactive(self):
        """Run the interactive CLI mode."""
        self.display_header()
        
        while True:
            # Get question
            self.console.print("\n[bold green]Enter a question (or 'q' to quit):[/bold green]")
            question = self.console.input("> ")
            
            if question.lower() in ('q', 'quit', 'exit'):
                break
            
            # Get answer
            self.console.print("\n[bold green]Enter an answer to evaluate:[/bold green]")
            answer = self.console.input("> ")
            
            # Check cache first
            cached_result = self.cache.get(question, answer)
            
            if cached_result:
                self.console.print("[yellow](Result from cache)[/yellow]")
                self.display_result(cached_result)
                continue
            
            # Calculate score with a spinner
            with Progress(
                SpinnerColumn(),
                TextColumn("[bold green]Calculating scores...[/bold green]"),
                transient=True,
            ) as progress:
                progress.add_task("calculate", total=None)
                result = calculate_relevance_score(question, answer)
            
            # Cache the result
            self.cache.put(result)
            
            # Display the result
            self.display_result(result)
        
        self.console.print("\n[bold]Thanks for using LlamaCalc![/bold]")


def format_result_simple(result: RelevanceResult) -> str:
    """
    Format a result as a simple text output.
    
    Args:
        result: The RelevanceResult to format
        
    Returns:
        Formatted string with the results
    """
    output = []
    output.append("== LlamaCalc Results ==")
    output.append(f"Total Score: {result.total_score:.2f}")
    output.append(f"  Proximity: {result.proximity_score:.2f}")
    output.append(f"  Coverage: {result.coverage_score:.2f}")
    output.append(f"  Conciseness: {result.conciseness_score:.2f}")
    output.append(f"  Logical Flow: {result.logical_flow_score:.2f}")
    output.append(f"Computation Time: {result.computation_time*1000:.2f}ms")
    return "\n".join(output)


def read_file(filepath: str) -> str:
    """Read the contents of a file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description="LlamaCalc - Advanced relevance scoring for LLM outputs",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""
        Examples:
          llamacalc --question "What is Python?" --answer "Python is a programming language."
          llamacalc --interactive
          llamacalc --question-file questions.txt --answer-file answers.txt --json
        """)
    )
    
    # Input options
    input_group = parser.add_argument_group("Input Options")
    input_group.add_argument("--question", "-q", type=str, help="The question text")
    input_group.add_argument("--answer", "-a", type=str, help="The answer text")
    input_group.add_argument("--question-file", "-qf", type=str, help="File containing the question")
    input_group.add_argument("--answer-file", "-af", type=str, help="File containing the answer")
    input_group.add_argument("--batch-file", "-bf", type=str, 
                           help="JSON file with array of {question, answer} objects for batch processing")
    
    # Output options
    output_group = parser.add_argument_group("Output Options")
    output_group.add_argument("--json", "-j", action="store_true", help="Output in JSON format")
    output_group.add_argument("--output-file", "-o", type=str, help="Write output to a file")
    
    # Mode options
    mode_group = parser.add_argument_group("Mode Options")
    mode_group.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")
    
    # Weight options
    weight_group = parser.add_argument_group("Weight Options")
    weight_group.add_argument("--proximity-weight", type=float, default=0.35,
                            help="Weight for proximity score (default: 0.35)")
    weight_group.add_argument("--coverage-weight", type=float, default=0.30,
                            help="Weight for coverage score (default: 0.30)")
    weight_group.add_argument("--conciseness-weight", type=float, default=0.15,
                            help="Weight for conciseness score (default: 0.15)")
    weight_group.add_argument("--logical-flow-weight", type=float, default=0.20,
                            help="Weight for logical flow score (default: 0.20)")
    
    args = parser.parse_args()
    
    # Interactive mode
    if args.interactive:
        ui = LlamaUI()
        ui.run_interactive()
        return
    
    # Batch processing mode
    if args.batch_file:
        try:
            with open(args.batch_file, 'r', encoding='utf-8') as f:
                batch_data = json.load(f)
                
            if not isinstance(batch_data, list):
                print("Error: Batch file must contain a JSON array of objects.")
                sys.exit(1)
                
            qa_pairs = []
            for item in batch_data:
                if not isinstance(item, dict) or "question" not in item or "answer" not in item:
                    print("Error: Each item in batch must have 'question' and 'answer' fields.")
                    sys.exit(1)
                qa_pairs.append((item["question"], item["answer"]))
            
            # Set up custom weights
            weights = {
                "proximity": args.proximity_weight,
                "coverage": args.coverage_weight,
                "conciseness": args.conciseness_weight,
                "logical_flow": args.logical_flow_weight
            }
            
            # Process in batch
            results = batch_calculate_relevance(qa_pairs, weights=weights)
            
            # Format output
            if args.json:
                output = json.dumps([r.to_dict() for r in results], indent=2)
            else:
                output_lines = []
                for i, result in enumerate(results):
                    output_lines.append(f"=== Result {i+1} ===")
                    output_lines.append(format_result_simple(result))
                    output_lines.append("")
                output = "\n".join(output_lines)
            
            # Write output
            if args.output_file:
                with open(args.output_file, 'w', encoding='utf-8') as f:
                    f.write(output)
            else:
                print(output)
                
            return
    
    # Single question-answer processing
    question = None
    answer = None
    
    # Get question
    if args.question:
        question = args.question
    elif args.question_file:
        question = read_file(args.question_file)
    
    # Get answer
    if args.answer:
        answer = args.answer
    elif args.answer_file:
        answer = read_file(args.answer_file)
    
    # Validate inputs
    if not question or not answer:
        print("Error: Both question and answer must be provided.")
        parser.print_help()
        sys.exit(1)
    
    # Set up custom weights
    weights = {
        "proximity": args.proximity_weight,
        "coverage": args.coverage_weight,
        "conciseness": args.conciseness_weight,
        "logical_flow": args.logical_flow_weight
    }
    
    # Calculate score
    result = calculate_relevance_score(question, answer, weights=weights)
    
    # Format output
    if args.json:
        output = json.dumps(result.to_dict(), indent=2)
    else:
        output = format_result_simple(result)
    
    # Write output
    if args.output_file:
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(output)
    else:
        print(output)


if __name__ == "__main__":
    main() 