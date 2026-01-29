""" solve.py for 2446번. 별 찍기 - 9 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    upper = [" " * i + "*" * (2 * (n - i) - 1) for i in range(n)]
    lower = [" " * i + "*" * (2 * (n - i) - 1) for i in range(n - 2, -1, -1)]
    return upper + lower


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
