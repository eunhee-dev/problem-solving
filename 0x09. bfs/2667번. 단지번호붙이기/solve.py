""" solve.py for 2667번. 단지번호붙이기 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, board: list[str],
        visited: list[list[bool]], start: tuple[int, int]) -> int:
    queue = deque([start])
    visited[start[0]][start[1]] = True
    area = 0

    while queue:
        x, y = queue.popleft()
        area += 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == "1":
                visited[nx][ny] = True
                queue.append((nx, ny))
    return area


def solve(n: int, board: list[str]) -> tuple[int, list[int]]:
    visited = [[False] * n for _ in range(n)]
    area_list = []

    for x in range(n):
        for y in range(n):
            if board[x][y] == "1" and not visited[x][y]:
                area_list.append(bfs(n, board, visited, (x, y)))

    return len(area_list), sorted(area_list)


def main() -> None:
    n = int(sys_input())
    board = [sys_input() for _ in range(n)]

    answer: tuple[int, list[int]] = solve(n, board)
    print(answer[0])
    for i in range(answer[0]):
        print(answer[1][i])


if __name__ == '__main__':
    main()
