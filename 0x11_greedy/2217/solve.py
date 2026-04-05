""" solve.py for 2217번. 로프 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, ropes: list[int]) -> int:
    ropes.sort()
    max_weight = 0

    for i in range(1, n + 1):
        max_weight = max(max_weight, ropes[n - i] * i)

    return max_weight


def main() -> None:
    n = int(sys_input())
    ropes = [int(sys_input()) for _ in range(n)]

    answer: int = solve(n, ropes)
    print(answer)


if __name__ == "__main__":
    main()
