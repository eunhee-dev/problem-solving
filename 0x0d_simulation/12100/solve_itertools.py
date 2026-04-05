""" solve_itertools.py for 12100번. 2048 (Easy) """

import sys
from itertools import product


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate(n: int, board: list[list[int]]) -> list[list[int]]:
    rot_board = [[0] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            rot_board[x][y] = board[n - 1 - y][x]
    return rot_board


def move(n: int, board: list[list[int]], direction: int) -> list[list[int]]:
    for _ in range(direction):
        board = rotate(n, board)
    new_board = [[0] * n for _ in range(n)]
    for i, row in enumerate(board):
        blocks = []  # (block, is_merged)
        for block in row:
            if block != 0:
                if blocks and blocks[-1][0] == block and not blocks[-1][1]:
                    blocks.append((blocks.pop()[0] + block, True))
                else:
                    blocks.append((block, False))
        for j, (block, _) in enumerate(blocks):
            new_board[i][j] = block
    for _ in range(4 - direction):
        new_board = rotate(n, new_board)
    return new_board


def solve(n: int, board: list[list[int]]) -> int:
    max_block = 0

    for dir_comb in product(range(4), repeat=5):
        new_board = [row[:] for row in board]
        for direction in dir_comb:
            new_board = move(n, new_board, direction)
        max_block = max(max_block, max(max(row) for row in new_board))

    return max_block


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
