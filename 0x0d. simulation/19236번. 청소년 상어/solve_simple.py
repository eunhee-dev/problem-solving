""" solve_simple.py for 19236번. 청소년 상어 """

import sys


Board = list[list[tuple[int, int]]]
Pos = tuple[int, int]


DIRECTIONS = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def move_fish(board: Board, shark_pos: Pos) -> Board:
    new_board = [row[::] for row in board]
    pos_map = [None] * 17
    for x in range(4):
        for y in range(4):
            pos_map[new_board[x][y][0]] = (x, y)

    for fish_no in range(1, 17):
        if pos_map[fish_no] is None:
            continue
        x, y = pos_map[fish_no]
        d = new_board[x][y][1]
        for _ in range(8):
            nx, ny = x + DIRECTIONS[d][0], y + DIRECTIONS[d][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != shark_pos:
                swap_no = new_board[nx][ny][0]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], (fish_no, d)
                pos_map[fish_no] = (nx, ny)
                if swap_no != 0:
                    pos_map[swap_no] = (x, y)
                break
            d = (d % 8) + 1

    return new_board


def eat(board: Board, shark_pos: Pos) -> tuple[int, int]:
    x, y = shark_pos
    fish_no, fish_d = board[x][y]
    board[x][y] = (0, 0)
    return fish_no, fish_d


def solve(fish_info: list[list[int]]) -> int:
    max_score = 0

    def backtrack(curr_board: Board, shark_pos: Pos, shark_d: int, score: int) -> None:
        nonlocal max_score

        # 물고기 움직이기
        moved_board = move_fish(curr_board, shark_pos)

        # 상어 움직이기 + 먹기
        dx, dy = DIRECTIONS[shark_d]
        nx, ny = shark_pos[0] + dx, shark_pos[1] + dy
        shark_moved = False

        while 0 <= nx < 4 and 0 <= ny < 4:
            if moved_board[nx][ny][0] != 0:
                shark_moved = True
                next_board = [row[::] for row in moved_board]
                fish_no, fish_d = eat(next_board, (nx, ny))
                backtrack(next_board, (nx, ny), fish_d, score + fish_no)
            nx += dx
            ny += dy

        if not shark_moved:
            max_score = max(max_score, score)

    board: Board = [list(zip(row[::2], row[1::2])) for row in fish_info]
    fish_no, fish_d = eat(board, (0, 0))
    backtrack(board, (0, 0), fish_d, fish_no)
    return max_score


def main() -> None:
    fish_info = [list(map(int, sys_input().split())) for _ in range(4)]

    answer: int = solve(fish_info)
    print(answer)


if __name__ == "__main__":
    main()
