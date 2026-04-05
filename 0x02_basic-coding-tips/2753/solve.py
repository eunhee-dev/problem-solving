""" solve.py for 2753번. 윤년 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(year: int) -> int:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 1
    return 0

def main() -> None:
    year = int(sys_input())

    answer: int = solve(year)
    print(answer)


if __name__ == "__main__":
    main()
