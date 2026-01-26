""" solve.py for 2579번. 계단 오르기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, stairs: list[int]) -> int:
    stairs = [0] + stairs
    if n == 1:
        return stairs[1]

    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1][1] = stairs[1]
    dp[2][1] = stairs[2]
    dp[2][2] = stairs[1] + stairs[2]

    for i in range(3, n + 1):
        dp[i][1] = max(dp[i - 2][1], dp[i - 2][2]) + stairs[i]
        dp[i][2] = dp[i - 1][1] + stairs[i]

    return max(dp[n][1], dp[n][2])


def main() -> None:
    n = int(sys_input())
    stairs = [int(sys_input()) for _ in range(n)]

    answer: int = solve(n, stairs)
    print(answer)


if __name__ == "__main__":
    main()
