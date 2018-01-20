from itertools import permutations


def generate_four_digit_sequence_members(sequence_function):
    i = 1
    while sequence_function(i) < 1000:
        i += 1
    while sequence_function(i) < 10000:
        yield sequence_function(i)
        i += 1


def get_octagonal(n):
    return n * (3 * n - 2)


def get_heptagonal(n):
    return int(n * (5 * n - 3) / 2)


def get_hexagonal(n):
    return n * (2 * n - 1)


def get_pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def get_square(n):
    return n * n


def get_triangle(n):
    return int(n * (n + 1) / 2)


def get_fun_numbers():
    octagonals = frozenset(generate_four_digit_sequence_members(get_octagonal))
    heptagonals = frozenset(generate_four_digit_sequence_members(get_heptagonal))
    hexagonals = frozenset(generate_four_digit_sequence_members(get_hexagonal))
    pentagonals = frozenset(generate_four_digit_sequence_members(get_pentagonal))
    squares = frozenset(generate_four_digit_sequence_members(get_square))
    triangles = frozenset(generate_four_digit_sequence_members(get_triangle))
    return triangles, squares, pentagonals, hexagonals, heptagonals, octagonals


def get_transitions(nums):
    transitions = {}
    for num in nums:
        str_num = str(num)
        transitions.setdefault(str_num[:2], set()).add(str_num[2:])
    return {a: frozenset(b) for a, b in transitions.items()}


def get_nums_from_starts(starts):
    for i in range(len(starts)):
        yield int(starts[i] + starts[(i + 1) % len(starts)])


class FunNumberFinder:
    def __init__(self):
        self.fun_numbers = ()
        self.transitions = ()
        self.starts = []

    # Finds a set of "Cyclical figurate numbers"
    def find_fun_numbers(self):
        for i in self.find_fun_numbers2():
            print(i)
            print(sorted(i))
            print("sum!!!", sum(i))
            for j in range(6):
                print(j + 3)
                print(i.intersection(self.fun_numbers[j]))


    # Finds a set of "Cyclical figurate numbers"
    def find_fun_numbers2(self):
        self.fun_numbers = get_fun_numbers()
        self.transitions = [get_transitions(i) for i in self.fun_numbers]
        print(self.transitions[0])
        # Permutation represents an order of the cycle after the octagonal
        for octagonal_start, octagonal_ends in self.transitions[5].items():
            self.starts = [octagonal_start]
            for octagonal_end in octagonal_ends:
                start = octagonal_end
                self.starts.append(start)
                for perm in permutations(range(5)):
                    yield from self.get_results(start, perm, octagonal_start)
                self.starts.pop()

    def get_results(self, start, perm, octagonal_start):
        if len(perm) == 1:
            if octagonal_start in self.transitions[perm[0]].setdefault(start, frozenset()):
                yield frozenset(get_nums_from_starts(self.starts))
        else:
            for new_start in self.transitions[perm[0]].setdefault(start, frozenset()):
                self.starts.append(new_start)
                yield from self.get_results(new_start, perm[1:], octagonal_start)
                self.starts.pop()


def main():
    FunNumberFinder().find_fun_numbers()


if __name__ == '__main__':
    main()
