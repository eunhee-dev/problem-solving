""" solve.py for 17142번. 연구소 3 """

import sys
from itertools import combinations
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def spread_virus_bfs(board: list[list[int]],
                     viruses: list[tuple[int, int]], blank_count: int) -> int:
    n = len(board)

    queue = deque(viruses)
    visited = [[False] * n for _ in range(n)]
    distance = 0

    for x, y in viruses:
        visited[x][y] = True

    while queue:
        if blank_count == 0:
            return distance

        for _ in range(len(queue)):
            x, y = queue.popleft()

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in (0, 2) and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    if board[nx][ny] == 0:
                        blank_count -= 1
                    board[nx][ny] = 3

        distance += 1

    return float("inf")


def solve(n: int, m: int, board: list[list[int]]) -> int:
    min_time = float("inf")
    blank_count = 0
    virus_cands = []
    for x in range(n):
        for y in range(n):
            if board[x][y] == 0:
                blank_count += 1
            elif board[x][y] == 2:
                virus_cands.append((x, y))

    for viruses in combinations(virus_cands, m):
        temp_board = [row[:] for row in board]
        for x, y in viruses:
            temp_board[x][y] = 3

        elapsed_time = spread_virus_bfs(temp_board, viruses, blank_count)
        min_time = min(min_time, elapsed_time)

    return min_time if min_time != float("inf") else -1


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int ,sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
