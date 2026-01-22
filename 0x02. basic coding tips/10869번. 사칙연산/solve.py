""" solve.py for 10869번. 사칙연산 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int) -> tuple[int, int, int, int, int]:
    return a + b, a - b, a * b, a // b, a % b


def main() -> None:
    a, b = map(int, sys_input().split())

    answer = solve(a, b)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
