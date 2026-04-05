""" solve_itertools.py for 15665번. N과 M (11) """

import sys
from itertools import product


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(m: int, integers: list[int]) -> list[str]:
    integers.sort()
    items = product(map(str, integers), repeat=m)
    items = list(dict.fromkeys(items))
    return list(map(" ".join, items))


def main() -> None:
    _, m = map(int, sys_input().split())
    integers = list(map(int, sys_input().split()))

    answer: list[str] = solve(m, integers)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
