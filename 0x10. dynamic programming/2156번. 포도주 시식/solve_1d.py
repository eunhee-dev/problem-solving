""" solve_1d.py for 2156번. 포도주 시식 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, wine: list[int]) -> int:
    wine = [0] + wine
    if n == 1:
        return wine[1]
    if n == 2:
        return wine[1] + wine[2]

    dp = [0] * (n + 1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    dp[3] = max(dp[2], dp[1] + wine[3], wine[2] + wine[3])

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

    return dp[n]


def main() -> None:
    n = int(sys_input())
    wine = list(int(sys_input()) for _ in range(n))

    answer: int = solve(n, wine)
    print(answer)


if __name__ == "__main__":
    main()
