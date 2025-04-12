import os
import sys
from pathlib import Path
import unittest
import csv
from datetime import datetime

DIR_PATH = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(DIR_PATH + "/app")
from iteration_kaprekar import iteration_kaprekar


# ==================== Tests ==================== #

class TestIterationKaprekar(unittest.TestCase):
    def test_iteration_kaprekar_1(self):
        number : str = "321"
        base : int = 10
        expected_output : str = "198"
        self.assertEqual(iteration_kaprekar(number=number, base=base), expected_output)


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
