import unittest
from Solver1 import Solver1


class SolverTest(unittest.TestCase):
    def test_d_10(self):
        self.assertEqual(2, Solver1().d(10))

    def test_d_100(self):
        self.assertEqual(21, Solver1().d(100))

    # def test_d_1000(self):
        #self.assertEqual(69, Solver1().d(1000))
    #
    # def test_d_10_6(self):
    #     self.assertEqual(1303, Solver1().d(10**6))

    # def test_d_10_12(self):
    #     self.assertEqual(1014800, Solver1().d(10**12))

    # def test_d_10_18(self):
    #     self.assertEqual(???, Solver1().d(10**18))


if __name__ == '__main__':
    unittest.main()
