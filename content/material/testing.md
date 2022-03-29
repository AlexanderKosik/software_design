# Testing your system

Over time, our system grows as new features are added or existing features need to be modified and extended. The implementation of new features is usually accompanied by an increase in complexity.

For small and simple systems, it is easy to keep track and ensure functionality through manual testing when changes are made.

However, the larger the system becomes, the more difficult it is to keep track and manually test the system. In some circumstances, the duration of performing manual testing after a change outweighs the duration of implementing the change. 

What if only small changes are made to our system, e.g. renaming a variables or moving functions to another module. We call these changes *refactoring*, this means changing the structure of our program or system without changing its functionality. Do such small changes justify retesting the whole application manually?

At this point it is necessary to rethink the strategy of manual testing and to supplement it with automatic tests. 

Manuell tests are usually performed using the system as a whole. In comparison, automatic tests can take place on different levels of our system. Like manual tests they can test the system as a whole (so-called *system tests*), verify the interaction of individual components (so-called *integration tests*) or verify individual units of the system in isolation. In the latter case, we speak of unittests.

# Unit tests
Unittests test units of our system in isolation. But what is *a unit*? A unit is the smallest testable thing. It may be as small as a function, or an object or an modul. The only important thing is that we can test this unit in isolation.

Isolation means, that we have no dependencies to other components that make it hard or even impossible for us to test this unit in isolation. Such dependencies might be connections to specific hardware, dependencies to network input, dependencies to a database and so on. 

Unit tests give us the possibility to test units in isolation so we can be sure that this one thing under tests behaves as expected. We still cannot exclude that the system as a whole works as expected, but having successful running unit tests is a good starting point. 

## Example

Suppose we have function that calculates the arithmetic mean and the median of a list of numbers. 
These functions could be implemented like this:

```python
def mean_int(list_of_numbers) -> int:
    """
    Returns the mean as integer. Function is always rounding down. 
    Returns 0 on empty input
    """
    import math
    try:
        return math.floor(sum(list_of_numbers)/len(list_of_numbers))
    except ZeroDivisionError:
        return 0

def median_int(list_of_numbers) -> int:
    """
    Returns the median as integer. Function is lower item of the sorted list
    if container length is even. 

    Throws an IndexError on empty list
    """
    return sorted(list_of_numbers)[len(list_of_numbers)//2]
```

How can we assure that the functions behave as expected?
We can write unit test functions for the functions that will make sure, they will behave as described.

```python
def test_mean_int():
    assert mean_int([]) == 0, "test with empty list"
    assert mean_int([1, 1, 1]) == 1, "avg of 3x 1 is equal to 1"
    assert mean_int([1, 1, 2]) == 1, "test rounding down"
    print("Good mean_int() function")

def test_median_int():
    assert median_int([1, 1, 1]) == 1, "median of 3x 1 is equal to 1"
    assert median_int([1, 1, 2]) == 1, "test on uneven list length"
    assert median_int([1, 1, 2, 2]) == 1, "test on even list length"
    exceptionThrown = false
    try:
        median_int([]), "test with empty list"
    except IndexError:
        exceptionThrown = true
    assert exceptionThrows, "test IndexError on empty list"
    print("Good median_int() function")
```
# Supporting frameworks

# how many tests do we need?

We can use a metric called cyclomatic complexity. The number of tests is equal to the CC.


# parametrisierte tests
