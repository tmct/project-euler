from math import floor, log2


class Solver:
    def d(self, n):
        return self.c(n)

    # Number of (n,e) MPS for some E
    def c(self, n):
        return sum(self.find_number_of_mpses(i, e) for i in range(6, n) for e in range(2, int(floor(log2(n)))))

    # Number of (n,e) MPS
    @staticmethod
    def find_number_of_mpses(n, e):
        integer_under_root = floor(n ** (1/e))
        sequence = [integer_under_root]
        # future improvement: iterate over squares...
        jump_up_destination = integer_under_root ** e
        jump_down_destination = n - jump_up_destination
        if jump_down_destination < 2:
            return 0
        current_a = jump_down_destination
        sequence.append(current_a)
        if current_a == integer_under_root:
            sequence.pop()
            print("Found a ({},{}) sequence: {}".format(n, e, sequence))
            return 1
        while current_a < integer_under_root:
            current_a = current_a ** e
            sequence.append(current_a)
        if current_a == integer_under_root:
            sequence.pop()
            print("Found a ({},{}) sequence: {}".format(n, e, sequence))
            return 1
        else:
            return 0
