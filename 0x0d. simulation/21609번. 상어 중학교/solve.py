""" solve.py for 21609번. 상어 중학교 """

import sys
from collections import deque


Board2D = list[list[int]]


DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
RAINBOW_BLOCK = 0
BLACK_BLOCK = -1
EMPTY_BLOCK = -2


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate_ccw(board: Board2D) -> Board2D:
    return [list(row) for row in zip(*board)][::-1]


def gravity(board: Board2D) -> None:
    n = len(board)
    for x in range(n - 2, -1, -1):
        for y in range(n):
            block = board[x][y]
            if block >= RAINBOW_BLOCK:
                nx = x + 1
                while nx < n and board[nx][y] == EMPTY_BLOCK:
                    board[nx - 1][y] = EMPTY_BLOCK
                    board[nx][y] = block
                    nx += 1


def find_largest_group(board: Board2D) -> list[tuple[int, int]]:
    largest_group = []
    largest_rainbow_cnt = 0

    def bfs(sx: int, sy: int) -> None:
        nonlocal largest_group, largest_rainbow_cnt
        color = board[sx][sy]
        rainbow_blocks = []
        curr_group = [(sx, sy)]

        queue = deque([(sx, sy)])
        visited[sx][sy] = True

        while queue:
            x, y = queue.popleft()
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if board[nx][ny] < RAINBOW_BLOCK:
                    continue
                if board[nx][ny] in {RAINBOW_BLOCK, color} and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    curr_group.append((nx, ny))
                    if board[nx][ny] == RAINBOW_BLOCK:
                        rainbow_blocks.append((nx, ny))

        if len(curr_group) == 1:
            return

        if (len(curr_group) > len(largest_group)
            or (len(curr_group) == len(largest_group)
                and len(rainbow_blocks) >= largest_rainbow_cnt)):
            largest_group = curr_group
            largest_rainbow_cnt = len(rainbow_blocks)

        for x, y in rainbow_blocks:
            visited[x][y] = False

    n = len(board)
    visited = [[False] * n for _ in range(n)]

    for x in range(n):
        for y in range(n):
            if board[x][y] > RAINBOW_BLOCK and not visited[x][y]:
                bfs(x, y)

    return largest_group


def solve(board: Board2D) -> int:
    score = 0

    while True:
        largest_group = find_largest_group(board)
        if not largest_group:
            break
        score += len(largest_group) ** 2
        for x, y in largest_group:
            board[x][y] = EMPTY_BLOCK

        gravity(board)
        board = rotate_ccw(board)
        gravity(board)

    return score


def main() -> None:
    n, _ = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(board)
    print(answer)


if __name__ == "__main__":
    main()
