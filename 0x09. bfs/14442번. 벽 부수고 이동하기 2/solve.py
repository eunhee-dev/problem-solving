""" solve.py for 14442번. 벽 부수고 이동하기 2 """ 
# Python3: 시간 초과, PyPy3: 통과

import sys
from collections import deque


sys_input = sys.stdin.readline
DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(n: int, m: int, k: int, board: list[str]) -> int:
    queue = deque([(0, 0, 0)])
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    distance = 1

    while queue:
        len_queue = len(queue)
        for _ in range(len_queue):
            x, y, broken_cnt = queue.popleft()
            if (x, y) == (n-1, m-1):
                return distance
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if board[nx][ny] == "0" and not visited[nx][ny][broken_cnt]:
                    visited[nx][ny][broken_cnt] = True
                    queue.append((nx, ny, broken_cnt))
                if board[nx][ny] == "1" and broken_cnt < k and not visited[nx][ny][broken_cnt + 1]:
                    visited[nx][ny][broken_cnt + 1] = True
                    queue.append((nx, ny, broken_cnt + 1))
        distance += 1

    return -1


def solve(n: int, m: int, k: int, board: list[str]) -> int:
    return bfs(n, m, k, board)


def main() -> None:
    n, m, k = map(int, sys_input().rstrip().split())
    board = [sys_input().rstrip() for _ in range(n)]

    answer: int = solve(n, m, k, board)
    print(answer)


if __name__ == "__main__":
    main()
