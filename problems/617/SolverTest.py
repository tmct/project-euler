import unittest
from Solver import Solver


class SolverTest(unittest.TestCase):
    def test_d_10(self):
        self.assertEqual(Solver().d(10), 2)

    def test_d_100(self):
        self.assertEqual(Solver().d(100), 21)

    def test_d_1000(self):
        self.assertEqual(Solver().d(1000), 69)

    def test_d_10_6(self):
        self.assertEqual(Solver().d(10**6), 1303)

    def test_d_10_12(self):
        self.assertEqual(Solver().d(10**12), 1014800)

    # def test_d_10_18(self):
    #     self.assertEqual(Solver().d(10**18), ???)


if __name__ == '__main__':
    unittest.main()
