""" solve.py for 2442번. 별 찍기 - 5 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    return [" " * (n - i) + "*" * (2 * i - 1) for i in range(1, n + 1)]


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
