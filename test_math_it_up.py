import pytest
import math_it_up

"""
This file contains the tests for the math_it_up module, which contains the
following functions:

- math_it_up.is_even
- math_it_up.is_odd
- math_it_up.mean
- math_it_up.median
- math_it_up.mode

The `is_even` and `is_odd` functions accept a single argument, a number, and
return True if the number is even or odd, respectively.

The `mean` function accepts a single argument, a list of numbers, and returns
the mean of the numbers.

The `median` function accepts a single argument, a list of numbers, and returns
the median of the numbers.

The `mode` function accepts a single argument, a list of numbers, and returns
the mode of the numbers.

To run the tests, run `pytest` from the command line in the same directory as
this file.
"""

def test_is_even():
  """
  Tests for the `is_even` function
  """
  assert math_it_up.is_even(2) == True
  assert math_it_up.is_even(-2) == True
  assert math_it_up.is_even(0) == True
  assert math_it_up.is_even(1) != True
  assert math_it_up.is_even(1) == False
  assert math_it_up.is_even(100050) == True


def test_is_odd():
  """
  Tests for the `is_odd` function
  """
  assert math_it_up.is_odd(1) == True
  assert math_it_up.is_odd(10001) == True
  assert math_it_up.is_odd(2) != True
  assert math_it_up.is_odd(-1) == True
  assert math_it_up.is_odd(2) == False
  assert math_it_up.is_odd(0) == False    



def test_mean():
  """
  Tests for the `mean` function
  """
  assert math_it_up.mean([1, 2, 5, 0]) == 2
  assert math_it_up.mean([1, 2, 5, 0]) != 1
  assert math_it_up.mean([1, 2, 5, 100]) == 27
  assert math_it_up.mean([0, 0, 0, 0, 0, 0, 0, 0]) == 0
  assert math_it_up.mean([-1, -3, -5, -6, -5]) == -4
  assert math_it_up.mean([1]) == 1
  assert math_it_up.mean([240, -120]) == 60

def test_median():
  """
  Tests for the `median` function
  """
  assert math_it_up.median([1, 2, 5, 6, 10]) == 5
  assert math_it_up.median([1, 2, 5, 6, 10]) != 2
  assert math_it_up.median([1, 2, 5, 6, 10, 10]) == 5.5
  assert math_it_up.median([1, 2]) == 1.5
  assert math_it_up.median([0, 0, 0, 0, 1]) == 0
  assert math_it_up.median([10, 2, 5, 6, 10]) == 6
  assert math_it_up.median([9, 8, 5, 6, 10]) == 8
  assert math_it_up.median([1]) == 1

def test_mode():
  """
  Tests for the `mode` function
  """

  # 
  assert math_it_up.mode([1, 1, 5, 6, 10]) == [1]
  assert math_it_up.mode([1, 1, 5, 5, 10]) == [1, 5]
  assert math_it_up.mode([1, 1, 5, 5, 10, 10]) == [1, 5, 10]
  assert math_it_up.mode([1, 5, 6, 10, 10]) != [1]
  assert math_it_up.mode([1]) == [1]
  assert math_it_up.mode([1, 1, 5, 6, 10, 10, 10, 10, 10, 0]) == [10]
  assert math_it_up.mode([1, 1, 1, 1, 1, 1, 1, 1]) == [1]