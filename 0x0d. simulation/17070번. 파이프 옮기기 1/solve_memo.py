""" solve_memo.py for 17070번. 파이프 옮기기 1 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, board: list[list[int]]) -> int:
    memo = {}

    # if board[n - 1][n - 1] == 1:
    #     return 0

    def dfs(x: int, y: int, prev_d: int) -> int:
        count = 0

        if (x, y, prev_d) in memo:
            return memo[(x, y, prev_d)]

        if (x, y) == (n - 1, n - 1):
            return 1

        if prev_d != 1 and y + 1 < n and board[x][y + 1] == 0:
            count += dfs(x, y + 1, 0)

        if prev_d != 0 and x + 1 < n and board[x + 1][y] == 0:
            count += dfs(x + 1, y, 1)

        if (x + 1 < n and y + 1 < n and
            board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0):
            count += dfs(x + 1, y + 1, 2)

        memo[(x, y, prev_d)] = count
        return count

    return dfs(0, 1, 0)


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
