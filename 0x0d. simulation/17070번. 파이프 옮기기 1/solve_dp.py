""" solve_dp.py for 17070번. 파이프 옮기기 1 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, board: list[list[int]]) -> int:
    dp = [[[0] * n for _ in range(n)] for _ in range(3)]

    dp[0][0][1] = 1

    for x in range(n):
        for y in range(2, n):
            if board[x][y] != 0:
                continue
            dp[0][x][y] = dp[0][x][y - 1] + dp[2][x][y - 1]
            dp[1][x][y] = dp[1][x - 1][y] + dp[2][x - 1][y]
            if board[x - 1][y] == 0 and board[x][y - 1] == 0:
                dp[2][x][y] = dp[0][x - 1][y - 1] + dp[1][x - 1][y - 1] + dp[2][x - 1][y - 1]

    return sum(dp[i][n - 1][n - 1] for i in range(3))


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
