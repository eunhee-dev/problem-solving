""" solve.py for 1074번. Z """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, r: int, c: int) -> int:
    if n == 1:
        return 2 * r + c
    half = 1 << (n-1)
    val = solve(n-1, r % half, c % half)

    offset = (2 * (r // half) + (c // half))
    return offset * half * half  + val


def main() -> None:
    n, r, c = map(int, sys_input().split())

    answer: int = solve(n, r, c)
    print(answer)


if __name__ == "__main__":
    main()
