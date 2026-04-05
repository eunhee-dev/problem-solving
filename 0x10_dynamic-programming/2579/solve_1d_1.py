""" solve_1d_1.py for 2579번. 계단 오르기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, stairs: list[int]) -> int:
    stairs = [0] + stairs
    if n == 1:
        return stairs[1]

    dp = [0] * (n + 1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]

    return dp[n]


def main() -> None:
    n = int(sys_input())
    stairs = [int(sys_input()) for _ in range(n)]

    answer: int = solve(n, stairs)
    print(answer)


if __name__ == "__main__":
    main()
