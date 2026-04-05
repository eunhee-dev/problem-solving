""" solve.py for 2206번. 벽 부수고 이동하기 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MAX_BROKEN = 1


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[str]) -> int:
    queue = deque([(0, 0, 0)])
    dist = [[[-1] * (MAX_BROKEN + 1) for _ in range(m)] for _ in range(n)]
    dist[0][0][0] = 1

    while queue:
        x, y, broken_cnt = queue.popleft()
        if (x, y) == (n-1, m-1):
            return dist[x][y][broken_cnt]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            next_dist = dist[x][y][broken_cnt] + 1
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if board[nx][ny] == "0" and dist[nx][ny][broken_cnt] == -1:
                dist[nx][ny][broken_cnt] = next_dist
                queue.append((nx, ny, broken_cnt))
            if board[nx][ny] == "1" and broken_cnt < MAX_BROKEN and dist[nx][ny][broken_cnt + 1] == -1:
                dist[nx][ny][broken_cnt + 1] = next_dist
                queue.append((nx, ny, broken_cnt + 1))
    return -1


def solve(n: int, m: int, board: list[str]) -> int:
    return bfs(n, m, board)


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [sys_input().rstrip() for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
