## 5: Fixture Returns

Beyond simply printing a message, a fixture can also return data, just like a regular function:

[tests/04_fixture_returns_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/04_fixture_returns_test.py)

```
pytest -vs tests/04_fixture_returns_test.py
```

The interesting part is that when PyTest runs our test, it not only runs the fixture function first, it also captures the output (in this case, the return value of `one_fixture`), and passes it into our test function as the `one_fixture` argument!

So we can make assertions about what our fixture is returning, or use it in any other way we'd like during our test. (And by default, PyTest runs our fixtures for each test that depends on them, so we are guaranteed that each test is getting a "fresh" copy of whatever it is that our fixture returns: It doesn't matter for fixtures that return static data, but imagine a fixture that returns a mutable data structure, that gets altered during a test?)

This helps take care of test case "setUp" scenarios, but what about "tearDown"? (If you aren't familiar with xUnit, the "setUp" method is run before each test, and the "tearDown" method is called afterwards, and typically used to clean up after a test.)

### Up Next:

[Yield Fixtures](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/06_yield_fixtures.md)