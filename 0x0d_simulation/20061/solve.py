""" solve.py for 20061번. 모노미노도미노 2 """

import sys


BLOCK_OFFSETS = {
    1: (0, 0),
    2: (0, 1),
    3: (1, 0)
}


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def delete_row(board: list[list[int]], row: int) -> None:
    del board[row]
    board.insert(0, [0, 0, 0, 0])


def add_block(board: list[list[int]], t: int, col: int) -> None:
    dr, dc = BLOCK_OFFSETS[t]
    row = 0
    while row + dr < 5 and board[row + 1][col] == 0 and board[row + 1 + dr][col + dc] == 0:
        row += 1
    board[row][col], board[row + dr][col + dc] = 1, 1


def check_filled(board: list[list[int]]) -> int:
    for r in range(5, 1, -1):
        if all(board[r][c] for c in range(4)):
            board[r] = [0, 0, 0, 0]
            return r
    return 0


def play(board: list[list[int]], t: int, col: int) -> int:
    score = 0

    # 블록 추가
    add_block(board, t, col)

    # 완성된 행 체크하여 제거
    while row := check_filled(board):
        score += 1
        delete_row(board, row)

    # 연한 칸에 블록이 있는 경우 처리
    for _ in range(2):
        if any(board[1][c] for c in range(4)):
            delete_row(board, 5)

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

    return score, sum(v != 0 for row in green + blue for v in row)


def main() -> None:
    n = int(sys_input())
    blocks = [tuple(map(int, sys_input().split())) for _ in range(n)]

    answer: tuple[int, int] = solve(blocks)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
