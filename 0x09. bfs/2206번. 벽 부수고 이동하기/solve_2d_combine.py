""" solve_2d.py for 2206번. 벽 부수고 이동하기 """

import sys
from collections import deque
from math import inf


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[list[str]], start: tuple[int, int]) -> list[list[int]]:
    queue = deque([start])
    dist = [[-1] * m for _ in range(n)]
    dist[start[0]][start[1]] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and board[nx][ny] == "0":
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist


def combine_dist(board: list[list[str]], d_min: int | float,
                 start_dist: list[list[int]], end_dist: list[list[int]]) -> int:
    n = len(board)
    m = len(board[0])
    for x in range(n):
        for y in range(m):
            if board[x][y] != "1":
                continue
            starts = []
            ends = []
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                d_start = start_dist[nx][ny]
                d_end = end_dist[nx][ny]
                if d_start != -1:
                    starts.append(d_start)
                if d_end != -1:
                    ends.append(d_end)
            if not (starts and ends):
                continue
            d_min = min(d_min, min(starts) + 1 + min(ends))
    return d_min


def solve(n: int, m: int, board: list[list[str]]) -> int:
    start_dist = bfs(n, m, board, (0, 0))
    d_min = start_dist[n-1][m-1] if start_dist[n-1][m-1] != -1 else inf

    end_dist = bfs(n, m, board, (n-1, m-1))
    d_min = combine_dist(board, d_min, start_dist, end_dist)

    return d_min if d_min != inf else -1


def main() -> None:
    n, m = map(int, input().split())
    board = [list(sys_input()) for _ in range(n)]

    answer: str = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
