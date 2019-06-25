## 2: Special Assertions

Not everything can be expressed as a simple assertion, though, but fear not - PyTest provides:

[tests/02_special_assertions_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/02_special_assertions_test.py)

```
pytest 02_special_assertions_test.py
```
Two of these tests raise exceptions on purpose - we can use the `pytest.raises` context manager to both assert that they happen (and handle that exception, so it doesn't show up as a failure). For example, if you change line 9 to `print 1/1`, PyTest will now fail the test, since the expected Exception didn't happen. (and it will explain this in detail in the console!)

In `test_keyerror_details`, we also assign the exception to a variable using `as`, so that we can refer to it after the `pytest.raises` block - we can inspect it in more detail, or even `assert` that it has qualities we're expecting. Very helpful when you want to test for specific exception-raising behavior!

Finally, in `test_approximate_matches`, we use `pytest.approx` to help assert that our two values are "approximately" equal, even it's not exact due to fun with floating point math. (We can also adjust how "close" we want the match to be before it fails the test - For more details, check out the [pytest.approx documentation](https://docs.pytest.org/en/latest/reference.html#pytest-approx).)

### Up Next:

[Review of the Basics](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/03_reviewing_the_basics.md)
