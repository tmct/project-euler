from math import log2

LOGGING = True

class Solver:
    def __init__(self):
        self.tub = set()

    def d(self, n):
        # n += 10
        extremes = self.generate_extremes(n)
        return sum(self.count_by_extreme(extreme, n) for extreme in extremes)

    def generate_extremes(self, n):
        extremes = []
        for i in range(1, int(log2(n)) + 1):
            for e in range(2, int(log2(n) ** (1 / i)) + 1):
                a = int(n ** (1 / (e ** i)))
                extremes.append((i, e, a))
        return extremes

    def count_by_extreme(self, extreme, n):
        k = extreme[0]
        e = extreme[1]
        a = extreme[2]
        return sum(self.get_answers(a, e, k, n, t) for t in range(k))

    def get_answers(self, a, e, k, n, t):
        test = a + a ** (e ** k)
        while test > n and a > 1:
            a -= 1
            test = a + a ** (e ** k)

        j = t
        # you've got your result right here!
        if a <= 1:
            return 0
        if a ** (e ** j) + a ** (e ** k) > n:
            return 0
        else:
            # have a working equation!


            # for z in range(k - j):
            #     for y in range (2, a + 1):
            #         to_add = (y ** (e ** j) + y ** (e ** k), e, y ** (e ** z))
            #         self.tub.add(to_add)
            # want case where a = 2 e = 2 j = 2: don't count starting on 4 please
            print(j)
            ways = (a - 2 + 1) * min(k - j, 2)

            return ways
