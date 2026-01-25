""" solve.py for 23289번. 온풍기 안녕! """

import sys
from itertools import product
from collections import deque


Coord = tuple[int, int]
Board2d = list[list[int]]


DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def is_valid(n: int, m: int,
             x: int, y: int, nx: int, ny: int, walls: set[frozenset[Coord]]) -> bool:
    return 0 <= nx < n and 0 <= ny < m and {(x, y), (nx, ny)} not in walls


def heat(n: int, m: int,
         heaters: list[tuple[int, int, int]], walls: set[frozenset[Coord]]) -> Board2d:
    heat_board = [[0] * m for _ in range(n)]

    for hx, hy, hd in heaters:
        move_d = [DIRECTIONS[d] for d in range(4) if (d < 2) != (hd < 2)]

        sx, sy = hx + DIRECTIONS[hd][0], hy + DIRECTIONS[hd][1]
        queue = deque([(sx, sy, 5)])  # 온풍기의 바람이 나오는 방향에 있는 칸은 항상 존재한다.
        visited = {(sx, sy)}

        while queue:
            x, y, temperature = queue.popleft()
            if temperature == 0:
                continue
            heat_board[x][y] += temperature

            move_move_d = [(x, y)]
            for dx, dy in move_d:
                nx, ny = x + dx, y + dy
                if is_valid(n, m, x, y, nx, ny, walls):
                    move_move_d.append((nx, ny))

            dx, dy = DIRECTIONS[hd]
            for x, y in move_move_d:
                nx, ny = x + dx, y + dy
                if is_valid(n, m, x, y, nx, ny, walls) and (nx, ny) not in visited:
                    queue.append((nx, ny, temperature - 1))
                    visited.add((nx, ny))

    return heat_board


def circulate(board: Board2d, walls: set[frozenset[Coord]]) -> None:
    n, m = len(board), len(board[0])

    diff_board = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            for dx, dy in (DIRECTIONS[0], DIRECTIONS[3]):
                nx, ny = x + dx, y + dy
                if is_valid(n, m, x, y, nx, ny, walls):
                    diff = int((board[x][y] - board[nx][ny]) / 4)
                    diff_board[x][y] -= diff
                    diff_board[nx][ny] += diff

    for x in range(n):
        for y in range(m):
            board[x][y] += diff_board[x][y]


def solve(k: int, board: Board2d, walls_info: list[tuple[int, int, int]]) -> int:
    n, m = len(board), len(board[0])
    outer_coords = [(x, y) for x, y in product(range(n), range(m))
                    if x == 0 or x == n - 1 or y == 0 or y == m - 1]

    heaters = []
    inspects = []
    for x in range(n):
        for y in range(m):
            if 1 <= board[x][y] <= 4:
                heaters.append((x, y, board[x][y] - 1))
                board[x][y] = 0
            elif board[x][y] == 5:
                inspects.append((x, y))
                board[x][y] = 0

    walls = set()
    for x, y, t in walls_info:
        if t == 0:
            walls.add(frozenset({(x, y), (x - 1, y)}))
        else:
            walls.add(frozenset({(x, y), (x, y + 1)}))

    heat_board = heat(n, m, heaters, walls)

    for chocolate in range(1, 101):
        # heat
        for x in range(n):
            for y in range(m):
                board[x][y] += heat_board[x][y]

        # circulate
        circulate(board, walls)

        # freeze
        for x, y in outer_coords:
            board[x][y] = board[x][y] - 1 if board[x][y] > 0 else 0

        # inspect
        if all(board[x][y] >= k for x, y in inspects):
            return chocolate

    return 101


def main() -> None:
    r, _, k = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(r)]
    w = int(sys_input())
    walls_info = [(x - 1, y - 1, t)
                  for x, y, t in (map(int, sys_input().split()) for _ in range(w))]

    answer: int = solve(k, board, walls_info)
    print(answer)


if __name__ == "__main__":
    main()
