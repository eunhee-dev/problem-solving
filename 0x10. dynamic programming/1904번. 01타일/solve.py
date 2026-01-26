""" solve.py for 1904번. 01타일 """

import sys


MOD = 15746


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 2] + dp[i - 1]) % MOD

    return dp[n]


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
