#!/usr/bin/env python3
"""
Unit tests for LlamaCalc relevance scoring functions.
"""

import unittest
import json
import tempfile
import os
from llamacalc import (
    calculate_relevance_score,
    compute_proximity_score,
    compute_coverage_score,
    compute_conciseness_score,
    compute_logical_flow_score,
    extract_key_concepts,
    LRUCache,
    RelevanceResult,
    batch_calculate_relevance
)


class TestRelevanceScoring(unittest.TestCase):
    """Tests for the core scoring functionality."""
    
    def test_extract_key_concepts(self):
        """Test extraction of key concepts from a question."""
        question = "What is the capital of France?"
        concepts = extract_key_concepts(question)
        self.assertIn("capital", concepts)
        self.assertIn("france", concepts)
        
        # Test caching
        concepts2 = extract_key_concepts(question)
        self.assertEqual(concepts, concepts2)  # Should be the exact same object due to caching
    
    def test_proximity_score(self):
        """Test proximity scoring."""
        question = "What is the capital of France?"
        
        # Perfect answer should score high
        perfect_answer = "The capital of France is Paris."
        perfect_score = compute_proximity_score(question, answer=perfect_answer)
        self.assertGreater(perfect_score, 0.7)
        
        # Irrelevant answer should score low
        irrelevant_answer = "Bananas are yellow fruits that grow in tropical climates."
        irrelevant_score = compute_proximity_score(question, answer=irrelevant_answer)
        self.assertLess(irrelevant_score, 0.5)
        
        # Partially relevant
        partial_answer = "France is a European country with many beautiful cities."
        partial_score = compute_proximity_score(question, answer=partial_answer)
        self.assertGreater(partial_score, irrelevant_score)
        self.assertLess(partial_score, perfect_score)
    
    def test_coverage_score(self):
        """Test coverage scoring."""
        question = "What are the symptoms of influenza and how is it treated?"
        
        # Answer covers all key concepts
        full_coverage = "Influenza symptoms include fever, cough, and fatigue. It is treated with rest, fluids, and sometimes antiviral medications."
        full_score = compute_coverage_score(question, answer=full_coverage)
        self.assertGreater(full_score, 0.8)
        
        # Answer covers only symptoms
        partial_coverage = "Influenza symptoms include fever, cough, and fatigue."
        partial_score = compute_coverage_score(question, answer=partial_coverage)
        self.assertGreater(partial_score, 0.3)
        self.assertLess(partial_score, full_score)
        
        # Answer covers nothing
        no_coverage = "It's important to get vaccinated every year."
        no_score = compute_coverage_score(question, answer=no_coverage)
        self.assertLess(no_score, partial_score)
    
    def test_conciseness_score(self):
        """Test conciseness scoring."""
        question = "What is photosynthesis?"
        
        # Concise answer
        concise = "Photosynthesis is the process by which plants convert light energy into chemical energy."
        concise_score = compute_conciseness_score(question, answer=concise)
        self.assertGreater(concise_score, 0.7)
        
        # Too short (incomplete)
        too_short = "It's a plant process."
        short_score = compute_conciseness_score(question, answer=too_short)
        self.assertLess(short_score, concise_score)
        
        # Too verbose
        verbose = "Photosynthesis is the process by which plants convert light energy into chemical energy. " + \
                 "It occurs in all plants, algae, and many bacteria. During photosynthesis, plants take in " + \
                 "carbon dioxide and water, using energy from sunlight to convert them into glucose and oxygen. " + \
                 "The process primarily takes place in plant leaves through specialized cell structures called " + \
                 "chloroplasts. These chloroplasts contain a green pigment called chlorophyll, which absorbs " + \
                 "light energy. This energy is then used to break down water molecules, releasing oxygen as a " + \
                 "byproduct. The carbon dioxide is incorporated into organic molecules, forming glucose and other " + \
                 "carbohydrates. These carbohydrates serve as energy storage for the plant and as building blocks " + \
                 "for growth. The process of photosynthesis is crucial for life on Earth as it produces oxygen and " + \
                 "serves as the basis for most food chains. It's a remarkably efficient process that has evolved " + \
                 "over billions of years." * 3  # Make it really verbose
        verbose_score = compute_conciseness_score(question, answer=verbose)
        self.assertLess(verbose_score, concise_score)
    
    def test_logical_flow_score(self):
        """Test logical flow scoring."""
        # Well-structured answer with logical transitions
        good_flow = "First, the heart pumps blood to the lungs to pick up oxygen. Second, the oxygenated blood returns to the heart. Finally, the heart pumps this oxygen-rich blood to the rest of the body."
        good_score = compute_logical_flow_score(good_flow)
        self.assertGreater(good_score, 0.7)
        
        # Poor structure
        poor_flow = "Blood goes to body. Heart is a muscle. Oxygen is important. Veins and arteries exist."
        poor_score = compute_logical_flow_score(poor_flow)
        self.assertLess(poor_score, good_score)
    
    def test_overall_relevance_score(self):
        """Test the overall relevance scoring."""
        question = "What causes climate change and what are its effects?"
        
        # Good answer
        good_answer = "Climate change is primarily caused by greenhouse gas emissions from human activities like burning fossil fuels. Effects include rising sea levels, more extreme weather events, and disruption to ecosystems."
        good_result = calculate_relevance_score(question, good_answer)
        self.assertGreater(good_result.total_score, 0.7)
        
        # Poor answer
        poor_answer = "The weather changes all the time. It's natural."
        poor_result = calculate_relevance_score(question, poor_answer)
        self.assertLess(poor_result.total_score, 0.5)
        
        # Verify that all component scores are included
        self.assertTrue(hasattr(good_result, 'proximity_score'))
        self.assertTrue(hasattr(good_result, 'coverage_score'))
        self.assertTrue(hasattr(good_result, 'conciseness_score'))
        self.assertTrue(hasattr(good_result, 'logical_flow_score'))
        
        # Verify that computation time is tracked
        self.assertGreater(good_result.computation_time, 0)
    
    def test_batch_calculation(self):
        """Test batch calculation of relevance scores."""
        qa_pairs = [
            ("What is the capital of France?", "Paris is the capital of France."),
            ("What is the capital of Italy?", "Rome is the capital of Italy."),
            ("What is the capital of Japan?", "Tokyo is the capital of Japan.")
        ]
        
        results = batch_calculate_relevance(qa_pairs)
        
        # Check that we got the right number of results
        self.assertEqual(len(results), len(qa_pairs))
        
        # Check that all results have the correct structure
        for result in results:
            self.assertIsInstance(result, RelevanceResult)
            self.assertTrue(0 <= result.total_score <= 1)


