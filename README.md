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

(PyTest will list module file that it located tests inside of, and then a period for each test that passed, or other symbols for tests that failed, were skipped, etc...)

But if you're seeing all that, then congratulations! You're ready to get started.

The recommended approach is to read each example file, then run it directly with pytest, with the `v` flag (so that each Test Case is listed by name) and the `s` flag, so that we can see the raw output from the Tests, which will help explain how each example is working. (Though we can shorten this to `-vs`.)

## 0: The Empty Test

The first test is pretty boring: It is a module with "test" in the name, containing a callable (in this case, a plain old function) which also has "test" in the name, that doesn't really do anything.

[tests/00_empty_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/00_empty_test.py)

```
pytest -vs tests/00_empty_test.py
```
This is about as minimal as a PyTest test can get - It doesn't even assert anything! But since it also doesn't raise any exceptions, it passes. Among other things, this demonstrates that we can use PyTest tests to simply "exercise" our code, even if we don't assert anything specific about the behavior (beyond it not being "broken").

This is also an example of how PyTest decides what is and is not a test: By default, it looks for callables whose names begin with "test". And when we ran it without any arguments, it searched for tests in all the modules (python files) whose name contained "test", by default. (But all these behaviors can be changed, if you want...)

## 1: A Basic Test

Finally, a proper test that actually asserts something! It's not much, but it's a start.

[tests/01_basic_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/01_basic_test.py)

```
pytest -vs tests/01_basic_test.py
```
Pytest doesn't come with a ton of fancy assertion methods, because it's doing a lot of work behind the scenes to make the humble `assert` operator more informative.

For example, try setting `y` to 0 to make this test fail, and run it again - Instead of just raising "AssertionError", PyTest will show you the line where the failure occurred, in context with the rest of your code, and even unpack the two variables for you. Nifty!

## 2: Special Assertions

Not everything can be expressed as a simple assertion, though, and so PyTest does come with a few extra functions:

[tests/02_special_assertions_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/02_special_assertions_test.py)

