""" solve.py for 1149번. RGB거리 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, cost: list[list[int]]) -> int:
    cost = [[0, 0, 0]] + cost
    if n == 1:
        return min(cost[1])

    dp = [[0, 0, 0] for _ in range(n + 1)]
    for color in range(3):
        dp[1][color] = cost[1][color]

    for i in range(2, n + 1):
        for color in range(3):
            dp[i][color] = min(dp[i - 1][j] + cost[i][color] for j in range(3) if color != j)

    return min(dp[n][j] for j in range(3))


def main() -> None:
    n = int(sys_input())
    cost = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, cost)
    print(answer)


if __name__ == "__main__":
    main()
