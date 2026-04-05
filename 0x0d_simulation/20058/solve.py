""" solve.py for 20058번. 마법사 상어와 파이어스톰 """

import sys
from collections import deque


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate_cw(board: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*board[::-1])]


def get_max_area_bfs(board: list[list[int]]) -> int:
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    max_area = 0

    for sx in range(n):
        for sy in range(n):
            if visited[sx][sy] or board[sx][sy] == 0:
                continue
            queue = deque([(sx, sy)])
            visited[sx][sy] = True
            area = 1

            while queue:
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        area += 1
            max_area = max(max_area, area)
    return max_area


def solve(n: int, a: list[list[int]], l_list: list[int]) -> tuple[int, int]:
    size = 2 ** n
    for l in l_list:
        sub_size = 2 ** l

        for x in range(0, size, sub_size):
            for y in range(0, size, sub_size):
                sub_board = [row[y: y + sub_size] for row in a[x: x + sub_size]]
                rot_sub_board = rotate_cw(sub_board)

                for i, row in enumerate(rot_sub_board):
                    for j, val in enumerate(row):
                        a[x + i][y + j] = val

        melted_coords = []
        for x in range(size):
            for y in range(size):
                if a[x][y] == 0:
                    continue
                adj_ice_cnt = sum(1 for dx, dy in DIRECTIONS
                                  if 0 <= x + dx < size and 0 <= y + dy < size and
                                  a[x + dx][y + dy] > 0)
                if adj_ice_cnt < 3:
                    melted_coords.append((x, y))

        for x, y in melted_coords:
            a[x][y] -= 1

    return sum(sum(row) for row in a), get_max_area_bfs(a)



def main() -> None:
    n, _ = map(int, sys_input().split())
    a = [list(map(int, sys_input().split())) for _ in range(2 ** n)]
    l_list = list(map(int, sys_input().split()))

    answer: tuple[int, int] = solve(n, a, l_list)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
