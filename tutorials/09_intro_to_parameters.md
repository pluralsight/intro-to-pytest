## 9: Intro to Parameters

When we decorate a callable as a Fixture, we can also give it some additional properties, like parameters, allowing us to do parameterized testing - And the `request` plugin (built-in fixture) we've covered previously will come in handy here as well.

In testing, we use parameterization to refactor and "automate" similar tests. Especially in unit testing, you may find yourself in a situation where you want to run the same code, with the same set of assertions (essentially, the same "test") with a number of different inputs and expected outputs.

It's possible to simply include those inputs and outputs (a.k.a. parameters) in our test case... But at the expense of making that test more complicated, and harder to understand when it fails: We'll see a single test case passing or failing, regardless of how many of those cases were valid. And it may not be clear which set of parameters was the problem, without digging into the code, turning on more debugging, etc...

So let's look at a better approach:

[tests/08_params_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/08_params_test.py)

```
pytest -vs tests/08_params_test.py
```

We only have one test case here, with one fixture, but that fixture includes five parameters, "a" through "e". Because our test case depends on a parameterized fixture, PyTest will run it repeatedly, once for each parameter, and it treats each of those as a distinct "test" that can pass or fail independently: We can clearly see how many of those parameters passed or failed, and it even labeled those tests with both the test case name, and the parameter being used.

(This is an interesting philosophical point: When we saw PyTest referring to "nodes" earlier, they seemed to correspond to our test functions... But it's more accurate to say that our test functions are merely "specifications" or "requests" that tell PyTest what to do, and the resulting nodes are the _real_ Tests. This may also make )

PyTest will run our test cases (and their fixture) once per parameter: In our fixture, we're using the `request` plugin to access the current parameter value, as `request.param`, and in this example we're simply yielding that value.

And so our single test case is called five times, once for each parameter value, with that value being passed in as the named argument corresponding to `letters_fixture`.

It doesn't have to be this direct - Our fixture might use the parameter to customize an object, then yield that object to our test. (Or even yield a tuple of values that are derived from the parameter).

(There is also a second parameterized fixture, `mode`, which uses a second keyword argument, `ids`, which allows the names of each parameter label to be overridden. For example, the parameters we need are 1, 2, and 3, but we would prefer to see them labeled as "foo", "bar", and "baz" on the individual tests.)

And this behavior gets really interesting (and powerful) when we consider that fixtures can depend on other fixtures...

### Up Next:

[Parameter-ception!](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/10_parameter-ception.md)