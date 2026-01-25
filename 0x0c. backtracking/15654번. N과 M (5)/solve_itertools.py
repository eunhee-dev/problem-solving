""" solve_itertools.py for 15654번. N과 M (5) """

import sys
from itertools import permutations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(m: int, integers: list[int]) -> list[str]:
    integers.sort()
    perms = permutations(map(str, integers), m)
    return list(map(" ".join, perms))


def main() -> None:
    _, m = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: list[str] = solve(m, integers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
