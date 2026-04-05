""" solve.py for 2445번. 별 찍기 - 8 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    upper = ["*" * i + " " * (2 * (n - i)) + "*" * i for i in range(1, n + 1)]
    lower = ["*" * i + " " * (2 * (n - i)) + "*" * i for i in range(n - 1, 0, -1)]
    return upper + lower


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
