from itertools import islice, count, combinations

import cProfile
import time
from sympy import primerange, sieve, isprime


def generate_primes():
    prime_digits = 1
    while True:
        for p in primerange(10 ** (prime_digits - 1), 10 ** prime_digits):
            yield p
        prime_digits += 1


def generate_primes_2():
    for i in count():
        if not i % 1000:
            sieve.extend_to_no(i)
        yield sieve[i]


def concat_is_prime(a, b):
    concat = concat_nums(a, b)
    return isprime(concat)


def concat_nums(a, b):
    return int(str(a) + str(b))


def primes_are_compatible(p, q):
    return concat_is_prime(p, q) and concat_is_prime(q, p)


class Solver:
    def __init__(self):
        self.primes = []
        self.k_cliques = tuple()

    def solve(self, number_of_primes):
        start_time = time.time()

        # the compatible primes below p
        self.primes = []

        self.k_cliques = ([], self.primes, [], [], [], [])
        # for p in generate_primes():
        self.generate_1_2_cliques(number_of_primes)
        self.generate_3_4_5_cliques()
        print([len(i) for i in self.k_cliques])
        print(self.k_cliques[5])

        print("time elapsed: {:.2f}s".format(time.time() - start_time))

    def generate_3_4_5_cliques(self):
        # split for profiling :)
        self.generate_3_cliques()
        self.generate_4_cliques()
        self.generate_5_cliques()

    def generate_3_cliques(self):
        self.generate_n_cliques(3)

    def generate_4_cliques(self):
        self.generate_n_cliques(4)

    def generate_5_cliques(self):
        self.generate_n_cliques(5)

    def generate_n_cliques(self, i):
        for c1, c2 in combinations(self.k_cliques[i - 1], 2):
            d1 = c1.difference(c2)
            if len(d1) == 1:
                d2 = c2.difference(c1)
                v1 = next(iter(d1))
                v2 = next(iter(d2))
                crucial_edge = frozenset((v1, v2))
                if crucial_edge in self.k_cliques[2]:
                    # Only count each new clique once
                    if max(c1) == max(c2) or min(c1) == min(c2):
                        continue
                    new_clique = c1.union(d2)
                    self.k_cliques[i].append(new_clique)

    def generate_1_2_cliques(self, number_of_primes):
        for p in islice(generate_primes(), number_of_primes):
            for q in self.primes:
                if primes_are_compatible(p, q):
                    self.k_cliques[2].append(frozenset((p, q)))
            self.primes.append(p)


if __name__ == '__main__':
    # Solver().solve(100)
    cProfile.run('Solver().solve(700)')
