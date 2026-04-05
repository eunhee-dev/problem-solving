""" solve.py for 2193번. 이친수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[1][1] = 1

    for i in range(2, n + 1):
        dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0]

    return dp[n][0] + dp[n][1]


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
