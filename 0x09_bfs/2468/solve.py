""" solve.py for 2468번. 안전 영역 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, board: list[list[int]], visited: list[list[bool]],
        rain: int, start: tuple[int, int]) -> None:
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > rain and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


def solve(n: int, board: list[list[int]]) -> int:
    max_height = max(max(row) for row in board)
    max_count = 0

    for rain in range(0, max_height):
        visited = [[False] * n for _ in range(n)]
        count = 0
        for x in range(n):
            for y in range(n):
                if board[x][y] > rain and not visited[x][y]:
                    bfs(n, board, visited, rain, (x, y))
                    count += 1
        max_count = max(max_count, count)

    return max_count


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
