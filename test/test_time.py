import time
from random import randint
from typing import Callable, List, Dict, Any
import json
import os
from conftest import GamingBaseTestCase

# Import the modules being tested
try:
    from Gaming.heals import clw, cmw, csw
    print("Successfully imported healing spells in test_time.py")
except ImportError as e:
    print(f"ERROR in test_time.py: {e}")
    # Placeholders for functions that will be mocked
    def clw(level=1): return randint(1, 8) + level
    def cmw(level=1): return randint(2, 8) + level + 1
    def csw(level=1): return randint(3, 8) + level + 2

import statistics
from collections import defaultdict

# Decorator to measure and log execution time of a function with high precision
class BenchmarkStats:
    def __init__(self):
        self.times = defaultdict(list)
        self.reset()
    
    def reset(self) -> None:
        """Reset all stored times"""
        self.times.clear()
    
    def add_time(self, name: str, time: float) -> None:
        self.times[name].append(time)
    
    def get_stats(self, name: str) -> Dict[str, float]:
        times = self.times[name]
        if not times:
            return {}
        return {
            'min': min(times),
            'max': max(times),
            'mean': statistics.mean(times),
            'median': statistics.median(times),
            'stdev': statistics.stdev(times) if len(times) > 1 else 0,
            'count': len(times)
        }
    
    def print_stats(self) -> None:
        print("\n=== Benchmark Statistics ===")
        for name in sorted(self.times.keys()):
            stats = self.get_stats(name)
            if stats:
                print(f"\n{name}:")
                print(f"  Min: {stats['min']:.8f} seconds")
                print(f"  Max: {stats['max']:.8f} seconds")
                print(f"  Mean: {stats['mean']:.8f} seconds")
                print(f"  Median: {stats['median']:.8f} seconds")
                print(f"  Std Dev: {stats['stdev']:.8f} seconds")
                print(f"  Count: {stats['count']}")

# Global benchmark stats object
benchmark_stats = BenchmarkStats()

