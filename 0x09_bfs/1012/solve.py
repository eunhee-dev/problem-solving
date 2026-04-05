""" solve.py for 1012번. 유기농 배추 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[list[int]],
        visited: list[list[bool]], start: tuple[int, int]) -> None:
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <=ny < m and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


def solve(n: int, m: int, cabbage_coords: list[tuple[int, int]]) -> int:
    board = [[0] * m for _ in range(n)]
    for x, y in cabbage_coords:
        board[x][y] = 1

    visited = [[False] * m for _ in range(n)]
    cnt = 0

    for x, y in cabbage_coords:
        if not visited[x][y]:
            bfs(n, m, board, visited, (x, y))
            cnt += 1

    return cnt


def main() -> None:
    t = int(sys_input().rstrip())
    for _ in range(t):
        m, n, k = map(int, sys_input().split())
        cabbage_coords = [tuple(map(int, sys_input().split())) for _ in range(k)]
        n, m = m, n  # 행: n / 열: m 으로 조정

        answer: int = solve(n, m, cabbage_coords)
        print(answer)


if __name__ == "__main__":
    main()
