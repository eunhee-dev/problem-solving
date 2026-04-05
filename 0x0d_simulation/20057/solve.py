""" solve.py for 20057번. 마법사 상어와 토네이도 """

import sys


LEFT_MOVE_MAP = [
    (-2, 0, 0.02), (-1, -1, 0.10), (-1, 0, 0.07), (-1, 1, 0.01),
    (0, -2, 0.05), (1, -1, 0.10), (1, 0, 0.07), (1, 1, 0.01),
    (2, 0, 0.02), (0, -1, 0)
]

DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate90(x: int, y: int) -> tuple[int, int]:
    return -y, x


def solve(n: int, board: list[list[int]]) -> int:
    move_map = [LEFT_MOVE_MAP]
    for _ in range(3):
        next_move_map = []
        for x, y, ratio in move_map[-1]:
            x, y = rotate90(x, y)
            next_move_map.append((x, y, ratio))
        move_map.append(next_move_map)

    total = 0
    x = y = n // 2
    d = 0
    size = 1

    while x > 0 or y > 0:
        dx, dy = DIRECTIONS[d]
        for _ in range(size):
            x, y = x + dx, y + dy
            curr_sand = board[x][y]
            if curr_sand == 0:
                continue

            total_moved_sand = 0
            for dmx, dmy, ratio in move_map[d]:
                if (dmx, dmy) == (dx, dy):
                    moved_sand = curr_sand - total_moved_sand
                else:
                    moved_sand = int(curr_sand * ratio)
                    if moved_sand == 0:
                        continue
                    total_moved_sand += moved_sand
                mx, my = x + dmx, y + dmy
                if not (0 <= mx < n and 0 <= my < n):
                    total += moved_sand
                else:
                    board[mx][my] += moved_sand

            board[x][y] = 0

        d = (d + 1) % 4
        if d % 2 == 0:
            size += 1

    return total


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
