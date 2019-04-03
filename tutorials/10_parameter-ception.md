## 10: Parameter-ception!

Python includes an amazing set of Iteration Tools, including functions that make it simple to generate all possible combinations and permutations of a set of data - We're about to see an interesting example of this kind of behavior, using multiple parameterized fixtures.

It's a lot easier to demonstrate than explain, so let's start with that: Here's another single test case, which depends on two fixtures - And it's worth noting that each of those fixtures each have their own set of parameters:

[tests/09_params-ception_test.py](https://github.com/pluralsight/intro-to-pytest/blob/master/tests/09_params-ception_test.py)

```
pytest -vs tests/09_params-ception_test.py
```

How did two sets of 4 parameters turn into 16 tests? The short answer is that we're experiencing the [Cartesian Product](https://en.wikipedia.org/wiki/Cartesian_product) of our fixture parameters.

But the less set-theory-intensive answer is that our test case depends on `letters_fixture`, which causes PyTest to produce a test for each letter parameter... And it also depends on `numbers_fixture`, which in turn wants to repeat each test with each of its own number parameters.

This is evident from the order in which the tests are run, and (thanks to PyTest!) from the labels of those tests: We can see that our test is being run first with our `letters_fixture`, and each of its parameters (starting with "a"), and those runs are being further "multiplied" by the `letters_fixture`, which is ensuring that its own tests are being repeated for each of its own parameters (starting with "1").

As a result, our single test case function gets run as a total of sixteen tests, once for each combination of the four numbers and four letters (4 x 4 = 16).

While we _could_ just make a single fixture that yielded each combination as a parameter ('a1', 'a2', 'a3', etc.), maintaining them as separate fixtures reduces the footprint of those parameters in our code, leaving it somewhat easier to read (in the sense that two lists of four takes up half the space of a full list of sixteen).

But these individual fixtures could also be reused and composed across different tests, allowing for a lot more flexibility, especially if the letters or numbers ever needed to be referenced on their own. And imagine if you needed a fixture that tested 234 unique combinations of letters and digits, and later decided to drop all the sets with vowels, or all the sets containing the number 3 - Wouldn't it be cleaner and easier to operate on two smaller subsets (the list of the 26 letters, and the list of 9 digits) that combine to produce that data?

But there's an even more elegant way to solve that particular problem, continuing to take advantage of the fact that fixtures can, in turn, depend on other fixtures...

### Up Next:

[Advanced Parameter-ception!](https://github.com/pluralsight/intro-to-pytest/blob/master/tutorials/11_advanced_parameter-ception.md)
