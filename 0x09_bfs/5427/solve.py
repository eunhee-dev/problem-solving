""" solve.py for 5427번. 불 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(w: int, h: int, building: list[str], starts: list[tuple[int, int]]) -> list[list[int]]:
    queue = deque(starts)
    dist = [[-1] * w for _ in range(h)]
    for start in starts:
        dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and dist[nx][ny] == -1 and building[nx][ny] != "#":
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    return dist


def sanggeun_bfs(w: int, h: int, building: list[str],
                 fire_map: list[list[int]], start: tuple[int, int]) -> int:
    queue = deque([start])
    dist = [[-1] * w for _ in range(h)]
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            nt = dist[x][y] + 1
            if not (0 <= nx < h and 0 <= ny < w):
                return nt
            if dist[nx][ny] != -1 or building[nx][ny] == "#":
                continue
            if fire_map[nx][ny] != -1 and fire_map[nx][ny] <= nt:
                continue
            dist[nx][ny] = nt
            queue.append((nx, ny))
    return -1


def solve(w: int, h: int, building: list[str]) -> str:
    fire_starts = []
    sanggeun_start = ()
    for x in range(h):
        for y in range(w):
            if building[x][y] == "*":
                fire_starts.append((x, y))
            if building[x][y] == "@":
                sanggeun_start = (x, y)

    fire_map = bfs(w, h, building, fire_starts)
    min_time = sanggeun_bfs(w, h, building, fire_map, sanggeun_start)
    return str(min_time) if min_time != -1 else "IMPOSSIBLE"


def main() -> None:
    t = int(sys_input().rstrip())
    for _ in range(t):
        w, h = map(int, sys_input().split())
        building = [sys_input() for _ in range(h)]

        answer: str = solve(w, h, building)
        print(answer)


if __name__ == "__main__":
    main()
