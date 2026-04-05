""" solve.py for 2156번. 포도주 시식 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, wine: list[int]) -> int:
    wine = [0] + wine
    if n == 1:
        return wine[1]

    dp = [[0] * 3 for _ in range(n + 1)]
    dp[1][1] = wine[1]
    dp[2][1] = wine[2]
    dp[2][2] = wine[1] + wine[2]

    for i in range(3, n + 1):
        dp[i][0] = max(dp[i - 1])
        dp[i][1] = max(dp[i - 2]) + wine[i]
        dp[i][2] = dp[i - 1][1] + wine[i]

    return max(dp[n])


def main() -> None:
    n = int(sys_input())
    wine = list(int(sys_input()) for _ in range(n))

    answer: int = solve(n, wine)
    print(answer)


if __name__ == "__main__":
    main()
