### TASK ONE ###

"""
This is a possible interview coding question. Let's check the task,
implement our solution and then write tests for it:

Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'

Constraint notes:
an input integer is always withing the range 1 to 100 inclusive
"""


# Return true when it is even , false otherwise
def is_even(num):
    return num % 2 == 0


# Return true if the given number is between min and max, otherwise return false
def within_range(num, min, max):
    if min <= num <= max:
        return True
    return False

def red_or_blue(num):
    if not within_range(num, 1, 100):
        raise ValueError('Number must be between 1 and 100')

    if not is_even(num) or within_range(num, 6, 20):
        return 'Red'

    if within_range(num, 2, 5) and num > 20:
        return 'Blue'


### TASK TWO -- TDD ###

"""
Let's write a test for our function first and then will write an actual code to ensure that
all tests pass. 

Task
Given a list of dictionaries where keys are student's  name and student's mark.
calculate the average score for the exam.

If mark is not within the range 1 to 10, raise an error
Some mark values can be integers and some are strings, we need to process both
If mark is missing, use value 5

"""
from unittest import TestCase, main
class TestAverageExamScore(TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'Marks': 7},
            {'name': 'Nitesh', 'Marks': 6},
            {'name': 'Aisha', 'Marks': 8},
            {'name': 'Zac', 'Marks': 8},
        ]

        expected = 7.25
