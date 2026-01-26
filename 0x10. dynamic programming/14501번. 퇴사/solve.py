""" solve.py for 14501번. 퇴사 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, schedule: list[list[int]]) -> int:
    dp = [0] * (n + 1)
    schedule = [[0, 0]] + schedule

    for i in range(1, n + 1):
        t, p = schedule[i]
        if i + t - 1 <= n:
            dp[i + t - 1] = max(dp[i + t - 1], max(dp[:i]) + p)

    return max(dp)


def main() -> None:
    n = int(sys_input())
    schedule = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, schedule)
    print(answer)


if __name__ == "__main__":
    main()
