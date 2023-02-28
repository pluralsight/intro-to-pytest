from other_code.services import DATA_SET_A, DATA_SET_B, DATA_SET_C
import random


def test_example():
    """
    But really, test cases should be callables containing assertions:
    """
    print("\nRunning test_example...")
    assert DATA_SET_A == DATA_SET_B

def test_pass_seventy_percent():
    assert(random.random() < 0.7)