class TestCaching(unittest.TestCase):
    """Tests for the caching functionality."""
    
    def test_lru_cache(self):
        """Test the LRU caching mechanism."""
        cache = LRUCache(capacity=2)
        
        # Create sample results
        result1 = RelevanceResult(
            total_score=0.8,
            proximity_score=0.8,
            coverage_score=0.9,
            conciseness_score=0.7,
            logical_flow_score=0.8,
            computation_time=0.1,
            question="Question 1",
            answer="Answer 1"
        )
        
        result2 = RelevanceResult(
            total_score=0.6,
            proximity_score=0.6,
            coverage_score=0.7,
            conciseness_score=0.5,
            logical_flow_score=0.6,
            computation_time=0.1,
            question="Question 2",
            answer="Answer 2"
        )
        
        # Add to cache
        cache.put("Question 1", "Answer 1", result1)
        cache.put("Question 2", "Answer 2", result2)
        
        # Check retrieval
        self.assertEqual(cache.get("Question 1", "Answer 1"), result1)
        self.assertEqual(cache.get("Question 2", "Answer 2"), result2)
        
        # Add one more (exceeding capacity)
        result3 = RelevanceResult(
            total_score=0.7,
            proximity_score=0.7,
            coverage_score=0.8,
            conciseness_score=0.6,
            logical_flow_score=0.7,
            computation_time=0.1,
            question="Question 3",
            answer="Answer 3"
        )
        cache.put("Question 3", "Answer 3", result3)
        
        # LRU item should be gone
        self.assertIsNone(cache.get("Question 1", "Answer 1"))
        self.assertEqual(cache.get("Question 2", "Answer 2"), result2)
        self.assertEqual(cache.get("Question 3", "Answer 3"), result3)
    
    def test_cache_file_operations(self):
        """Test saving and loading cache to/from file."""
        cache = LRUCache(capacity=5)
        
        # Create sample results
        result = RelevanceResult(
            total_score=0.8,
            proximity_score=0.8,
            coverage_score=0.9,
            conciseness_score=0.7,
            logical_flow_score=0.8,
            computation_time=0.1,
            question="Test Question",
            answer="Test Answer"
        )
        
        cache.put("Test Question", "Test Answer", result)
        
        # Save to a temporary file
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_filename = temp_file.name
        
        try:
            # Save and clear
            cache.save_to_file(temp_filename)
            cache.clear()
            self.assertIsNone(cache.get("Test Question", "Test Answer"))
            
            # Load and verify
            cache.load_from_file(temp_filename)
            loaded_result = cache.get("Test Question", "Test Answer")
            self.assertIsNotNone(loaded_result)
            self.assertEqual(loaded_result.total_score, result.total_score)
            self.assertEqual(loaded_result.question, result.question)
            self.assertEqual(loaded_result.answer, result.answer)
        finally:
            # Clean up
            if os.path.exists(temp_filename):
                os.unlink(temp_filename)


if __name__ == '__main__':
    unittest.main()