```
pytest 02_special_assertions_test.py
```
Two of these tests raise exceptions on purpose - we can use the `pytest.raises` context manager to both assert that they happen (and handle that exception, so it doesn't show up as a failure). For example, if you change line 9 to `print 1/1`, PyTest will now fail the test, since the expected Exception didn't happen. (and it will explain this in detail in the console!)

In `test_keyerror_details`, we also name the exception using `as`, so that we can refer to it after the `pytest.raises` block - we can inspect it in more detail, or even `assert` that it has qualities we're expecting. Very helpful when you want to test exception-raising behavior!

Finally, in `test_approximate_matches`, we use `pytest.approx` to help assert that our two values are "approximately" equal, even it's not exact due to fun with floating point math. (We can also adjust how "close" we want the match to be before it fails the test - For more details, check out the [pytest.approx documentation](https://docs.pytest.org/en/latest/reference.html#pytest-approx).)

### Review

* PyTest cases can be as simple as a function whose name starts with "test", in a file whose name starts with "test".

    * (PyTest will also find and run `unittest` style tests, and the test-finding behavior is [extremely configurable](https://docs.pytest.org/en/latest/goodpractices.html#conventions-for-python-test-discovery).)

* A PyTest case that doesn't that doesn't raise any unhandled exceptions (or failing assertions) will pass.

    * (PyTest can be used to "exercise" code and detect errors, even without any assertions!)

* PyTest uses basic Python assertions, but can introspect into your code and "unpack" a lot of useful info about why the assertion failed.

    * (If your PyTest case calls other code that makes assertions, they will be honored as well; However, in that case, those "external" assertions may need to provide their own detailed failure messages.)

* PyTest provides features for "expecting" Exceptions, and matching approximately similar values, similiar to [unittest.TestCase](https://docs.python.org/2/library/unittest.html#basic-example).

## 3: Fixtures

Fixtures are a core part of what makes PyTest really powerful - They fill the same role as `setUp()` and `tearDown()` methods in the old xUnit style `unittest.TestCase` tests, but can also go far beyond that. And you don't even need to create Classes to use them!

We create our `simple_fixture` simply by defining a function with the `pytest.fixture` decorator - This example just prints some text, but you could imagine it doing something more interesting, like setting up some test data.

Then we make another test, but this time we give it a single argument whose name matches the name of our `simple_fixture`, above.

[tests/03_simple_fixture_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/03_simple_fixture_test.py)

```
pytest -vs tests/03_simple_fixture_test.py
```
What the heck just happened?

The short answer is "dependency injection", but the longer answer is that, when PyTest runs all of our tests, it's also attempting to "fill in" their named arguments using fixtures with matching names. And as we can see in the detailed output, it is essentially running the fixture first, and then our test.

Another way to express this is that PyTest test case arguments indicate "dependencies" on fixtures. (If you add an argument whose name doesn't correspond to a Fixture, PyTest will get upset - For example, try changing the argument name to `simple_fixtures` on one of the tests.)

But how can we make our fixture more directly useful to our test?

## 4: Fixture Returns

Beyond simply running some code, a fixture can also return data, just like a regular function...

[tests/04_fixture_returns_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/04_fixture_returns_test.py)

```
pytest -vs tests/04_fixture_returns_test.py
```
The interesting part is that when PyTest runs our test, it not only runs the fixture function first, it also takes the output of our fixture (in this case, the return value of `one_fixture`), and passes it into our test function as the `one_fixture` argument!

So we can make assertions about what our fixture is returning, or use it in any other way we'd like during our test. (And by default, PyTest runs our fixtures for each test that depends on them, so we are guaranteed that each test is getting a "fresh" copy of whatever it is that our fixture returns.)

This helps take care of test "setup" scenarios, but what about "teardown"?

## 5: Yield Fixtures

Here's a more complicated fixture that uses the `yield` keyword - You may be more accustomed to seeing it used in generator functions, which are typically called repeatedly (e.g. iterated) to deliver their values.

If this seems confusing (or if you aren't familiar with `yield`), don't worry: The important thing to know is that it's a lot like `return`, except for one interesting difference...

[tests/05_yield_fixture_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/05_yield_fixture_test.py)

```
pytest -vs tests/05_yield_fixture_test.py
```

Like last time, our fixture ran before the test case... Up until the point that we called `yield`. Then the test was run, receiving the "yielded" value as an argument... And then, _after_ the test finished, our fixture picked up where it left off, and ran the rest of the code (after the `yield` call).

This allows us to do both pre-test and post-test actions, with a minimum of code! But there are a few things to keep in mind:

 * Unlike normal generators, our fixtures shouldn't yield more than once. (PyTest enforces this - try adding a second yield and see what happens!)

 * If something goes wrong inside our fixture, such that an unhandled exception is thrown before we call `yield`, we'll never get to the post-`yield` code... But we also won't actually run the test case that depends on it. (But don't worry: We'll cover some more thorough cleanup options later on.)

## 6: The "request" fixture

Fixtures are very powerful, not only because PyTest can run them automatically, but because they can be "aware" of the context in which they're being used.

(And also, as we're about to see, Fixtures can depend on other Fixtures, allowing for some really interesting behavior...)

In this example, we write a fixture which leverages the built-in `request` fixture (aka a "Plugin", a standard fixture that is globally available to PyTest tests) to learn more about how it's being called:

[tests/06_request_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/06_request_test.py)

```
pytest -vs tests/06_request_test.py
```

Among other things, our fixture can tell that it's being invoked at function-level scope (e.g. it is being referenced directly by a test case function), it knows which "node" it's currently running on (in a dependency tree sense: It knows which test case is calling it), and it knows which Module it's being run in, which in this case is the `06_request_test.py` file.

In addition to providing context, the `request` fixture can also be used to change PyTest's behavior as it runs our tests:

## 7: Adding "finalizer" callbacks

Sometimes we want to run a "cleanup" function after testing is complete: We covered a very easy way to do this above in the 05_yield_fixture_test.py , but noted that it's not the safest option, if something goes wrong inside our Fixture...

We can also use the `request` plugin (a built-in global fixture) to add a "finalizer", another function which is guaranteed to be called after this fixture (and the test(s) that depend on it) are run. Even in the worst case scenario, where our fixture raises an unhandled exception (before the test case gets run):

[tests/07_request_finalizer_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/07_request_finalizer_test.py)

```
pytest -vs tests/07_request_finalizer_test.py
```

As with our yield example, we can see that our fixture runs first (including a "risky" function call), followed by our test case, and finally our safe_cleanup function. One advantage of this approach is that we can re-use a shared cleanup function, but the big one is that even if our Fixture itself critically fails, our cleanup function still runs!

To try this out, uncomment line 11 in `07_request_finalizer_test.py` (e.g. the commented-out "raise Exception" call), and re-run the test.

That "risky" function didn't work out - it derailed our Fixture, and our test case never even ran! But despite all that, our `safe_cleanup` function still got called, which could be a really important distinction in a real test!

## 8: Testing with Parameters

When we decorate a callable as a Fixture, we can also give it some additional properties, like parameters, allowing us to do parameterized testing - And the `request` plugin we've covered above will come in handy here as well.

In testing, we use parameterization to refactor and "automate" similar tests. Especially in unit testing, you may find yourself in a situation where you want to run the same code, with the same set of assertions (essentially, the same "test") with a lot of different inputs and expected outputs.

It's possible to simply include those inputs and outputs (a.k.a. parameters) in our test case... But at the expense of making that test more complicated, and harder to understand when it fails. (We'll see a single test case failing, regardless of whether one, or some, or all of the parameters inside of it have failed. And it may not be clear which set of parameters was the problem, without digging into the code, turning on more debugging, etc.)

So let's look at a better approach:

[tests/08_params_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/08_params_test.py)

```
pytest -vs tests/08_params_test.py
```

We only have one test case here, with one fixture, but that fixture included five parameters, "a" through "e". Because our test case depends on a parameterized fixture, PyTest will run it repeatedly, once for each parameter, and it treats each of those as a distinct "test" that can pass or fail independently: We can clearly see how many of those parameters passed or failed, and it even labeled those tests with both the test case name, and the parameter being used.

PyTest will run our test cases (and their fixture) once per parameter: In our fixture, we're using the `request` plugin to access the current parameter value, as `request.param`, and in this example we're simply yielding that value.

And so our single test case is called five times, once for each parameter value, with that value being passed in as the named argument corresponding to `letters_fixture`.

It doesn't have to be this direct - Our fixture might use the parameter to customize an object, then yield that object to our test. (Or even yield a tuple of values that are derived from the parameter).

And this behavior gets really interesting (and powerful) when we consider that fixtures can depend on other fixtures...

## 9: Parameter-ception!

Python includes a great set of Iteration Tools that make it easy to generate all of the combinations and permutations of sets of data - And while the exact distinctions between a combination and a permutation aren't really in the scope of this guide, we're about to see an interesting example of this kind of behavior using multiple parameterized fixtures.

It's a lot easier to demonstrate than explain, so let's start with that: Here's another single test case, which depends on a fixture (which depends on a second fixture): And it's worth noting that both of those fixtures each have their own set of four parameters:

[tests/09_params-ception_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/09_params-ception_test.py)

```
pytest -vs tests/09_params-ception_test.py
```

How did that turn into 16 tests? The short answer is that we're experiencing the [Cartesian Product](https://en.wikipedia.org/wiki/Cartesian_product) of our fixture parameters.

But the less set-theory-intensive answer is that our test case depends on `letters_fixture`, which causes PyTest to run it once for each letter parameter... And it depends on `numbers_fixture`, which _also_ wants to repeat each call for each of its number parameters.

This is evident from the order in which the tests are run, and (thanks to PyTest!) from the labels of those tests: We can see that our test is being run first with our `letters_fixture`, and each of it's parameters (starting with "a"), and those runs are being further "multiplied" by the `letters_fixture`, which is ensuring that those tests are each being run with it's own parameters (starting with "1").

As a result, our single test case gets run a total of sixteen times, once for each combination of the four numbers and four letters (4 x 4 = 16).

While we _could_ just make a single fixture that yielded each combination as a parameter ('a1', 'a2', 'a3', etc.), maintaining them as separate fixtures makes maintenance a lot easier. These individual fixtures can be reused and composed across different tests, allowing for a lot more flexibility. And imagine if you had a fixture containing 198 unique combinations of letters and numbers, and decided you needed to drop all the sets with vowels, or all the sets containing the number 3 - Wouldn't it be easier (and more readble) to operate on the smaller subsets that make up that data?

But there's an even more elegant way to solve that particular problem, taking advantage of the fact that fixtures can, in turn, depend on other fixtures...

## 10: Advanced Parameter-ception!

Let's try that again, but with our test case depending on only one fixture (which, in turn, depends on a second fixture):

[tests/10_advanced_params-ception_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/10_advanced_params-ception_test.py)


```
pytest -vs tests/10_advanced_params-ception_test.py
```

The end result is... almost identical, even though the approach is different.

Since our parameterized `coordinate_fixture` depends on another parameterized fixture, `numbers_fixture`, we still get the Cartesian Product of both set of parameters, even though the test case itself only depends on one of them.

And this relationship is still reflected in the names PyTest assigns to the tests being run: the letter from the "inner" fixture appears first, followed by the digit from the "outer" fixture it depends on.

This can be a deceptively simple but powerful feature - You can essentially create "higher order fixtures" that take each other as dependencies (and arguments), using extra layers of fixtures to further customize behavior, all without touching the test case itself.

For example, try uncommenting the commented section of code (lines 19 through 22) to enable a clever piece of filtering logic using the `pytest.skip` function, and run the test again...

Now the `coordinate_fixture` applies some extra logic about which parameter combinations should be used, without affecting `numbers_fixture`, or the test case. This also demonstrates that PyTest responds to `skip` at any time - even if it's called inside of a fixture, before we've even gotten into a test case, allowing us to avoid any undesirable combinations.

(In this example, we've added our filtering logic to one of our parameterized fixtures... But we could further abstract this into a `letters_fixture`and `numbers_fixture` which yield parameters, and a third, more purpose-specific `coordinates_fixture` that depends on those, adds the filtering logic, and has no parameters of its own, with the test case depending on it only.)

## 11: Using pytest.mark

PyTest includes a "mark" decorator, which can be used to tag tests and other objects for later reference (and for a more localized type of parameterization, though we'll get to that later).

Here are some tests with marks already applied:

[tests/11_mark_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/11_mark_test.py)

```
pytest -vs tests/11_mark_test.py
```

We ran three tests... Note that even though we marked `asserty_callable_thing` as if it was a test, PyTest still didn't actually run it - `mark` tags are only processed on callables that PyTest recognizes as tests (and `asserty_callable_thing`'s name does not start with "test"!)

Admittedly, this code isn't all that interesting on its own. But the real value of `mark` is best demonstrated within the `pytest` runner itself:

We can tell PyTest to run a specific named test (a.k.a "node") by name, by appending it to our module path with a "::" separator. For example:

```
pytest -vs tests/11_mark_test.py::test_fake_query
```

(PyTest only collected and ran the named `test_fake_query` case, instead of all the available test cases in the file.)

We can also do partial matches on node name, for example, running all tests with "query" in the name, using the `-k` operator:

```
pytest -v -k query
```

(PyTest only matches two of our three test cases, based on name.)

Or we could use a simple `-k` expression to run all tests with "stats" or "join" in their names:

```
pytest -v -k "stats or join"
```

Or use `-m` to run all tests marked with the "db" tag:

```
pytest -v -m db
```

Or a `-m` expression to target tests marked with "db", but *not* with the "slow" tag:

```
pytest -v -m "db and not slow"
```

---

(More documentation coming soon...)

---

## 12: Special marks

[tests/12_special_marks.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/12_special_marks.py)

```
pytest -vs tests/12_special_marks.py
```

https://docs.pytest.org/en/latest/skipping.html

## 13: Mark-based "Parametrization"

[tests/13_mark_parametrization.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/13_mark_parametrization.py)

```
pytest -vs tests/13_mark_parametrization.py
```

## 14: PyTesting with Classes

[tests/14_class_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/14_class_test.py)

```
pytest -vs tests/14_class_test.py
```

## 15: Advanced Class usage

[tests/15_advanced_class_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/15_advanced_class_test.py)

```
pytest -vs tests/15_advanced_class_test.py
```

## 16: Fixture Scoping

[tests/16_scoped_and_meta_fixtures_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/16_scoped_and_meta_fixtures_test.py)

```
pytest -vs tests/16_scoped_and_meta_fixtures_test.py
```

## 17: Mocking with pytest-mock

[tests/17_mock_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/17_mock_test.py)

```
pytest -vs tests/17_mock_test.py
```

## 18: Re-Usable mock fixtures

[tests/18_re_usable_mock_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/18_re_usable_mock_test.py)

```
pytest -vs tests/18_re_usable_mock_test.py
```
