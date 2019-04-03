import pytest


@pytest.mark.db
def test_fake_query():
    """
    pytest.mark can be used to "tag" tests for later reference
    """
    assert True


@pytest.mark.slow
def test_fake_stats_function():
    assert True


@pytest.mark.db
@pytest.mark.slow
def test_fake_multi_join_query():
    """
    Test cases can have multiple marks assigned
    """
    assert True


@pytest.mark.db
def asserty_callable_thing():
    """
    PyTest still only runs "tests", not just any callabe with a mark
    """
    print("This isn't even a test! And it fails!")
    assert False


"""
Tags can be used to target (or omit) tests in the runner:

# Run all three tests in this module (verbosely)
pytest -v 10_mark_test.py

# Run one specific test by Node name:
pytest -v 10_mark_test.py::test_fake_query

# Run all tests with "query" in their names
pytest -v -k query

# Run all tests with "stats" or "join" in their names
pytest -v -k "stats or join"

# Run all tests marked with "db"
pytest -v -m db

# Run all tests marked with "db", but not with "slow"
pytest -v -m "db and not slow"
"""
