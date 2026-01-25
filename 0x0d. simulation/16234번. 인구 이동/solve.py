""" solve.py for 16234번. 인구 이동 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_union_bfs(l: int, r: int, board: list[list[int]],
                  visited: list[list[bool]], start: tuple[int, int]) -> list[tuple[int, int]]:
    n = len(board)
    union = [start]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        curr_population = board[x][y]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not visited[nx][ny] and l <= abs(curr_population - board[nx][ny]) <= r:
                visited[nx][ny] = True
                queue.append((nx, ny))
                union.append((nx, ny))

    return union


def solve(n: int, l: int, r: int, board: list[list[int]]) -> int:
    day = 0

    while True:
        is_finished = True
        visited = [[False] * n for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if visited[x][y]:
                    continue
                union = get_union_bfs(l, r, board, visited, (x, y))
                if len(union) > 1:
                    is_finished = False
                    total_poulation = sum(board[ux][uy] for ux, uy in union)
                    next_population = total_poulation // len(union)
                    for ux, uy in union:
                        board[ux][uy] = next_population
        if is_finished:
            break
        day += 1

    return day


def main() -> None:
    n, l, r = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, l, r, board)
    print(answer)


if __name__ == "__main__":
    main()
