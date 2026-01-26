""" solve.py for 15486번. 퇴사 2 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, schedule: list[list[int]]) -> int:
    dp = [0] * (n + 1)
    schedule = [[0, 0]] + schedule
    max_profit = 0

    for i in range(1, n + 1):
        t, p = schedule[i]
        if i + t - 1 <= n:
            dp[i + t - 1] = max(dp[i + t - 1], max_profit + p)
        max_profit = max(max_profit, dp[i])

    return max_profit


def main() -> None:
    n = int(sys_input())
    schedule = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, schedule)
    print(answer)


if __name__ == "__main__":
    main()
