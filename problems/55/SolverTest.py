import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test(self):
        self.assertEqual(249, Solver().count_lychrels(10 ** 4, 50))


if __name__ == '__main__':
    unittest.main()
