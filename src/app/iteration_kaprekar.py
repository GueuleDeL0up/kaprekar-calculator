"""
==================================
Script Name: iteration_kaprekar.py
==================================

Purpose:
    This script performs the Kaprekar routine on a number in a given base.

Author:
    GueuleDeL0up

Date:
    April 2025

Version:
    1.0.0

Dependencies:
    None

Usage:
    python iteration_kaprekar.py

Description:
    This script defines a function `iteration_kaprekar` that takes a number represented as a string in a specified base,
    and performs one iteration of the Kaprekar routine. The result is returned as a string in the same base.
"""

from soustraction_base import soustraction_base


def iteration_kaprekar(number: str, base: int) -> str:
    """
    Perform one iteration of the Kaprekar routine on a number in a given base.

    This function arranges the digits of the number in descending and ascending order,
    subtracts the smaller from the larger (in the given base), and returns the result
    as a string in the same base.

    :param number: The number as a string in the given base.
    :type number: str
    :param base: The base of the number system (between 2 and 16 inclusive).
    :type base: int
    :return: The result of one Kaprekar iteration as a string.
    :rtype: str
    :raises TypeError: If `number` is not a string or `base` is not an integer.
    :raises ValueError: If `base` is not between 2 and 16 inclusive.

    :example:
    >>> iteration_kaprekar("321", 10)
    '198'
    
    >>> iteration_kaprekar("B3A", 16)
    '7F8'
    """

    if not isinstance(number, str):
        raise TypeError(f"number must be a string, {type(number)} is not a valid type.")
        
    if not isinstance(base, int):
        raise TypeError(f"base must be a integer, {type(base)} is not a valid type.")
    
    if not (2 <= base <= 16):
        raise ValueError("base must be between 2 and 16")

    number_asc = ''.join(sorted(number))
    number_desc = ''.join(sorted(number, reverse=True))
    diff = soustraction_base(number_desc, number_asc, base)
    
    return diff

# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    
    # example usage
    result : str = iteration_kaprekar("321", 10)
    print(result)
    
    return 0

if __name__ == "__main__":
    main()
