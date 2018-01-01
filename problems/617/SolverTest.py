import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    # def test_d_10(self):
    #     self.assertEqual(2, Solver().d(10))

    def test_d_100(self):
        self.assertEqual(21, Solver().d(100))

    # def test_d_1000(self):
    #     self.assertEqual(69, Solver().d(1000))
    #
    # def test_d_10_6(self):
    #     self.assertEqual(1303, Solver().d(10**6))
    #
    # def test_d_10_12(self):
    #     self.assertEqual(1014800, Solver().d(10**12))

    # def test_d_10_18(self):
    #     self.assertEqual(???, Solver().d(10**18))


if __name__ == '__main__':
    unittest.main()