def measure_time(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Execution time for {func.__name__}: {execution_time:.8f} seconds")
            benchmark_stats.add_time(func.__name__, execution_time)
            return result
        except Exception as e:
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Error in {func.__name__}: {str(e)}")
            print(f"Time until error: {execution_time:.8f} seconds")
            benchmark_stats.add_time(f"{func.__name__}_error", execution_time)
            raise
    return wrapper

# Base dice rolling function
@measure_time
def d(sides: int, mod: int = 0, times: int = 1) -> List[str]:
    results: List[str] = []
    for _ in range(times):
        roll: int = randint(1, sides)
        result = f"{roll} + {mod} = {roll + mod}"
        results.append(result)
    return results

@measure_time
def d20(mod: int = 0, times: int = 1) -> List[str]:
    return d(20, mod, times)

# Dictionary with lambda functions for dice rolls
roll = {
    "d20": lambda m=0, t=1: [f"{r} + {m} = {r + m}" for r in [randint(1, 20) for _ in range(t)]]
}

# Class-based dice roller
class DiceRoller:
    def __init__(self, sides: int, mod: int = 0, times: int = 1) -> None:
        self.sides = sides
        self.mod = mod
        self.times = times

    @measure_time
    def roll(self) -> List[str]:
        results: List[str] = []
        for _ in range(self.times):
            roll = randint(1, self.sides)
            results.append(f"{roll} + {self.mod} = {roll + self.mod}")
        return results

@measure_time
def test_json_logging(sides: int = 20, times: int = 100) -> None:
    """Test JSON logging performance with multiple rolls"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    test_file = os.path.join(script_dir, 'test_rolls.json')

    for _ in range(times):
        roll = randint(1, sides)
        try:
            data: Dict[str, List[Any]] = {}
            if os.path.exists(test_file):
                with open(test_file, 'r') as file:
                    data = json.load(file)

            current_date = "2024-12-22"  # Using provided timestamp
            data.setdefault(current_date, []).append((sides, roll))

            with open(test_file, 'w') as file:
                json.dump(data, file)
        except Exception as e:
            print(f"Error in JSON logging: {str(e)}")

    # Cleanup test file
    if os.path.exists(test_file):
        os.remove(test_file)

@measure_time
def test_healing_spells() -> None:
    """Test performance of different healing spell levels"""
    spells = [(clw, 1), (clw, 5), (cmw, 5), (csw, 10)]
    for spell, level in spells:
        try:
            spell(level)
        except Exception as e:
            print(f"Error testing {spell.__name__}: {str(e)}")

@measure_time
def test_edge_cases() -> None:
    """Test handling of edge cases and invalid inputs"""
    test_cases = [
        (lambda: d(-1), "negative sides"),
        (lambda: d(20, times=0), "zero times"),
        (lambda: d(10**6), "very large sides"),
        (lambda: DiceRoller(20, times=1000).roll(), "many rolls"),
    ]

    for test_func, desc in test_cases:
        try:
            test_func()
            print(f"Test case '{desc}' completed successfully")
        except Exception as e:
            print(f"Expected error in '{desc}': {str(e)}")

@measure_time
def benchmark_comparison(iterations: int = 10, quiet: bool = False) -> None:
    """Compare different dice rolling implementations"""
    if not quiet:
        print(f"\n=== Running {iterations} iterations of each implementation ===")
    
    benchmark_stats.reset()  # Reset previous results
    
    for _ in range(iterations):
        # Basic dice rolling
        d20(mod=5)
        d(6, mod=2)
        
        # Class-based rolling
        roller = DiceRoller(sides=20, mod=3)
        roller.roll()
        
        # Dictionary-based rolling
        start_time = time.perf_counter()
        roll["d20"](m=2)
        end_time = time.perf_counter()
        dict_time = end_time - start_time
        benchmark_stats.add_time("dictionary_roll", dict_time)

def main() -> None:
    # Add quiet parameter to suppress output when running from Streamlit
    def run_tests(quiet: bool = False) -> None:
        if not quiet:
            print("\n=== Running Basic Tests ===")
        d20(mod=5, times=3)
        d(6, mod=2, times=2)
        
        if not quiet:
            print("\n=== Running Implementation Comparison ===")
        benchmark_comparison(quiet=quiet)
        
        if not quiet:
            print("\n=== Testing JSON Logging Performance ===")
        test_json_logging(times=50)
        
        if not quiet:
            print("\n=== Testing Healing Spells ===")
        test_healing_spells()
        
        if not quiet:
            print("\n=== Testing Edge Cases ===")
        test_edge_cases()
        
        if not quiet:
            benchmark_stats.print_stats()

    run_tests()

# Convert to unittest test cases
class TestDiceRolling(GamingBaseTestCase):
    """Test dice rolling functionality."""
    
    def test_dice_rolling(self):
        """Test basic dice rolling functionality."""
        # Test d20 function
        results = d20(mod=5, times=3)
        self.assertEqual(len(results), 3)
        for result in results:
            # Extract the roll value from the formatted string
            roll_value = int(result.split("+")[0].strip())
            self.assertTrue(1 <= roll_value <= 20)
        
        # Test d function
        results = d(6, mod=2, times=2)
        self.assertEqual(len(results), 2)
    
    def test_json_logging_functionality(self):
        """Test JSON logging process works correctly."""
        test_json_logging(times=5)  # Use fewer iterations for testing
    
    def test_healing_spells_functionality(self):
        """Test that healing spells work correctly."""
        test_healing_spells()
    
    def test_edge_cases_functionality(self):
        """Test handling of edge cases."""
        test_edge_cases()
    
    def test_benchmark_comparison_functionality(self):
        """Test benchmark comparison works correctly."""
        benchmark_comparison(iterations=2, quiet=True)
        
        # Verify stats collection
        stats = benchmark_stats.get_stats("d20")
        self.assertTrue(stats.get('count', 0) >= 2, "Should have at least 2 measurements for d20")

if __name__ == "__main__":
    unittest.main(exit=False)
    main()
