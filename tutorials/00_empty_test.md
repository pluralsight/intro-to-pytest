## 0: An Empty Test

The first test is pretty boring: It is a module with "test" in the name, containing a callable (in this case, a plain old function) which also has "test" in the name, that doesn't really do anything.

[tests/00_empty_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/00_empty_test.py)

```
pytest -vs tests/00_empty_test.py
```

This is about as minimal as a PyTest test can get - It doesn't assert anything. It doesn't even really do anything interesting at all! But since it also doesn't raise any Exceptions, it results in a passing test.

Among other things, this demonstrates that we can use PyTest tests to simply "exercise" our code, even if we don't assert anything specific about the behavior (beyond it not being "broken").

This is also an example of how PyTest decides what is and is not a test: By default, it looks for callables (such as functions or methods) whose names begin with "test". And earlier, when we ran it without any arguments, it searched for tests in all the modules (python files) whose name contained "test", by default. (But all these behaviors can be changed, if you want...)

## Up Next:

[Basic Tests and Assertions](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/01_basic_test.md)
