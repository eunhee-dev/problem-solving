""" solve.py for 16236번. 아기 상어 """

import sys
from collections import deque


DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(board: list[list[int]], start: tuple[int, int], size: int) -> tuple[int ,tuple[int, int]]:
    n = len(board)
    queue = deque([start])
    visited = [[False] * n for _ in range(n)]
    distance = 1
    candidates = []
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if visited[nx][ny] or board[nx][ny] > size:
                    continue

                visited[nx][ny] = True
                queue.append((nx, ny))

                if 0 < board[nx][ny] < size:
                    candidates.append((nx, ny))

        if candidates:
            x, y = min(candidates)
            board[x][y] = 0
            return distance, (x, y)

        distance += 1

    return -1, (-1, -1)


def solve(n: int, board: list[list[int]]) -> int:
    elapsed_time = 0
    size = 2

    baby_shark = next((x, y) for x in range(n) for y in range(n) if board[x][y] == 9)
    board[baby_shark[0]][baby_shark[1]] = 0

    while True:
        for _ in range(size):
            distance, baby_shark = bfs(board, baby_shark, size)
            if distance == -1:
                return elapsed_time
            elapsed_time += distance
        size += 1


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
