""" solve.py for 19236번. 청소년 상어 """

import sys


Board = list[list[tuple[int, int]]]
PosMap = list[tuple[int, int] | None]
Pos = tuple[int, int]


DIRECTIONS = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def move_fish(board: Board, pos_map: PosMap, shark_pos: Pos) -> tuple[Board, PosMap]:
    new_board, new_pos_map = [row[::] for row in board], pos_map[::]
    for fish_no in range(1, 17):
        if not new_pos_map[fish_no]:
            continue
        x, y = new_pos_map[fish_no]
        fish_d = new_board[x][y][1]
        for _ in range(8):
            nx, ny = x + DIRECTIONS[fish_d][0], y + DIRECTIONS[fish_d][1]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != shark_pos:
                swap_no = new_board[nx][ny][0]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], (fish_no, fish_d)
                new_pos_map[fish_no] = (nx, ny)
                if swap_no != 0:
                    new_pos_map[swap_no] = (x, y)
                break
            fish_d = (fish_d % 8) + 1

    return new_board, new_pos_map


def eat(board: Board, pos_map: PosMap, shark_pos: Pos) -> Pos:
    x, y = shark_pos
    fish_no, fish_d = board[x][y]

    board[x][y] = (0, 0)
    pos_map[fish_no] = None
    return fish_no, fish_d


def solve(fish_info: list[list[int]]) -> int:
    max_score = 0

    def backtrack(curr_board: Board, curr_pos_map: PosMap, shark_pos: Pos,
                  shark_d: int, score: int) -> None:
        nonlocal max_score

        # 물고기 움직이기
        moved_board, moved_pos_map = move_fish(curr_board, curr_pos_map, shark_pos)

        # 상어 움직이기 + 먹기
        dx, dy = DIRECTIONS[shark_d]
        nx, ny = shark_pos[0] + dx, shark_pos[1] + dy
        shark_moved = False

        while 0 <= nx < 4 and 0 <= ny < 4:
            if moved_board[nx][ny][0] != 0:
                shark_moved = True
                next_board, next_pos_map = [row[::] for row in moved_board], moved_pos_map[::]
                fish_no, fish_d = eat(next_board, next_pos_map, (nx, ny))
                backtrack(next_board, next_pos_map, (nx, ny), fish_d, score + fish_no)
            nx += dx
            ny += dy

        if not shark_moved:
            max_score = max(max_score, score)

    board: Board = [list(zip(row[::2], row[1::2])) for row in fish_info]
    pos_map: PosMap = [None for _ in range(17)]
    for x in range(4):
        for y in range(4):
            pos_map[board[x][y][0]] = (x, y)

    fish_no, fish_d = eat(board, pos_map, (0, 0))
    backtrack(board, pos_map, (0, 0), fish_d, fish_no)
    return max_score


def main() -> None:
    fish_info = [list(map(int, sys_input().split())) for _ in range(4)]

    answer: int = solve(fish_info)
    print(answer)


if __name__ == "__main__":
    main()
