## 4: Fixtures

Fixtures are a core part of what makes PyTest really powerful - They can fill the same role as `setUp()` and `tearDown()` methods in the old xUnit style `unittest.TestCase` tests, but can also go far beyond that. And you don't even need to create Classes to use them!

We create our `simple_fixture` simply by defining a function with the `pytest.fixture` decorator - This example just prints some text, but you could imagine it doing something more interesting, like setting up test data, or initializing objects to be tested...

Then we make another test, but this time we give it a single argument whose name matches the name of our `simple_fixture`, above.

PyTest is responsible for "calling" our test functions, and deciding if they were successful, but what will it do if a test function has a named argument?

[tests/03_simple_fixture_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/03_simple_fixture_test.py)

```
pytest -vs tests/03_simple_fixture_test.py
```

Now, you might be asking, "What the heck just happened?"

The short answer is "dependency injection", but the longer answer is that, when PyTest calls our test functions, it's also attempting to "fill in" their named arguments using `fixtures` with matching names. And as we can see in the detailed output, it is essentially calling our fixture function first, and then our test.

Another way to express this is that PyTest test case arguments indicate "dependencies" on fixtures, which PyTest will prepare in advance. And it is falling the fixture function multiple times - By default, it calls the fixture function once for each test case that depends on it. (This behavior is configurable as well! But we'll get to that later.) 

(You might be wondering what happens if you add an argument whose name doesn't correspond to a Fixture: The answer is "nothing good". For example, try changing the argument name to `not_a_fixture` on one of the tests, and run them again...)

So far, our fixture hasn't done much for us: Let's change that.

### Up Next:

[Fixture Return Values](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/05_fixture_return_values.md)