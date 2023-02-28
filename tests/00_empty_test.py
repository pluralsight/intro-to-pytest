import random

def test_empty():
    """
    PyTest tests are callables whose names start with "test"
    (by default)

    It looks for them in modules whose name starts with "test_" or ends with "_test"
    (by default)
    """
    pass


def empty_test():
    """
    My name doesn't start with "test", so I won't get run.
    (by default ;-)
    """
    pass

def test_pass_fifty_percent():
    assert(random.random() < 0.5)
