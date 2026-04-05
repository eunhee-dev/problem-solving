""" solve.py for 2583번. 영역 구하기 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(m: int, n: int, board: list[list[int]],
        visited: list[list[bool]], start: tuple[int, int]) -> int:
    queue = deque([start])
    visited[start[0]][start[1]] = True
    area = 0

    while queue:
        x, y = queue.popleft()
        area += 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return area


def solve(m: int, n: int, rect_coord: list[tuple[int, int, int, int]]) -> tuple[int, str]:
    board = [[1] * n for _ in range(m)]

    for x1, y1, x2, y2 in rect_coord:
        for x in range(y1, y2):  # 직교 좌표계 => (행: x, 열: y)로 바꾸기
            for y in range(x1, x2):
                board[x][y] = 0

    visited = [[False] * n for _ in range(m)]
    area_list = []

    for x in range(m):
        for y in range(n):
            if board[x][y] == 1 and not visited[x][y]:
                area_list.append(bfs(m, n, board, visited, (x, y)))

    return len(area_list), " ".join(map(str, sorted(area_list)))


def main() -> None:
    m, n, k = map(int, sys_input().split())
    rect_coord = [tuple(map(int, sys_input().split())) for _ in range(k)]

    answer: tuple[int, str] = solve(m, n, rect_coord)
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    main()
