def is_palindrome(n):
    return str(n) == str(n)[::-1]


def get_palindrome(n):
    return int(str(n)[::-1])


def add_to_palindrome(n):
    return n + get_palindrome(n)


class Solver:
    def count_lychrels(self, limit_exclusive, max_given_iterations):
        is_lychrel = {}
        for a in range(1, limit_exclusive):
            test_group = [a]
            if a in is_lychrel:
                continue
            orig_a = a
            for i in range(max_given_iterations):
                a = add_to_palindrome(a)
                if a in is_lychrel:
                    for n in test_group:
                        is_lychrel[n] = is_lychrel[a]
                    break
                if is_palindrome(a):
                    for n in test_group:
                        is_lychrel[n] = False
                    break
                if a < limit_exclusive:
                    test_group.append(a)
            if orig_a not in is_lychrel:
                for n in test_group:
                    is_lychrel[n] = True
        return sum(is_lychrel.values())
