""" solve.py for 2440번. 별 찍기 - 3 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    return ["*" * i for i in range(n, 0, -1)]


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
