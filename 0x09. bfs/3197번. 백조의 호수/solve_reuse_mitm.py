""" solve_reuse_multi.py for 3197번. 백조의 호수 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def swan_bfs(board: list[list[int]], visited: list[list[bool]],
             queue: deque[tuple[int, int]]) -> tuple[bool, list[tuple[int, int]]]:
    r = len(board)
    c = len(board[0])

    next_day_queue = deque()

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if board[nx][ny] == "X":
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    next_day_queue.append((nx, ny))
            else:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y]
                    queue.append((nx, ny))
                elif visited[nx][ny] != visited[x][y]:
                    return True, []

    return False, next_day_queue


def melt_bfs(board: list[list[str]], queue: deque[tuple[int, int]]) -> list[tuple[int, int]]:
    r = len(board)
    c = len(board[0])

    next_day_queue = deque()

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < r and 0 <= ny < c):
                continue
            if board[nx][ny] == "X":
                board[nx][ny] = "."
                next_day_queue.append((nx, ny))

    return next_day_queue


def solve(r: int, c: int, board: list[list[str]]) -> int:
    swans = []
    water_queue = deque()
    for x in range(r):
        for y in range(c):
            if board[x][y] == "X":
                continue
            water_queue.append((x, y))
            if board[x][y] == "L":
                swans.append((x, y))

    swan_queue = deque([swans[0], swans[1]])
    visited = [[0] * c for _ in range(r)]
    visited[swans[0][0]][swans[0][1]] = 1
    visited[swans[1][0]][swans[1][1]] = 2
    day = 0

    while True:
        is_meet, swan_queue = swan_bfs(board, visited, swan_queue)
        if is_meet:
            return day
        water_queue = melt_bfs(board, water_queue)
        day += 1


def main() -> None:
    r, c = map(int, sys_input().split())
    board = [list(sys_input()) for _ in range(r)]

    answer: int = solve(r, c, board)
    print(answer)


if __name__ == "__main__":
    main()
