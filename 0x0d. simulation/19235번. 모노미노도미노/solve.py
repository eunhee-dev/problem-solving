""" solve.py for 19235번. 모노미노도미노 """

import sys
from itertools import count


BLOCK_OFFSETS = {
    1: (0, 0),
    2: (0, 1),
    3: (1, 0)
}

block_id = count(1)


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def add_block(board: list[list[int]], t: int, row: int, col: int) -> None:
    dr, dc = BLOCK_OFFSETS[t]
    while row + dr < 5 and board[row + 1][col] == 0 and board[row + 1 + dr][col + dc] == 0:
        row += 1
    b_id = next(block_id)
    board[row][col], board[row + dr][col + dc] = b_id, b_id


def check_filled(board: list[list[int]]) -> int:
    """ 완성된 행을 위에서부터 탐색하여 하나만 제거 """
    for r in range(2, 6):
        if all(board[r][c] for c in range(4)):
            board[r] = [0, 0, 0, 0]
            return r
    return 0


def play(board: list[list[int]], t: int, col: int) -> int:
    score = 0

    # 블록 추가
    add_block(board, t, 0, col)

    # 완성된 행 체크하여 제거
    while row := check_filled(board):
        score += 1
        for r in range(row, -1, -1):
            for c in range(4):
                if board[r][c] == 0:
                    continue
                if c < 3 and board[r][c] == board[r][c + 1]:
                    board[r][c], board[r][c + 1] = 0, 0
                    add_block(board, 2, r, c)
                elif r < 5 and board[r][c] == board[r + 1][c]:
                    board[r][c], board[r + 1][c] = 0, 0
                    add_block(board, 3, r, c)
                else:
                    board[r][c] = 0
                    add_block(board, 1, r, c)

    # 연한 칸에 블록이 있는 경우 처리
    for _ in range(2):
        if any(board[1][c] for c in range(4)):
            board.pop()
            board.insert(0, [0, 0, 0, 0])

    return score


def solve(blocks: list[tuple[int, int, int]]) -> tuple[int, int]:
    score = 0
    green = [[0] * 4 for _ in range(6)]
    blue = [[0] * 4 for _ in range(6)]

    for t, x, y in blocks:
        if t == 1:
            score += play(green, 1, y)
            score += play(blue, 1, x)

        elif t == 2:
            score += play(green, 2, y)
            score += play(blue, 3, x)

        elif t == 3:
            score += play(green, 3, y)
            score += play(blue, 2, x)

    return score, sum(v != 0 for r in green + blue for v in r)


def main() -> None:
    n = int(sys_input())
    blocks = [tuple(map(int, sys_input().split())) for _ in range(n)]

    answer: tuple[int, int] = solve(blocks)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
