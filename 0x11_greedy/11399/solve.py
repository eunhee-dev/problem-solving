""" solve.py for 11399번. ATM """

import sys
from itertools import accumulate


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(p: list[int]) -> int:
    p.sort()
    return sum(accumulate(p))


def main() -> None:
    _ = int(sys_input())
    p = list(map(int, sys_input().split()))

    answer: int = solve(p)
    print(answer)


if __name__ == "__main__":
    main()
