""" solve.py for 11057번. 오르막 수 """

import sys


MOD = 10007


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    dp = [[0] * 10 for _ in range(n + 1)]
    for j in range(10):
        dp[1][j]= 1

    for i in range(2, n + 1):
        for j in range(10):
            for k in range(j + 1):
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD

    return sum(dp[n]) % MOD


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
