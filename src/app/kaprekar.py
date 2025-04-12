"""
========================
Script Name: kaprekar.py
========================

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
    python soustraction_base.py

Description:
    This script defines a function `soustraction_base` that takes two numbers represented as strings in a specified base,
    and performs subtraction, ensuring that the first number is larger than the second one.
    The result is returned as a string in the same base.
"""

from iteration_kaprekar import iteration_kaprekar


def kaprekar(number: str, base: int ) -> list:
    """
    Perform the Kaprekar routine repeatedly on a number in a given base until a cycle is detected.

    This function applies the Kaprekar transformation iteratively, arranging the digits of the number
    in descending and ascending order, subtracting the smaller from the larger (in the given base),
    and continues until the result repeats, forming a cycle.

    :param number: The starting number as a string in the given base.
    :type number: str
    :param base: The base of the number system (between 2 and 16 inclusive).
    :type base: int
    :return: A list representing the cycle of numbers formed by the Kaprekar routine.
    :rtype: list
    :raises TypeError: If `number` is not a string or `base` is not an integer.
    :raises ValueError: If `base` is not between 2 and 16 inclusive, if `number` contains invalid digits for the given base,
                        or if `number` consists of identical digits.
    
    :example:
    >>> kaprekar("321", 10)
    ['198', '198']
    
    >>> kaprekar("B3A", 16)
    ['7F8', '7F8']
    """
    
    if not isinstance(number, str):
        raise TypeError(f"number must be a string, {type(number)} is not a valid type.")
        
    if not isinstance(base, int):
        raise TypeError(f"base must be a integer, {type(digits)} is not a valid type.")
        
    if not (2 <= base <= 16):
        raise ValueError(f"Base must be between 2 and 16.")
    
    possible_digits : list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"][:base]
    for digit in number:
        if digit not in possible_digits:
            raise ValueError(f"number must be in base {base}, {digit} is not a valid digit.")
    
    if all(digit == number[0] for digit in number):
        raise ValueError(f"number can't be iddentical, {number} is not a valid number.")
    
    digits : int = len(number)
    seen : set = {}
    sequence : list = []

    while True:
        new_number = iteration_kaprekar(number.zfill(digits), base)

        if new_number in seen:
            cycle_start = sequence.index(new_number)
            cycle = sequence[cycle_start:]
            return cycle

        sequence.append(new_number)
        seen[new_number] = True

        number = new_number


# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    
    # example usage
    result : list = kaprekar(number="1010", base=2)
    print(result)
    
    return 0

if __name__ == "__main__":
    main()
