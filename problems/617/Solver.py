from math import log2

LOGGING = True

class Solver:
    def d(self, n):
        return self.c(n) + 1 # Why have I missed one?!! Oh well

    # Number of (n,e) MPS for some E
    def c(self, n):
        return sum(self.find_number_of_mpses(i, e) for i in range(6, n) for e in range(2, int(log2(n))))

    # Number of (n,e) MPS
    def find_number_of_mpses(self, n, e):
        integer_under_root = int(n ** (1/e))
        sequence = []
        # future improvement: iterate over squares...
        jump_up_destination = integer_under_root ** e
        jump_down_destination = n - jump_up_destination
        if jump_down_destination < 2:
            return 0
        current_a = jump_down_destination
        sequence.append(current_a)
        if current_a == integer_under_root:
            num_of_sequences = self.get_number_of_full_sequences_from_base_sequence(e, sequence)
            if LOGGING:
                print("Found a ({},{}) base sequence: {}. With {} starting points".format(n, e, sequence, num_of_sequences))
            return num_of_sequences
        while current_a < integer_under_root:
            current_a = current_a ** e
            sequence.append(current_a)
        if current_a == integer_under_root:
            num_of_sequences = self.get_number_of_full_sequences_from_base_sequence(e, sequence)
            if LOGGING:
                print("Found a ({},{}) base sequence: {}. With {} starting points".format(n, e, sequence, num_of_sequences))
            return num_of_sequences
        else:
            return 0

    # Number of (n,e) MPS for a given base sequence
    def get_number_of_full_sequences_from_base_sequence(self, e, sequence):
        first_member = sequence[0]
        return len(sequence) + self.number_of_lower_roots(first_member, e, 0)

    def number_of_lower_roots(self, num, e, total_already):
        putative_root = int(num ** (1/e))
        if putative_root ** 2 == num:
            return self.number_of_lower_roots(putative_root, e, total_already + 1)
        return total_already
