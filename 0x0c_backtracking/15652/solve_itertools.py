""" solve_itertools.py for 15652번. N과 M (4) """

import sys
from itertools import combinations_with_replacement


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int) -> list[str]:
    combs = combinations_with_replacement(map(str, range(1, n+1)), m)
    return list(map(" ".join, combs))


def main() -> None:
    n, m = map(int, sys_input().split())

    answer: list[str] = solve(n, m)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
