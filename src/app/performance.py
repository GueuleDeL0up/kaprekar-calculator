"""
===========================
Script Name: performance.py
===========================

Purpose:
    This script test functions performance.

Author:
    GueuleDeL0up

Date:
    April 2025

Version:
    1.0.0

Dependencies:
    - datetime
    - time
    - csv

Usage:
    python performance.py

Description:
    This script defines a function `performance` that takes a function and its arguments,
    measures the execution time of the function, and writes the results to a CSV file.
    The CSV file contains the date, time, and execution time of the function.
"""

from datetime import datetime
import time
import csv

# Functions to test
from generate_numbers_base import generate_numbers_base
from soustraction_base import soustraction_base
from iteration_kaprekar import iteration_kaprekar
from kaprekar import kaprekar
from kaprekar_search_constants_and_cycles import kaprekar_search_constants_and_cycles


def performance(func, args: list=list()) -> int:
    """
    Test the execution time of a function.

    Args:
        func (_type_): Function to test.
        args (list, optional): Arguments to take. Defaults to list().

    Returns:
        int: Return 0 if it is end with no errors.
    """
    now = datetime.now()

    #=====================#
    
    start_time = time.perf_counter()
    func(*args)
    end_time = time.perf_counter()

    #=====================#
    
    timer = f'{end_time - start_time:.5f}'
    
    new_data = [now.strftime("%Y-%m-%d"),
                now.strftime("%H:%M:%S"),
                timer,
                func.__name__
                ]
    
    with open("src/reports/performance.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_data)
        
    return 0


# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    performance(kaprekar_search_constants_and_cycles, args=[5, 10])
    return 0

if __name__ == '__main__':
    main()
