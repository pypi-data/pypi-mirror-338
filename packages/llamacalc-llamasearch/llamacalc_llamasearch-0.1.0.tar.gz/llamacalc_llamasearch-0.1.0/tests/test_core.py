"""
Tests for the core functionality of LlamaCalc.
"""

import unittest
import sys
from typing import Dict, Any

# Import the core module from the parent directory
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.llamacalc.core import (
        calculate_relevance_score,
        batch_calculate_relevance,
        compute_proximity_score,
        compute_coverage_score,
        compute_conciseness_score,
        compute_logical_flow_score,
        RelevanceResult,
        extract_key_concepts,
        text_to_vector
    )
except ImportError:
    print("Error: Could not import LlamaCalc core module.")
    sys.exit(1)


class TestCoreFunctions(unittest.TestCase):
    """Test case for core scoring functions."""
    
    def setUp(self):
        """Set up common test data."""
        self.question = "What is Python programming language?"
        self.good_answer = """
        Python is a high-level, interpreted programming language known for its 
        readability and simplicity. It supports multiple programming paradigms, 
        including procedural, object-oriented, and functional programming. 
        Python is widely used in web development, data analysis, artificial 
        intelligence, scientific computing, and automation.
        """
        self.poor_answer = "It's a snake."
        self.unrelated_answer = """
        The stock market experienced significant volatility yesterday, with major 
        indices closing lower amid concerns about inflation and interest rates.
        """
    
    def test_calculate_relevance_score(self):
        """Test that calculate_relevance_score returns a valid RelevanceResult."""
        result = calculate_relevance_score(self.question, self.good_answer)
        
        # Check that result is the right type
        self.assertIsInstance(result, RelevanceResult)
        
        # Check that scores are in valid range
        self.assertGreaterEqual(result.total_score, 0.0)
        self.assertLessEqual(result.total_score, 1.0)
        self.assertGreaterEqual(result.proximity_score, 0.0)
        self.assertLessEqual(result.proximity_score, 1.0)
        self.assertGreaterEqual(result.coverage_score, 0.0)
        self.assertLessEqual(result.coverage_score, 1.0)
        self.assertGreaterEqual(result.conciseness_score, 0.0)
        self.assertLessEqual(result.conciseness_score, 1.0)
        self.assertGreaterEqual(result.logical_flow_score, 0.0)
        self.assertLessEqual(result.logical_flow_score, 1.0)
        
        # Check that computation time is positive
        self.assertGreater(result.computation_time, 0.0)
        
        # Check that question and answer are preserved
        self.assertEqual(result.question, self.question)
        self.assertEqual(result.answer, self.good_answer)
        
        # Check that timestamp is set
        self.assertIsNotNone(result.timestamp)
    
    def test_batch_calculate_relevance(self):
        """Test batch calculation of relevance scores."""
        qa_pairs = [
            (self.question, self.good_answer),
            (self.question, self.poor_answer),
            (self.question, self.unrelated_answer)
        ]
        
        results = batch_calculate_relevance(qa_pairs)
        
        # Check that we get the right number of results
        self.assertEqual(len(results), len(qa_pairs))
        
        # Check that all results are valid
        for i, result in enumerate(results):
            self.assertIsInstance(result, RelevanceResult)
            self.assertEqual(result.question, qa_pairs[i][0])
            self.assertEqual(result.answer, qa_pairs[i][1])
    
    def test_proximity_score(self):
        """Test that proximity score correctly identifies relevant vs. irrelevant answers."""
        good_score = compute_proximity_score(self.question, self.good_answer)
        poor_score = compute_proximity_score(self.question, self.poor_answer)
        unrelated_score = compute_proximity_score(self.question, self.unrelated_answer)
        
        # Good answer should score higher than poor answer
        self.assertGreater(good_score, poor_score)
        
        # Good answer should score higher than unrelated answer
        self.assertGreater(good_score, unrelated_score)
        
        # Poor answer might still be slightly relevant, so should score higher than unrelated
        self.assertGreater(poor_score, unrelated_score)
    
    def test_coverage_score(self):
        """Test that coverage score correctly measures concept coverage."""
        good_score = compute_coverage_score(self.question, self.good_answer)
        poor_score = compute_coverage_score(self.question, self.poor_answer)
        
        # Good answer should cover more concepts than poor answer
        self.assertGreater(good_score, poor_score)
    
    def test_conciseness_score(self):
        """Test that conciseness score penalizes answers that are too short or too long."""
        # A very short answer should get a low score
        very_short = "Python."
        very_short_score = compute_conciseness_score(self.question, very_short)
        
        # A very long answer should get a lower score than a moderately sized answer
        very_long = self.good_answer * 10  # Repeat the good answer 10 times
        good_score = compute_conciseness_score(self.question, self.good_answer)
        very_long_score = compute_conciseness_score(self.question, very_long)
        
        self.assertLess(very_short_score, good_score)
        self.assertLess(very_long_score, good_score)
    
    def test_logical_flow_score(self):
        """Test that logical flow score evaluates text coherence."""
        # Well-structured paragraph
        well_structured = """
        Python is a programming language. It was created by Guido van Rossum.
        Python is known for its readability. Many developers prefer Python for
        its simplicity and elegant syntax.
        """
        
        # Poorly structured text with fragments
        poorly_structured = """
        Python. Programming. Created by Guido. Very readable. Simple syntax.
        Elegant. Developers like it. Good for beginners. Many libraries.
        """
        
        well_score = compute_logical_flow_score(well_structured)
        poor_score = compute_logical_flow_score(poorly_structured)
        
        # Well-structured text should score higher
        self.assertGreater(well_score, poor_score)
    
    def test_extract_key_concepts(self):
        """Test that key concept extraction works correctly."""
        concepts = extract_key_concepts("What is Python programming language?")
        
        # Should extract 'what', 'python', 'programming', 'language'
        # 'what' might be filtered out as it's a question word and short
        self.assertIn("python", concepts)
        self.assertIn("programming", concepts)
        self.assertIn("language", concepts)
    
    def test_custom_weights(self):
        """Test that custom weights affect the total score correctly."""
        # Default weights
        default_result = calculate_relevance_score(self.question, self.good_answer)
        
        # Custom weights emphasizing proximity
        proximity_weights = {
            "proximity": 0.7,
            "coverage": 0.1,
            "conciseness": 0.1,
            "logical_flow": 0.1
        }
        proximity_result = calculate_relevance_score(
            self.question, self.good_answer, weights=proximity_weights
        )
        
        # Custom weights emphasizing coverage
        coverage_weights = {
            "proximity": 0.1,
            "coverage": 0.7,
            "conciseness": 0.1,
            "logical_flow": 0.1
        }
        coverage_result = calculate_relevance_score(
            self.question, self.good_answer, weights=coverage_weights
        )
        
        # The total scores should be different based on the weights
        self.assertNotEqual(default_result.total_score, proximity_result.total_score)
        self.assertNotEqual(default_result.total_score, coverage_result.total_score)
        self.assertNotEqual(proximity_result.total_score, coverage_result.total_score)
        
        # The individual component scores should be the same regardless of weights
        self.assertEqual(default_result.proximity_score, proximity_result.proximity_score)
        self.assertEqual(default_result.coverage_score, proximity_result.coverage_score)
        self.assertEqual(default_result.conciseness_score, proximity_result.conciseness_score)
        self.assertEqual(default_result.logical_flow_score, proximity_result.logical_flow_score)
    
    def test_result_to_dict(self):
        """Test that RelevanceResult can be correctly converted to and from a dict."""
        # Create a result
        result = calculate_relevance_score(self.question, self.good_answer)
        
        # Convert to dict
        result_dict = result.to_dict()
        
        # Check that the dict has the expected keys
        expected_keys = [
            "total_score", "proximity_score", "coverage_score", 
            "conciseness_score", "logical_flow_score", 
            "computation_time", "question", "answer", "timestamp"
        ]
        for key in expected_keys:
            self.assertIn(key, result_dict)
        
        # Convert back to RelevanceResult
        new_result = RelevanceResult.from_dict(result_dict)
        
        # Check that we get the same values
        self.assertEqual(result.total_score, new_result.total_score)
        self.assertEqual(result.proximity_score, new_result.proximity_score)
        self.assertEqual(result.coverage_score, new_result.coverage_score)
        self.assertEqual(result.conciseness_score, new_result.conciseness_score)
        self.assertEqual(result.logical_flow_score, new_result.logical_flow_score)
        self.assertEqual(result.computation_time, new_result.computation_time)
        self.assertEqual(result.question, new_result.question)
        self.assertEqual(result.answer, new_result.answer)


if __name__ == '__main__':
    unittest.main() 