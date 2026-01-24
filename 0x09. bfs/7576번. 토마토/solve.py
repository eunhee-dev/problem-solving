""" solve.py for 7576번. 토마토 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[list[int]]) -> list[list[int]]:
    starts = [(x, y) for x in range(n) for y in range(m) if board[x][y] == 1]
    queue = deque(starts)
    dist = [[-1] * m for _ in range(n)]
    for x, y in starts:
        dist[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and board[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist


def solve(n: int, m: int, board: list[list[int]]) -> int:
    dist = bfs(n, m, board)
    min_day = 0
    for x in range(n):
        for y in range(m):
            if dist[x][y] == -1 and board[x][y] != -1:
                return -1
            min_day = max(min_day, dist[x][y])
    return min_day


def main() -> None:
    m, n = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
