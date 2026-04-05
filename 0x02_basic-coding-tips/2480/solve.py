""" solve.py for 2480번. 주사위 세개 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> int:
    if a == b == c:
        return 10000 + a * 1000
    if b in (a, c):
        return 1000 + b * 100
    if a == c:
        return 1000 + a * 100
    return max(a, b, c) * 100


def main() -> None:
    a, b, c = map(int, sys_input().split())

    answer: int = solve(a, b, c)
    print(answer)


if __name__ == "__main__":
    main()
