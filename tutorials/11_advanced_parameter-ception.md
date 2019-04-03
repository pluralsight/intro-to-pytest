## 11: Advanced Parameter-ception!

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

Now the `coordinate_fixture` applies some extra logic about which parameter combinations should be used, without affecting `numbers_fixture`, or the test case.

This also demonstrates that PyTest responds to `skip` at any time - even if it's called inside of a fixture, before we've even gotten into a test case, allowing us to avoid any undesirable combinations. This is an other hint to how PyTest works, internally: Our test cases are merely specifications for the tests that PyTest will be running, and we can conditionally skip a test at any point before it completes (thus passing or failing).

In this example, we've added our filtering logic to one of our parameterized fixtures... But we could further abstract this into a `letters_fixture`and `numbers_fixture` which yield parameters, and a third, more purpose-specific `coordinates_fixture` that depends on those, adds the filtering logic, and has no parameters of its own, with the test case depending on it only. If we expect to use our two parameterized fixtures separately, that might be an even better way of organizing them.

Finally, this can also serve as an example of how fixture dependencies are not entirely unlike an `import` - If you add the `number_fixture` as an argument for (and dependency of) `test_advanced_fixtureception`, what do you expect might go wrong?

While this seems like it could be problematic - The test case now depends on `number_fixture` twice, both directly with a named argument, and indirectly through `coordinates_fixture` - PyTest is surprisingly cool about it.

You might expect this to result in `number_fixture` being invoked twice, doubling our resulting tests, or even multiplying them by another copy of our extra parameter... But PyTest recognizes that both dependencies refer to the same fixture, and that fixture (by default) is run once per test case, and so we get the same results as if our `number_fixture` was only referred to once.

### Up Next:

[Reviewing Fixtures](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/12_reviewing_fixtures.md)
