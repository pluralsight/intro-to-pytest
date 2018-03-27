import pytest


@pytest.mark.db
def test_fake_query():
    """
    pytest.mark can be used to "tag" tests for later reference
    """
    assert True


@pytest.mark.db
@pytest.mark.slow
def test_fake_expensive_join():
    assert True


@pytest.mark.db
def asserty_callable_thing():
    """
    But tagging a function alone won't turn it into a test
    """
    print "This isn't even a test!"
    assert True


"""
Tags can be used to target (or omit) tests in the runner:

# Run all tests in this module (verbosely)
pytest -v mark_test.py

# Run a specific test by Node name:
pytest -v mark_test.py::test_fake_query

# Run all tests with "query" in their names
pytest -v -k query

# Run all tests with "query" or "join" in their names
pytest -v -k "query or join"

# Run all tests marked with "db"
pytest -v -m db

# Run all tests marked with "db", but not with "slow"
pytest -v -m "db and not slow"
"""
