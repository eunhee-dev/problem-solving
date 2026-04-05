""" solve.py for 1932번. 정수 삼각형 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, triangle: list[list[int]]) -> int:
    dp = [[0] * x for x in range(1, n + 1)]

    for y in range(n):
        dp[n - 1][y] = triangle[n - 1][y]

    for x in range(n - 2, -1, -1):
        for y in range(x + 1):
            dp[x][y] = max(dp[x + 1][y], dp[x + 1][y + 1]) + triangle[x][y]

    return dp[0][0]


def main() -> None:
    n = int(sys_input())
    triangle = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, triangle)
    print(answer)


if __name__ == "__main__":
    main()
