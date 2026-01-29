""" solve.py for 2443번. 별 찍기 - 6 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    return [" " * i + "*" * (2 * (n - i) - 1) for i in range(n)]


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
