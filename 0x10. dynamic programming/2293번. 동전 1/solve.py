""" solve.py for 2293번. 동전 1 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int, coins: list[int]) -> int:
    dp = [0] * (k + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]

    return dp[k]


def main() -> None:
    n, k = map(int, sys_input().split())
    coins = [int(sys_input()) for _ in range(n)]

    answer: int = solve(k, coins)
    print(answer)


if __name__ == "__main__":
    main()
