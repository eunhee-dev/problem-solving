""" solve_bs.py for 3197번. 백조의 호수 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def melt_bfs(board: list[list[str]],
             queue: deque[tuple[int, int]], melt_days: list[list[int]]) -> None:
    r = len(board)
    c = len(board[0])

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and melt_days[nx][ny] == -1 and board[nx][ny] == 'X':
                melt_days[nx][ny] = melt_days[x][y] + 1
                queue.append((nx, ny))


def swan_bfs(swans: list[tuple[int, int]], melt_days: list[list[int]], mid: int) -> bool:
    r = len(melt_days)
    c = len(melt_days[0])

    queue = deque([swans[0]])
    visited = [[False] * c for _ in range(r)]
    visited[swans[0][0]][swans[0][1]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == swans[1]:
            return True
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and melt_days[nx][ny] <= mid:
                visited[nx][ny] = True
                queue.append((nx, ny))
    return False


def solve(r: int, c: int, board: list[list[str]]) -> int:
    swans = []
    melt_days = [[-1] * c for _ in range(r)]
    queue = deque()
    for x in range(r):
        for y in range(c):
            if board[x][y] == "X":
                continue
            melt_days[x][y] = 0
            queue.append((x, y))
            if board[x][y] == "L":
                swans.append((x, y))

    melt_bfs(board, queue, melt_days)

    low, high = 0, max(max(row) for row in melt_days)
    day = high

    while low <= high:
        mid = (low + high) // 2
        if swan_bfs(swans, melt_days, mid):
            day = mid
            high = mid - 1
        else:
            low = mid + 1

    return day


def main() -> None:
    r, c = map(int, sys_input().split())
    board = [list(sys_input()) for _ in range(r)]

    answer: int = solve(r, c, board)
    print(answer)


if __name__ == "__main__":
    main()
