""" solve_itertools.py for 6603번. 로또 """

import sys
from itertools import combinations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s: list[str]) -> list[str]:
    combs = combinations(s, 6)
    return list(map(" ".join, combs))


def main() -> None:
    while True:
        test_case = sys_input().split()
        if test_case[0] == "0":
            break
        s = test_case[1:]
        answer: list[str] = solve(s)
        print(*answer, sep="\n")
        print()


if __name__ == "__main__":
    main()
