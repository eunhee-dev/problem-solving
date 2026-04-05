import sys
from itertools import product


FISHES = dict[int, tuple[int, int, int]]


FISH_DIRS = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
SHARK_DIRS = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s: int, fishes: FISHES, shark_pos: tuple[int, int]) -> int:
    last_fish_idx = len(fishes)
    smell_board = [[0] * 4 for _ in range(4)]

    for _ in range(s):
        # 복제 마법 시전
        copied_fishes: FISHES = {i + last_fish_idx: (x, y, d)
                                 for i, (x, y, d) in enumerate(fishes.values())}
        last_fish_idx += len(copied_fishes)

        # 물고기 이동
        board = [[[] for _ in range(4)] for _ in range(4)]
        for i, (x, y, d) in fishes.items():
            moved = False
            for rot_cnt in range(8):
                nd = (d - rot_cnt) % 8
                nx, ny = x + FISH_DIRS[nd][0], y + FISH_DIRS[nd][1]
                if (0 <= nx < 4 and 0 <= ny < 4
                    and (nx, ny) != shark_pos and smell_board[nx][ny] == 0):
                    fishes[i] = (nx, ny, nd)
                    board[nx][ny].append(i)
                    moved = True
                    break

            if not moved:
                fishes[i] = (x, y, d)
                board[x][y].append(i)

        # 상어 이동
        max_eaten_fish = -1
        best_shark_path = tuple()

        for path in product(range(4), repeat=3):
            temp_sx, temp_sy = shark_pos
            eaten_fish_cnt = 0
            visited = set()
            is_valid_path = True

            for d in path:
                dx, dy = SHARK_DIRS[d]
                nsx, nsy = temp_sx + dx, temp_sy + dy
                if not (0 <= nsx < 4 and 0 <= nsy < 4):
                    is_valid_path = False
                    break
                if (nsx, nsy) not in visited:
                    eaten_fish_cnt += len(board[nsx][nsy])
                    visited.add((nsx, nsy))
                temp_sx, temp_sy = nsx, nsy

            if is_valid_path and eaten_fish_cnt > max_eaten_fish:
                max_eaten_fish = eaten_fish_cnt
                best_shark_path = path

        # 잡아먹기
        sx, sy = shark_pos

        for d in best_shark_path:
            dx, dy = SHARK_DIRS[d]
            sx, sy = sx + dx, sy + dy
            if board[sx][sy]:
                smell_board[sx][sy] = 3  # 냄새 남김 (2턴 후 사라짐, 현재 턴 포함 3)
                for fish_idx in board[sx][sy]:
                    if fish_idx in fishes:
                        del fishes[fish_idx]

        shark_pos = (sx, sy)

        # 냄새 제거
        for x in range(4):
            for y in range(4):
                if smell_board[x][y] > 0:
                    smell_board[x][y] -= 1

        # 복제 완료
        fishes.update(copied_fishes)

    return len(fishes)


def main() -> None:
    m, s = map(int, sys_input().split())
    fishes = {i: (fx - 1, fy - 1, d - 1)
                  for i, (fx, fy, d) in enumerate(map(int, sys_input().split()) for _ in range(m))}
    sx, sy = map(lambda x: int(x) - 1, sys_input().split())

    answer: int = solve(s, fishes, (sx, sy))
    print(answer)


if __name__ == "__main__":
    main()
