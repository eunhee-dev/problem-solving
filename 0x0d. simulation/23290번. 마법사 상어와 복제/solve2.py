""" solve2.py for 23290번. 마법사 상어와 복제 """

import sys
from itertools import product


FISH_DIRS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
SHARK_DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s: int, fishes: list[tuple[int, int, int]], shark_pos: tuple[int, int]) -> int:
    board = [[[0] * 8 for _ in range(4)] for _ in range(4)]
    for fx, fy, d in fishes:
        board[fx][fy][d] += 1

    smell_board = [[0] * 4 for _ in range(4)]

    for _ in range(s):
        # 복제 마법 시전
        copied_board = [[board[x][y][:] for y in range(4)] for x in range(4)]

        # 물고기 이동
        next_board = [[[0] * 8 for _ in range(4)] for _ in range(4)]
        for x in range(4):
            for y in range(4):
                for d in range(8):
                    if board[x][y][d] == 0:
                        continue

                    fish_cnt = board[x][y][d]
                    moved = False
                    for rot_cnt in range(8):
                        nd = (d - rot_cnt) % 8
                        nx, ny = x + FISH_DIRS[nd][0], y + FISH_DIRS[nd][1]
                        if (0 <= nx < 4 and 0 <= ny < 4
                            and (nx, ny) != shark_pos and smell_board[nx][ny] == 0):
                            next_board[nx][ny][nd] += fish_cnt
                            moved = True
                            break

                    if not moved:
                        next_board[x][y][d] += fish_cnt
        board = next_board

        # 상어 이동
        max_eaten_fish = -1
        best_shark_path = tuple()

        for path in product(range(4), repeat=3):
            temp_sx, temp_sy = shark_pos
            eaten_fish_cnt = 0
            visited_in_path = set()
            is_valid_path = True

            for d in path:
                temp_sx += SHARK_DIRS[d][0]
                temp_sy += SHARK_DIRS[d][1]

                if not (0 <= temp_sx < 4 and 0 <= temp_sy < 4):
                    is_valid_path = False
                    break

                if (temp_sx, temp_sy) not in visited_in_path:
                    eaten_fish_cnt += sum(board[temp_sx][temp_sy])
                    visited_in_path.add((temp_sx, temp_sy))

            if is_valid_path and eaten_fish_cnt > max_eaten_fish:
                max_eaten_fish = eaten_fish_cnt
                best_shark_path = path

        # 잡아먹기
        sx, sy = shark_pos
        for d in best_shark_path:
            dx, dy = SHARK_DIRS[d]
            sx, sy = sx + dx, sy + dy
            if sum(board[sx][sy]) > 0:
                board[sx][sy] = [0] * 8  # 물고기 제거
                smell_board[sx][sy] = 3  # 냄새 남김 (2턴 후 사라짐, 현재 턴 포함 3)
        shark_pos = (sx, sy)

        # 냄새 제거
        for x in range(4):
            for y in range(4):
                if smell_board[x][y] > 0:
                    smell_board[x][y] -= 1

        # 복제 마법 완료
        for x in range(4):
            for y in range(4):
                for d in range(8):
                    board[x][y][d] += copied_board[x][y][d]

    return sum(sum(board[x][y]) for x in range(4) for y in range(4))


def main() -> None:
    m, s = map(int, sys_input().split())
    fishes = [(fx - 1, fy - 1, d - 1)
              for fx, fy, d in (map(int, sys_input().split()) for _ in range(m))]
    sx, sy = map(int, sys_input().split())

    answer = solve(s, fishes, (sx - 1, sy - 1))
    print(answer)


if __name__ == "__main__":
    main()
