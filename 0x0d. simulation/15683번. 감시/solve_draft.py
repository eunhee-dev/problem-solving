""" solve_draft.py for 15683번. 감시 """

import sys
import copy


DIRECTIONS = {
    "up": (1, 0),
    "right": (0, 1),
    "down": (-1, 0),
    "left": (0, -1)
}


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def mark_up(board: list[list[str]], x: int, y: int) -> list[list[str]]:
    checked_board = copy.deepcopy(board)
    nx = x
    while nx >= 0 and checked_board[nx][y] != "6":
        if checked_board[nx][y] == "0":
            checked_board[nx][y] = "#"
        nx -= 1
    return checked_board


def mark_down(board: list[list[str]], x: int, y: int) -> list[list[str]]:
    checked_board = copy.deepcopy(board)
    nx = x
    while nx < len(board) and checked_board[nx][y] != "6":
        if checked_board[nx][y] == "0":
            checked_board[nx][y] = "#"
        nx += 1
    return checked_board


def mark_left(board: list[list[str]], x: int, y: int) -> list[list[str]]:
    checked_board = copy.deepcopy(board)
    ny = y
    while ny >= 0 and checked_board[x][ny] != "6":
        if checked_board[x][ny] == "0":
            checked_board[x][ny] = "#"
        ny -= 1
    return checked_board


def mark_right(board: list[list[str]], x: int, y: int) -> list[list[str]]:
    checked_board = copy.deepcopy(board)
    ny = y
    while ny < len(board[0]) and checked_board[x][ny] != "6":
        if checked_board[x][ny] == "0":
            checked_board[x][ny] = "#"
        ny += 1
    return checked_board


def count_blind_spots(board: list[list[str]]) -> int:
    return sum(1 if val == "0" else 0 for row in board for val in row)


def solve(n: int, m: int, board: list[list[str]]) -> int:
    ans = n * m
    cctv = []
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val in ("0", "6", "#"):
                continue
            if val == "5":
                board = mark_up(board, x, y)
                board = mark_down(board, x, y)
                board = mark_left(board, x, y)
                board = mark_right(board, x, y)
            else:
                cctv.append((x, y))

    def backtrack(i: int, _board: list[list[str]]) -> None:
        nonlocal ans
        if i == len(cctv):
            ans = min(ans, count_blind_spots(_board))
            return
        x, y = cctv[i]
        if _board[x][y] == "1":
            next_board = mark_left(_board, x, y)
            backtrack(i + 1, next_board)
            next_board = mark_right(_board, x, y)
            backtrack(i + 1, next_board)
            next_board = mark_up(_board, x, y)
            backtrack(i + 1, next_board)
            next_board = mark_down(_board, x, y)
            backtrack(i + 1, next_board)

        if _board[x][y] == "2":
            next_board = mark_left(_board, x, y)
            next_board = mark_right(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_up(_board, x, y)
            next_board = mark_down(next_board, x, y)
            backtrack(i + 1, next_board)

        if _board[x][y] == "3":
            next_board = mark_up(_board, x, y)
            next_board = mark_right(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_right(_board, x, y)
            next_board = mark_down(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_down(_board, x, y)
            next_board = mark_left(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_left(_board, x, y)
            next_board = mark_up(next_board, x, y)
            backtrack(i + 1, next_board)

        if _board[x][y] == "4":
            next_board = mark_left(_board, x, y)
            next_board = mark_up(next_board, x, y)
            next_board = mark_right(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_up(_board, x, y)
            next_board = mark_right(next_board, x, y)
            next_board = mark_down(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_right(_board, x, y)
            next_board = mark_down(next_board, x, y)
            next_board = mark_left(next_board, x, y)
            backtrack(i + 1, next_board)

            next_board = mark_down(_board, x, y)
            next_board = mark_left(next_board, x, y)
            next_board = mark_up(next_board, x, y)
            backtrack(i + 1, next_board)

    backtrack(0, board)
    return ans


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [sys_input().split() for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
