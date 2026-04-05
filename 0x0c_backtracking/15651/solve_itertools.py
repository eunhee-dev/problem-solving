""" solve_itertools.py for 15651번. N과 M (3) """

import sys
from itertools import product


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int) -> list[str]:
    items = product(map(str, range(1, n+1)), repeat=m)
    return list(map(" ".join, items))


def main() -> None:
    n, m = map(int, sys_input().split())

    answer: list[str] = solve(n, m)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
