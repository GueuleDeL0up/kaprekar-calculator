"""
====================
Script Name: main.py
====================

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
    python main.py

Description:
    This script defines a function `main` that initializes the parameters for the Kaprekar routine,
    calls the `kaprekar_search_constants_and_cycles` function, and prints the results.
"""

from kaprekar_search_constants_and_cycles import kaprekar_search_constants_and_cycles


def main() -> int:
    """
    Launches an interactive interface to find Kaprekar constants and cycles 
    for a user-specified number of digits and base.

    Prompts the user for:
    - Number of digits.
    - Numerical base.

    Then calls `kaprekar_search_constants_and_cycles()` and displays the results.

    :return: Exit code (always 0).
    :rtype: int
    """
    
    print()
    
    print("Kaprekar search constants and cycles for x digits in base n:")
    
    while True:
        entry : str = input("Number of digits: ")
        try:
            digits : int = int(entry)
            if not (2 <= digits):
                raise print("Number of digits must be greater than 1.")
            break
        except:
            continue
    
    while True:
        entry : str = input("Base number: ")
        try:
            base : int = int(entry)
            if not (2 <= base <= 16):
                raise print("Base number must be between 2 and 16.")
            break
        except:
            continue

    result = kaprekar_search_constants_and_cycles(digits=digits, base=base)
    
    print("\nResult:")
    if result["constants"] != []:
        print("Constants:")
        for constant in result["constants"]:
            print(f"    - {constant}")
    
    if result["cycles"] != []:
        print("Cycles:")
        for cycles in result["cycles"]:
            print(f"    - {cycles}")
            
    print()
    
    return 0

if __name__ == '__main__':
    main()
