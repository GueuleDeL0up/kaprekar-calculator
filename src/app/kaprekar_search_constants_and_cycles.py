"""
====================================================
Script Name: kaprekar_search_constants_and_cycles.py
====================================================

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
    python kaprekar_search_constants_and_cycles.py

Description:
    This script defines a function `kaprekar_search_constants_and_cycles` that takes a number represented as a string in a specified base,
    and performs one iteration of the Kaprekar routine. The result is returned as a string in the same base.
"""

from generate_numbers_base import generate_numbers_base
from kaprekar import kaprekar


def kaprekar_search_constants_and_cycles(digits: int, base: int ) -> dict:
    """
    Search for Kaprekar constants and cycles for a given number of digits and base.

    This function iterates over all numbers with the specified number of digits and base,
    performs the Kaprekar routine on each, and identifies both constants (single-number cycles)
    and multi-number cycles. It returns a dictionary containing the Kaprekar constants and cycles.

    :param digits: The number of digits for the numbers to be considered.
    :type digits: int
    :param base: The base of the number system (between 2 and 16 inclusive).
    :type base: int
    :return: A dictionary containing two keys:
        - "constants": A list of Kaprekar constants.
        - "cycles": A list of cycles, each represented as a list of numbers.
    :rtype: dict
    :raises TypeError: If `digits` or `base` is not an integer.
    :raises ValueError: If `base` is not between 2 and 16 inclusive.

    :example:
    >>> kaprekar_search_constants_and_cycles(3, 10)
    {'constants': ['495'], 'cycles': [['198', '594', '495']]}
    
    >>> kaprekar_search_constants_and_cycles(2, 16)
    {'constants': ['00'], 'cycles': [['7F8', '8F7']]}
    """
    
    if not isinstance(digits, int):
        raise TypeError(f"digits must be a integer, {type(digits)} is not a valid type.")
        
    if not isinstance(base, int):
        raise TypeError(f"base must be a integer, {type(digits)} is not a valid type.")
        
    if not 2 <= base <= 16  :
        raise ValueError(f"Base must be between 2 and 16.")
        
    constants = set()
    cycles = set()
    
    list_numbers_in_base = generate_numbers_base(digits=digits, base=base)

    for number in list_numbers_in_base:
        if all(digit == number[0] for digit in number):
                continue
        cycle = kaprekar(number=number, base=base)
        if len(cycle) == 1:
            if cycle[0] != '0' * digits:
                constants.add(cycle[0])
        elif len(cycle) > 1:
            normalized_cycle = tuple(sorted(cycle))
            cycles.add(normalized_cycle)
        
    return {"constants": list(constants), "cycles": [list(cycle) for cycle in cycles]}
        

# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    
    # example usage
    result : dict = kaprekar_search_constants_and_cycles(digits=2, base=10)
    print(result)
    
    return 0

if __name__ == "__main__":
    main()
