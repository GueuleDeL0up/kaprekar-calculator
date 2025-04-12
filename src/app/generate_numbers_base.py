"""
=====================================
Script Name: generate_numbers_base.py
=====================================

Purpose:
    This script generates all numbers of a specified digit length in a given base.

Author:
    GueuleDeL0up

Date:
    April 2025

Version:
    1.0.0

Dependencies:
    None

Usage:
    python generate_numbers_base.py

Description:
    This script reads a list of numbers from an input file, generates all numbers of a specified digit length in a given base,
    and saves the results to an output CSV file.
"""

def generate_numbers_base(digits: int, base: int) -> list:
    """
    Generate all numbers of a specified digit length in a given base.

    This function returns all numbers with the exact number of digits specified,
    represented as strings using characters from 0 to F (depending on the base).
    Supports bases from 2 to 16.

    :param digits: The number of digits each number should have.
    :type digits: int
    :param base: The base in which to generate the numbers (between 2 and 16 inclusive).
    :type base: int
    :return: A list of strings representing numbers of the specified digit length in the given base.
    :rtype: list[str]
    :raises TypeError: If `digits` or `base` is not an integer.
    :raises ValueError: If `base` is not between 2 and 16 inclusive.

    :example:
    >>> generate_numbers_base(2, 2)
    ['10', '11']
    
    >>> generate_numbers_base(2, 16)
    ['10', '11', ..., 'FF']
    """
    
    if not (isinstance(digits, int)):
        raise TypeError(f"digits must be a integer, {type(digits)} is not a valid type.")
    
    if not (isinstance(base, int)):
        raise TypeError(f"base must be a integer, {type(base)} is not a valid type.")
    
    if not (2 <= base <= 16):
        raise ValueError(f"base must be between 2 and 16.")
    
    symboles = "0123456789ABCDEF"

    min_val = base ** (digits - 1)
    max_val = base ** digits

    result = []
    for i in range(min_val, max_val):
        num = ""
        n = i
        while n > 0:
            num = symboles[n % base] + num
            n //= base

        while len(num) < digits:
            num = "0" + num

        result.append(num)

    return result


# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    
    # example usage
    result : list = generate_numbers_base(digits=2, base=10)
    print(result)
    
    return 0

if __name__ == "__main__":
    main()
