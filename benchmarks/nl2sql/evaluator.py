"""NL2SQL benchmark evaluation."""

import json
from typing import List, Dict
from dataclasses import dataclass


@dataclass
class NL2SQLTestCase:
    """NL2SQL test case."""
    
    id: str
    question: str
    expected_sql: str
    description: str
    difficulty: str  # easy, medium, hard


class NL2SQLBenchmark:
    """NL2SQL benchmark evaluator."""
    
    def __init__(self):
        self.test_cases: List[NL2SQLTestCase] = []
    
    def load_test_cases(self, filepath: str) -> None:
        """Load test cases from JSON file."""
        with open(filepath, "r") as f:
            data = json.load(f)
            for item in data:
                self.test_cases.append(
                    NL2SQLTestCase(
                        id=item["id"],
                        question=item["question"],
                        expected_sql=item["expected_sql"],
                        description=item["description"],
                        difficulty=item["difficulty"],
                    )
                )
    
    def evaluate(self, model_fn, test_case: NL2SQLTestCase) -> Dict:
        """Evaluate a single test case."""
        predicted_sql = model_fn(test_case.question)
        
        # Simple exact match (can be enhanced with SQL similarity)
        is_correct = predicted_sql.strip().lower() == test_case.expected_sql.strip().lower()
        
        return {
            "test_case_id": test_case.id,
            "question": test_case.question,
            "expected": test_case.expected_sql,
            "predicted": predicted_sql,
            "correct": is_correct,
            "difficulty": test_case.difficulty,
        }
    
    def run_benchmark(self, model_fn) -> Dict:
        """Run full benchmark."""
        results = []
        for test_case in self.test_cases:
            result = self.evaluate(model_fn, test_case)
            results.append(result)
        
        # Calculate metrics
        total = len(results)
        correct = sum(1 for r in results if r["correct"])
        
        by_difficulty = {}
        for r in results:
            diff = r["difficulty"]
            if diff not in by_difficulty:
                by_difficulty[diff] = {"total": 0, "correct": 0}
            by_difficulty[diff]["total"] += 1
            if r["correct"]:
                by_difficulty[diff]["correct"] += 1
        
        return {
            "total_cases": total,
            "correct": correct,
            "accuracy": correct / total if total > 0 else 0,
            "by_difficulty": by_difficulty,
            "results": results,
        }
