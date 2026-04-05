""" solve_undo.py for 14502번. 연구소 """

import sys
from itertools import combinations
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_safe_area_bfs(board: list[list[int]],
                      viruses: list[tuple[int, int]]) -> tuple[int, list[tuple[int, int]]]:
    n = len(board)
    m = len(board[0])

    queue = deque(viruses)
    visited = [[False] * m for _ in range(n)]
    modified = []

    for x, y in viruses:
        visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                board[nx][ny] = 2
                modified.append((nx, ny))
                queue.append((nx, ny))

    return sum(row.count(0) for row in board), modified


def solve(n: int, m: int, board: list[list[int]]) -> int:
    max_safe_area = 0
    blanks, viruses = [], []
    for x in range(n):
        for y in range(m):
            if board[x][y] == 0:
                blanks.append((x, y))
            elif board[x][y] == 2:
                viruses.append((x, y))

    for new_walls in combinations(blanks, 3):
        for x, y in new_walls:
            board[x][y] = 1

        safe_area, modified = get_safe_area_bfs(board, viruses)
        max_safe_area = max(max_safe_area, safe_area)

        # undo
        for x, y in modified:
            board[x][y] = 0
        for x, y in new_walls:
            board[x][y] = 0

    return max_safe_area


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int ,sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
