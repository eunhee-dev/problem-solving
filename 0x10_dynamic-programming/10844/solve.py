""" solve.py for 10844번. 쉬운 계단 수 """

import sys


MOD = 1_000_000_000


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    dp = [[0] * 10 for _ in range(n + 1)]
    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                dp[i][0] = dp[i - 1][1]
            elif j == 9:
                dp[i][9] = dp[i - 1][8]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

    return sum(dp[n]) % MOD


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
