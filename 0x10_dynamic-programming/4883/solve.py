""" solve.py for 4883번. 삼각 그래프 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, board: list[list[int]]) -> int:
    dp = [[0] * 3 for _ in range(n)]

    dp[0][0] = sys.maxsize
    dp[0][1] = board[0][1]
    dp[0][2] = dp[0][1] + board[0][2]

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][0], dp[i - 1][1]) + board[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2], dp[i][0]) + board[i][1]
        dp[i][2] = min(dp[i - 1][1], dp[i - 1][2], dp[i][1]) + board[i][2]

    return dp[n - 1][1]


def main() -> None:
    t = 1
    while True:
        n = int(sys_input())
        if n == 0:
            break
        board = [list(map(int, sys_input().split())) for _ in range(n)]

        answer: int = solve(n, board)
        print(f"{t}. {answer}")

        t += 1


if __name__ == "__main__":
    main()
