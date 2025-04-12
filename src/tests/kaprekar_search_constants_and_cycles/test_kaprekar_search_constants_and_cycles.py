import os
import sys
from pathlib import Path
import unittest
import csv
from datetime import datetime

DIR_PATH = str(Path(__file__).resolve().parent.parent.parent)
sys.path.append(DIR_PATH + "/app")
from kaprekar_search_constants_and_cycles import kaprekar_search_constants_and_cycles


# ==================== Tests ==================== #

class TestKaprekarSearchConstantsAndCycles(unittest.TestCase):
    def test_kaprekar_search_constants_and_cycles_1(self):
        digits: int = 2
        base : int = 10
        expected_output : dict = {
            'constants': [],
            'cycles': [['27', '45', '63', '81', '9']]
            }
        self.assertEqual(kaprekar_search_constants_and_cycles(digits=digits, base=base), expected_output)


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
