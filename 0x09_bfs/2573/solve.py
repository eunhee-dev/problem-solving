""" solve.py for 2573번. 빙산 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[list[int]],
        visited: list[list[bool]], start: tuple[int, int]) -> None:
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


def solve(n: int, m:int, board: list[list[int]]) -> int:
    year = 0
    area = 1  # 문제 조건 (한 덩어리의 빙산이 주어질 때, ...)

    while area > 0:
        melting_board = [[0] * m for _ in range(n)]
        year += 1

        # 녹을 빙산 계산
        for x in range(n):
            for y in range(m):
                if board[x][y] == 0:  # 바닷물은 스킵해주면 더 효율적임
                    continue
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if board[nx][ny] == 0:
                        melting_board[x][y] += 1

        # 실제로 빙산 녹이기
        for x in range(n):
            for y in range(m):
                if board[x][y] > 0:  # 바닷물은 스킵해주면 더 효율적임
                    curr_height = board[x][y] - melting_board[x][y]
                    board[x][y] = curr_height if curr_height > 0 else 0

        # bfs를 통한 빙산 덩어리 개수 카운트
        visited = [[False] * m for _ in range(n)]
        area = 0

        for x in range(n):
            for y in range(m):
                if board[x][y] != 0 and not visited[x][y]:
                    bfs(n, m, board, visited, (x, y))
                    area += 1

        if area >= 2:
            break

    return year if area > 0 else 0


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
