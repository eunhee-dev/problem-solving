""" solve.py for 10026번. 적록색약 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def flood_fill(paint: list[str], is_color_blind: bool = False) -> int:
    n = len(paint)
    m = len(paint[0])
    visited = [[False] * m for _ in range(n)]
    cnt = 0

    def bfs(start: tuple[int, int], colors: set[str]) -> None:
        queue = deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <=ny < m and paint[nx][ny] in colors and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                curr_color = paint[x][y]
                if is_color_blind and curr_color in "RG":
                    bfs((x, y), {"R", "G"})
                else:
                    bfs((x, y), {curr_color})
                cnt += 1
    return cnt


def solve(paint: list[str]) -> tuple[int, int]:
    normal_cnt = flood_fill(paint)
    color_blind_cnt = flood_fill(paint, is_color_blind=True)
    return normal_cnt, color_blind_cnt


def main() -> None:
    n = int(sys_input())
    paint = [sys_input() for _ in range(n)]

    answer: tuple[int, int] = solve(paint)
    print(f"{answer[0]} {answer[1]}")


if __name__ == "__main__":
    main()
