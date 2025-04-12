import os
import sys
from pathlib import Path
import unittest
import csv
from datetime import datetime

DIR_PATH = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(DIR_PATH + "/app")
from generate_numbers_base import generate_numbers_base


# ==================== Tests ==================== #

class TestGenerateNumbersBase(unittest.TestCase):
    def test_generate_numbers_base_1(self):
        digits : int = 3
        base : int = 2
        expected_output : list[str] = ['100', '101', '110', '111']
        self.assertEqual(generate_numbers_base(digits=digits, base=base), expected_output)


# ==================== if __name__ == "__main__" ==================== #

def main() -> int:
    result = unittest.main(exit=False)

    now = datetime.now()

    new_data = [
        now.strftime("%Y-%m-%d"),
        now.strftime("%H:%M:%S"),
        "Succeed" if result.result.wasSuccessful() else "Failed",
        os.path.basename(__file__)
    ]

    with open(DIR_PATH + "/reports/log.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(new_data)

    return 0 if result.result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
