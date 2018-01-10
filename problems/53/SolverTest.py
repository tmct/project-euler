import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_nLessThan24_numberOfChoicesOverAMillion_equalsEleven(self):
        self.assertEqual(4 + 7, Solver().count_choices_over(24, 10**6))

    def test_nLessThan100_numberOfChoicesOverAMillion_equalsEleven(self):
        self.assertEqual(4075, Solver().count_choices_over(100, 10**6))

    def test_nLessThan5_numberOfChoicesOverNine_equalsTwo(self):
        self.assertEqual(2, Solver().count_choices_over(5, 9))


if __name__ == '__main__':
    unittest.main()
