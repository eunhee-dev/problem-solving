""" solve_itertools.py for 15666번. N과 M (12) """

import sys
from itertools import combinations_with_replacement


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(m: int, integers: list[int]) -> list[str]:
    integers.sort()
    combs = combinations_with_replacement(map(str, integers), m)
    combs = list(dict.fromkeys(combs))
    return list(map(" ".join, combs))


def main() -> None:
    _, m = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: list[str] = solve(m, integers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
