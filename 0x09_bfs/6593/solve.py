""" solve.py for 6593번. 상범 빌딩 """

import sys
from collections import deque


DIRECTIONS = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(l: int, r: int, c: int,
        building: list[list[str]], start: tuple[int, int, int]) -> int:
    queue = deque([start])
    dist = [[[-1] * c for _ in range(r)] for _ in range(l)]
    dist[start[0]][start[1]][start[2]] = 0

    while queue:
        z, x, y = queue.popleft()
        if building[z][x][y] == "E":
            return dist[z][x][y]
        for dz, dx, dy in DIRECTIONS:
            nz, nx, ny = z + dz, x + dx, y + dy
            if not (0 <= nz < l and 0 <= nx < r and 0 <= ny < c):
                continue
            if building[nz][nx][ny] != "#" and dist[nz][nx][ny] == -1:
                dist[nz][nx][ny] = dist[z][x][y] + 1
                queue.append((nz, nx, ny))
    return 0


def solve(l: int, r: int, c: int, building: list[list[str]]) -> int:
    # 시작 지점("S") 찾기
    start = next(
        (z, x, y)
        for z, floor in enumerate(building)
        for x, row in enumerate(floor)
        for y, ch in enumerate(row)
        if ch == "S"
    )
    return bfs(l, r, c, building, start)


def main() -> None:
    while True:
        building = []
        l, r, c = map(int, sys_input().split())
        if l == r == c == 0:
            break
        for _ in range(l):
            floor = [sys_input() for _ in range(r)]
            building.append(floor)
            _ = sys_input()

        answer: int = solve(l, r, c, building)
        if answer:
            print(f"Escaped in {answer} minute(s).")
        else:
            print("Trapped!")


if __name__ == "__main__":
    main()
