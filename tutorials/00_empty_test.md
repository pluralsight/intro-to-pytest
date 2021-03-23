## 0: An Empty Test

The first test is pretty boring: It is a module with "test" in the name, containing a callable (in this case, a plain old function) which also has "test" in the name, that doesn't really do anything.

[tests/00_empty_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/00_empty_test.py)

```
pytest -vs tests/00_empty_test.py
```

This is about as minimal as a PyTest test can get - It doesn't assert anything. It doesn't really do anything interesting at all! But since it also doesn't raise any Exceptions, it results in a passing test.

Among other things, this demonstrates that we can use PyTest tests to simply "exercise" our code, even if we don't assert anything specific about the behavior (beyond it not being "broken"), in the sense that it does not raise any unhandled Exceptions or Errors.

This is also an example of how PyTest decides what is and is not a test: By default, it looks for callables (such as functions or methods) whose names begin with "test". And earlier, when we ran it without any arguments, it searched for tests in all the modules (python files) whose name started with "test_" or ended with "_test", by default. 

If you take a look into the file, you'll see that PyTest _did_ run the `test_empty` function, since its name starts with "test", but it chose not to run the `empty_test` function, since it contains "test", but does not start with it.

All of these "test discovery" behaviors can be changed, if you want, but I recommend at least starting with PyTest's defaults, as they tend to be pretty reasonable.

While it's a start, this test doesn't really prove much - let's fix that!

## Up Next:

[Basic Tests and Assertions](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/01_basic_test.md)
