import math


def nCr(n, r):
    f = math.factorial
    return f(n) / f(r) / f(n - r)


class Solver:
    def count_choices_over(self, highest_n, threshold):
        sum = 0
        for n in range(2, highest_n + 1):
            for r in range(1, n // 2 + 1):
                if nCr(n, r) > threshold:
                    number_over_threshold = n - 2 * r + 1
                    sum += number_over_threshold
                    break
        return sum
