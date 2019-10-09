### 3: Reviewing the Basics

* PyTest cases can be as simple as a function whose name starts with "test", in a file whose name starts with "test".

    * (PyTest will also find and run xUnit-style tests created using the standard `unittest` module, allowing you to start using PyTest alongside existing, legacy tests.
    
    * The test-finding behavior has reasonable defaults, but is [extremely configurable!](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery).)

* A PyTest case will pass if:
    * It's assertions are True
    * (Or it doesn't have any assertions!)
    * And if it doesn't raise any unhandled Exceptions.

* (PyTest can be used to "exercise" code, and will report errors, even without any actual assertions!)

* PyTest uses the basic Python `assert` keyword, but will introspect into your code and "unpack" useful info about why the assertion failed.

    * (If your PyTest case calls other code that makes assertions, they will be honored as well (in the sense that any failed assertion resulting from your test will cause the test to be reported as "failed".)
    
    * However, assertions that aren't local (e.g. not located inside your test function) won't be "unpacked" and explained in detail. If your tests call other code that performs assertions, you should make those "external" assertions as clear as possible: Try to limit each assert to one specific check, and provide an error message as a second argument, so that the failure is easier to understand.

        * For example, if you wanted to assert that x is greater than zero, and divisible by 2, in a function that is called by one of your test cases (but is not inside a python test case function!) consider something like:

        ```
        assert (x > 0), "X should be > 0, but is {}".format(x)
        assert not (x % 2), "X should be divisible by 2, but is {}".format(x)
        ```

        (But if possible, do all your assertions inside test cases, so that PyTest can document their failure reasons and context for you!)

* PyTest provides features for "expecting" Exceptions, and matching approximately similar values, similiar to [unittest.TestCase](https://docs.python.org/2/library/unittest.html#basic-example):

    * [pytest.raises](https://docs.pytest.org/en/latest/reference.html#pytest-raises)

    * [pytest.approx](https://docs.pytest.org/en/latest/reference.html#pytest-approx)

### Up Next:

[Intro to Fixtures](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/04_intro_to_fixtures.md)
