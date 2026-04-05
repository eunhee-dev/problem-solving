""" solve_verbose.py for 17070번. 파이프 옮기기 1 """
# Python3: 시간 초과, PyPy3: 통과

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, board: list[list[int]]) -> int:
    count = 0

    # if board[n - 1][n - 1] == 1:
    #     return 0

    def dfs(x: int, y: int, prev_d: int) -> None:
        nonlocal count

        if (x, y) == (n - 1, n - 1):
            count += 1
            return

        if prev_d == 0:
            if y + 1 < n and board[x][y + 1] == 0:
                dfs(x, y + 1, 0)
            if (x + 1 < n and y + 1 < n
                and board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0):
                dfs(x + 1, y + 1, 2)

        elif prev_d == 1:
            if x + 1 < n and board[x + 1][y] == 0:
                dfs(x + 1, y, 1)
            if (x + 1 < n and y + 1 < n
                and board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0):
                dfs(x + 1, y + 1, 2)

        else:
            if y + 1 < n and board[x][y + 1] == 0:
                dfs(x, y + 1, 0)
            if x + 1 < n and board[x + 1][y] == 0:
                dfs(x + 1, y, 1)
            if (x + 1 < n and y + 1 < n
                and board[x][y + 1] == 0 and board[x + 1][y] == 0 and board[x + 1][y + 1] == 0):
                dfs(x + 1, y + 1, 2)

    dfs(0, 1, 0)

    return count


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
