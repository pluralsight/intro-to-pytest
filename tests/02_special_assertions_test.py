import pytest


def test_div_zero_exception():
    """
    pytest.raises can assert that exceptions are raised (catching them)
    """
    with pytest.raises(ZeroDivisionError):
        print 1/0


def test_keyerror_details():
    """
    The raised exception can be referenced, and further inspected (or asserted)
    """
    my_map = {'foo': 'bar'}

    with pytest.raises(KeyError) as ke:
        print my_map['baz']
    print "\n(Raised KeyError: {})".format(ke)


def test_approximate_matches():
    """
    pytest.approx can be used to assert "approximate" numerical equality
    (compare UnitTest's "assertAlmostEqual")
    """
    assert (0.1 + 0.2) == pytest.approx(0.3)
