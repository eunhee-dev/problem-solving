""" solve.py for 11727번. 2×n 타일링 2 """

import sys


MOD = 10007


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 3

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD

    return dp[n]


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
