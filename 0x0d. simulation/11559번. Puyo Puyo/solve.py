""" solve.py for 11559번. Puyo Puyo """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check_adjacent_bfs(board: list[list[str]], visited: list[list[bool]],
                       start: tuple[int, int]) -> int:
    queue = deque([start])
    visited[start[0]][start[1]] = True
    adjacent_puyos = []

    while queue:
        x, y = queue.popleft()
        adjacent_puyos.append((x, y))
        color = board[x][y]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 12 and 0 <= ny < 6):
                continue
            if board[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return adjacent_puyos


def explode(board: list[list[str]], explode_candidates: list[tuple[int, int]]) -> None:
    for x, y in explode_candidates:
        board[x][y] = "."

    for y in range(6):
        puyo_in_col = []
        for x in range(12):
            if board[x][y] != ".":
                puyo_in_col.append(board[x][y])
                board[x][y] = "."
        for x, puyo in enumerate(reversed(puyo_in_col)):
            board[11-x][y] = puyo


def solve(board: list[list[str]]) -> int:
    streak = 0
    while True:
        is_exploded = False
        visited = [[False] * 6 for _ in range(12)]
        explode_candidates = []
        for x in range(12):
            for y in range(6):
                if board[x][y] == ".":
                    continue
                if visited[x][y]:
                    continue
                adjacent_puyos = check_adjacent_bfs(board, visited, (x, y))
                if len(adjacent_puyos) >= 4:
                    explode_candidates.extend(adjacent_puyos)
                    is_exploded = True

        if not is_exploded:
            break

        explode(board, explode_candidates)
        streak += 1

    return streak


def main() -> None:
    board = [list(sys_input()) for _ in range(12)]

    answer: int = solve(board)
    print(answer)


if __name__ == "__main__":
    main()
