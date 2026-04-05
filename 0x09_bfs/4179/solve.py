""" solve.py for 4179번. 불! """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(r: int, c: int, maze: list[str], starts: list[tuple[int, int]]) -> list[list[int]]:
    dist = [[-1] * c for _ in range(r)]
    queue = deque(starts)
    for x, y in starts:
        dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if maze[nx][ny] == "#" or dist[nx][ny] != -1:
                continue

            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

    return dist


def jihoon_bfs(r: int, c: int, maze: list[str], starts: list[tuple[int, int]],
               fire_map: list[list[int]]) -> int | None:
    dist = [[-1] * c for _ in range(r)]
    queue = deque(starts)
    for x, y in starts:
        dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            nt = dist[x][y] + 1
            # 끝까지 갔으면 최소 시간 return
            if not (0 <= nx < r and 0 <= ny < c):
                return nt
            if maze[nx][ny] == "#" or dist[nx][ny] != -1:
                continue
            # 불이 이미 붙어있는 경우 확인
            if fire_map[nx][ny] != -1 and fire_map[nx][ny] <= nt:
                continue

            dist[nx][ny] = nt
            queue.append((nx, ny))

    return None


def solve(r: int, c: int, maze: list[str]) -> str:
    fire_starts = []
    jihoon_start = tuple()

    for row_index, row in enumerate(maze):
        for col_index, cell in enumerate(row):
            if cell == "F":
                fire_starts.append((row_index, col_index))
            elif cell == "J":
                jihoon_start = (row_index, col_index)

    fire_map = bfs(r, c, maze, fire_starts)
    min_time = jihoon_bfs(r, c, maze, [jihoon_start], fire_map)

    return str(min_time) if min_time else "IMPOSSIBLE"


def main() -> None:
    r, c = map(int, sys_input().split())
    maze = [sys_input() for _ in range(r)]

    answer: str = solve(r, c, maze)
    print(answer)


if __name__ == "__main__":
    main()
