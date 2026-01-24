""" solve.py for 7569번. 토마토 """

import sys
from collections import deque


DIRECTIONS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(h: int, n: int, m: int, box: list[list[list[int]]]) -> list[list[list[int]]]:
    starts = [(z, x, y) for z in range(h) for x in range(n) for y in range(m) if box[z][x][y] == 1]
    queue = deque(starts)
    dist = [[[-1] * m for _ in range(n)] for _ in range(h)]
    for z, x, y in starts:
        dist[z][x][y] = 0

    while queue:
        z, x, y = queue.popleft()
        for dz, dx, dy in DIRECTIONS:
            nz, nx, ny = z + dz, x + dx, y + dy
            if not (0 <= nz < h and 0 <= nx < n and 0 <= ny < m):
                continue
            if dist[nz][nx][ny] == -1 and box[nz][nx][ny] == 0:
                dist[nz][nx][ny] = dist[z][x][y] + 1
                queue.append((nz, nx, ny))
    return dist


def solve(h: int, n: int, m: int, box: list[list[list[int]]]) -> int:
    dist = bfs(h, n, m, box)

    min_day = 0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if dist[z][x][y] == -1 and box[z][x][y] != -1:
                    return -1
                min_day = max(min_day, dist[z][x][y])
    return min_day


def main() -> None:
    m, n, h = map(int, sys_input().split())
    box = [[[*map(int, sys_input().split())] for _ in range(n)] for _ in range(h)]

    answer: int = solve(h, n, m, box)
    print(answer)


if __name__ == "__main__":
    main()
