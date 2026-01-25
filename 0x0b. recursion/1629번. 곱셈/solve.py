""" solve.py for 1629번. 곱셈 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> int:
    if b == 0:
        return 1
    half = solve(a, b//2, c)
    half = (half * half) % c
    if b % 2 == 0:
        return half
    return (half * a) % c


def main() -> None:
    a, b, c = map(int, sys_input().split())

    answer: int = solve(a, b, c)  # pow(a, b, c)
    print(answer)


if __name__ == "__main__":
    main()
