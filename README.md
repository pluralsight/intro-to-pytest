# intro-to-pytest
An introduction to PyTest with lots of simple, hackable examples (currently Python 2.7 compatible).

These examples are intended to be self-explanatory to a Python developer, with minimal setup - In addition to Python 2.7, you'll also need `pytest` and the `pytest-mock` plugin installed to use all these examples, which you can install by running:

```
pip install -r requirements.txt
```

In this repo (optionally, inside a virtualenv or other environment wrapper, to keep this from affecting your local Python libraries.)

Once you've got all the requirements in place, you should be able to simply run

```
pytest
```

In the repo folder, and see 35 items being collected, and 35 tests passing, in less than a second.

Congratulations! You're ready to get started.

The recommended approach is to read each example file, then run it directly with pytest, with the `v` flag (so that each Test Case is listed by name) and the `s` flag, so that we can see the raw output from the Tests, which will help explain how each example is working. (Though we can shorten this to `-vs`.)

## 0: The Empty Test

The first test is pretty boring: It is a module with "test" in the name, containing a callable (in this case, a plain old function) which also has "test" in the name, that doesn't really do anything.
```
pytest -vs 00_empty_test.py
```
This is about as minimal as a PyTest test can get - It doesn't even assert anything! But since it also doesn't raise any exceptions, it passes. Among other things, this demonstrates that we can use PyTest tests to simply "exercise" our code, even if we don't assert anything specific about the behavior (beyond it not being "broken").

This is also an example of how PyTest decides what is and is not a test: By default, it looks for callables whose names begin with "test". And when we ran it without any arguments, it searched for tests in all the modules (python files) whose name contained "test", by default. (But all these behaviors can be changed, if you want...)

## 1: A Basic Test

Finally, a proper test that actually asserts something! It's not much, but it's a start.
```
pytest -vs 01_basic_test.py
```
Pytest doesn't come with a ton of fancy assertion methods, because it's doing a lot of work behind the scenes to make the humble `assert` operator more informative.

For example, try setting `y` to 0 to make this test fail, and run it again - Instead of just raising "AssertionError", PyTest will show you the line where the failure occurred, in context with the rest of your code, and even unpack the two variables for you. Nifty!

## 2: Special Assertions

Not everything can be expressed as a simple assertion, though, and so PyTest does come with a few extra functions:
```
pytest 02_special_assertions_test.py
```
Two of these tests raise exceptions on purpose - we can use the `pytest.raises` context manager to both assert that they happen (and handle that exception, so it doesn't show up as a failure). For example, if you change line 9 to `print 1/1`, PyTest will now fail the test, since the expected Exception didn't happen. (and it will explain this in detail in the console!)

In `test_keyerror_details`, we also name the exception using `as`, so that we can refer to it after the `pytest.raises` block - we can inspect it in more detail, or even `assert` that it has qualities we're expecting. Very helpful when you want to test exception-raising behavior!

Finally, in `test_approximate_matches`, we use `pytest.approx` to help assert that our two values are "approximately" equal, even it's not exact due to fun with floating point math. (We can also adjust how "close" we want the match to be before it fails the test - For more details, check out the [pytest.approx documentation](https://docs.pytest.org/en/latest/reference.html#pytest-approx).)

## 3: Fixtures

Fixtures are a core part of what makes PyTest really powerful - They fill the same role as `setUp()` and `tearDown()` methods in the old xUnit style `unittest.TestCase` tests, but can also go far beyond that. And you don't even need to create Classes to use them!

We create our `simple_fixture` simply by defining a function with the `pytest.fixture` decorator - This example just prints some text, but you could imagine it doing something more interesting, like setting up some test data.

Then we make another test, but this time we give it a single argument whose name matches the name of our `simple_fixture`, above.
```
pytest -vs 03_simple_fixture_test.py
```
What the heck just happened?

The short answer is "dependency injection", but the longer answer is that, while PyTest is running all of our tests, it's also attempting to "fill in" their arguments using fixtures with matching names. And as we can see in the detailed output, it is essentially running the fixture first, and then our test. But how can we make our fixture more directly useful to our test?

## 4: Fixture Returns

Beyond simply running some code, a fixture can also return data, just like a regular function...
```
pytest -vs 03_simple_fixture_test.py
```
The interesting part is that when PyTest runs our test, it not only runs the fixture function first, it also takes the output of our fixture (in this case, `one_fixture`), and passes it into the our test function as the `one_fixture` argument!

So we can make assertions about what our fixture is returning, or use it in any other way we'd like during our test. (and since PyTest runs our fixture for each test, we can guarantee that each test is getting a "fresh" copy of whatever it is that our fixture returns... Assuming it's not returning a shared object.)

This helps take care of "set up" style scenarios, but what about "teardown"?

## 5: Yield Fixtures

Here's a more complicated fixture that uses the `yield` keyword - You may be more accustomed to seeing that used in generator functions, which are more commonly called repeatedly (or "iterated") to deliver their values.

If this seems confusing (or if you aren't familiar with `yield`), don't worry: The important thing to know is that it's a lot like `return`, except for one interesting difference...
```
pytest -vs 05_yield_fixture_test.py 
```
Like last time, our fixture ran before the test case... Up until the point that we called `yield`. Then the test ran... And then, _after_ the test finished, our fixture picked up where it left off, and ran the rest of the code (after the `yield` call).

This allows us to do both pre-test and post-test actions, with a minimum of code! But there are a few things to keep in mind:
 * Our fixtures shouldn't yield more than once. (PyTest enforces this - try adding a second yield and see what happens!)

 * If something goes wrong inside our fixture, such that an exception is thrown before we call `yield`, we'll never get to the post-`yield` code! While this is unlikely in a simple fixture, we should use more advanced features if there's a chance our fixture might fail, and we absolutely, positively need our "teardown" code to run...
