def test_in_non_test_module():
    """
    PyTest will recognize this function as a test...
    But will not collect tests from this file (by default)
    """
    print("\nRunning test_in_non_test_module...")
