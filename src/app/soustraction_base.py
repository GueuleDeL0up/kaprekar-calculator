"""
=================================
Script Name: soustraction_base.py
=================================

Purpose:
    This script performs subtraction of two numbers in a given base.

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

def soustraction_base(a: str, b: str, base: int) -> str:
    """
    Perform subtraction of two numbers in a given base.

    This function subtracts two numbers represented as strings in the given base,
    ensuring that the first number is larger than the second one, and returns 
    the result as a string in the same base.

    :param a: The first number as a string in the given base.
    :type a: str
    :param b: The second number as a string in the given base.
    :type b: str
    :param base: The base in which the numbers are represented (between 2 and 16 inclusive).
    :type base: int
    :return: The result of subtracting `b` from `a`, represented as a string in the given base.
    :rtype: str
    :raises TypeError: If `a` or `b` is not a string or if `base` is not an integer.
    :raises ValueError: If `a` or `b` is not a positive integer, if `a` is not greater than `b`, or if `base` is not between 2 and 16 inclusive.

    :example:
    >>> soustraction_base("1011", "110", 2)
    '101'
    
    >>> soustraction_base("F1A", "C2", 16)
    '4E'
    """

    if not isinstance(a, str):
        raise TypeError(f"a must be a string, {type(a)} is not a valid type.")
    
    if not isinstance(b, str):
        raise TypeError(f"b must be a string, {type(b)} is not a valid type.")
    
    if not isinstance(base, int):
        raise TypeError(f"base must be a integer, {type(base)} is not a valid type.")
    
    if not (int(a, base) >= 0 and int(b, base) >= 0):
        raise ValueError("a and b must be positive integers")
    
    if not (int(a, base) >= int(b, base)):
        raise ValueError("a must be greater than or equal to b")
    
    if not (2 <= base <= 16):
        raise ValueError("base must be between 2 and 16")

    a = a.upper()
    b = b.upper()

    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    digits = "0123456789ABCDEF"
    char_to_val = {c: i for i, c in enumerate(digits)}
    val_to_char = {i: c for i, c in enumerate(digits)}

    result = []
    borrow = 0

    for i in range(max_len - 1, -1, -1):
        ai = char_to_val[a[i]]
        bi = char_to_val[b[i]]
        diff = ai - bi - borrow
        if diff < 0:
            diff += base
            borrow = 1
        else:
            borrow = 0
        result.append(val_to_char[diff])

    while len(result) > 1 and result[-1] == '0':
        result.pop()

    return ''.join(reversed(result))


# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    
    # example usage
    result : str = soustraction_base("1101", "1010", 2)
    print(result)
    
    return 0

if __name__ == "__main__":
    main()
