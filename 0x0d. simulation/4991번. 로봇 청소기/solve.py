""" solve.py for 4991번. 로봇 청소기 """

import sys
from collections import deque


DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(board: list[list[str]], dirty_coords: list[tuple[int, int]], start: tuple[int, int]) -> int:
    h = len(board)
    w = len(board[0])
    dirty_index = {(x, y): i for i, (x, y) in enumerate(dirty_coords)}

    queue = deque([(start[0], start[1], 0)])
    visited = [[[False] * (1 << len(dirty_coords)) for _ in range(w)] for _ in range(h)]
    visited[start[0]][start[1]][0] = True
    distance = 0

    while queue:
        for _ in range(len(queue)):
            x, y, mask = queue.popleft()

            if mask == (1 << len(dirty_coords)) - 1:
                return distance

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == "x":
                    continue

                new_mask = mask
                if board[nx][ny] == "*":
                    new_mask |= (1 << dirty_index[(nx, ny)])

                if not visited[nx][ny][new_mask]:
                    visited[nx][ny][new_mask] = True
                    queue.append((nx, ny, new_mask))
        distance += 1

    return -1


def solve(w: int, h: int, board: list[list[str]]) -> int:
    robot_coord = None
    dirty_coords = []

    for x in range(h):
        for y in range(w):
            if board[x][y] == "o":
                robot_coord = (x, y)
            elif board[x][y] == "*":
                dirty_coords.append((x, y))

    return bfs(board, dirty_coords, robot_coord)


def main() -> None:
    while True:
        w, h = map(int, sys_input().split())
        if (w, h) == (0, 0):
            break
        board = [list(sys_input()) for _ in range(h)]

        answer: int = solve(w, h, board)
        print(answer)


if __name__ == "__main__":
    main()
