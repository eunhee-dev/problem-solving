""" solve.py for 9465번. 스티커 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, sticker: list[list[int]]) -> int:
    for i, row in enumerate(sticker):
        sticker[i] = [0] + row

    dp = [[0] * (n + 1) for _ in range(2)]
    dp[0][1] = sticker[0][1]
    dp[1][1] = sticker[1][1]

    for i in range(2, n + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]

    return max(dp[0][n], dp[1][n])


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        n = int(sys_input())
        sticker = [list(map(int, sys_input().split())) for _ in range(2)]

        answer: int = solve(n, sticker)
        print(answer)


if __name__ == "__main__":
    main()
