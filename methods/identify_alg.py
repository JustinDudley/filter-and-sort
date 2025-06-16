
from methods.find_pattern import find_pattern
from methods.find_group_and_kingdom import find_group_and_kingdom


def identify_alg(alg):
    pattern = find_pattern(alg)
    group_number, isCornerAlg = find_group_and_kingdom(pattern)   # note destructuring syntax

    return [pattern, group_number, isCornerAlg]