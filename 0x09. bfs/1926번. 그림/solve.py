""" solve.py for 1926번. 그림 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, board: list[list[int]],
        visited: list[list[bool]], start: tuple[int, int]) -> int:
    """ 
    Note:
        `visited` 리스트는 함수 내부에서 직접 수정됩니다. 
        따라서 함수 내 변경 사항이 호출한 쪽의 원본 객체에 반영됩니다.
    """

    size = 1
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1
    return size


def solve(n: int, m: int, board: list[list[int]]) -> tuple[int, int]:
    paints_size = []
    visited = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and board[i][j] == 1:
                size = bfs(n, m, board, visited, start=(i, j))
                paints_size.append(size)
    return len(paints_size), max(paints_size) if paints_size else 0


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: tuple[int, int] = solve(n, m, board)
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    main()
