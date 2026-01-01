"""
Solution for Problem 3 Part 2 - Advent of Code.

This module processes input lines to find maximum digits with specific constraints.
"""
import sys
import os

try:
    from utils import FileIO
except ImportError:
    # Add parent directory to path to import utils module
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from utils import FileIO


def solve():
    """Main function to solve the problem by processing input lines."""
    lines = FileIO.parse_file(
        "/Users/sathishkumar/GitHub-nssathish/adventofcode20xx/2025/problem3/input.txt",
        {"separator": "nl"}
    )
    count = 0

    for line in lines:
        val = get_max_12_digits(line)
        #print(val)
        count += val

    print(count)


def get_max_12_digits(line: str):
    """
    Find the maximum digit in a line with at least 12 remaining characters.
    """
    input_val = list(map(int, line))
    max_val = input_val[0]
    numerals = [max_val]
    length = len(line)

    for i in range(1, length):
        item = input_val[i]
        remaining_chars = length - i
        
        if item > top(numerals):
            numerals = reset_stack(numerals, item, remaining_chars)

        if len(numerals) < 12:
            numerals.append(item)

    return to_big_int(numerals)


def reset_stack(max_digits: list, item: int, remaining_chars: int):
    """Reset the stack by removing elements smaller than the given item."""
    while len(max_digits) and \
        top(max_digits) < int(item) and \
            (remaining_chars + len(max_digits)) > 12:
            max_digits.pop()

    return max_digits


def top(max_digits):
    """Return the top element of the stack or -1 if empty."""
    return max_digits[len(max_digits) - 1] if len(max_digits) else -1


def to_big_int(numerals: list):
    """Convert a string of numerals to an integer by summing and scaling."""
    count = 0
    for numeral in numerals:
        count *= 10
        count += numeral

    return count


if __name__ == '__main__':
    solve()
