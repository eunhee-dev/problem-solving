""" solve.py for 16985번. Maaaaaaaaaze """

import sys
from collections import deque
from itertools import permutations, product


Board2d = list[list[int]]


DIRECTIONS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(maze: tuple[Board2d, Board2d, Board2d, Board2d, Board2d]) -> int:
    if maze[0][0][0] == 0 or maze[4][4][4] == 0:
        return sys.maxsize

    dist = 0
    queue = deque([(0, 0, 0, 0)])
    visited = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    visited[0][0][0] = True

    while queue:
        z, x, y, dist = queue.popleft()
        if (z, x, y) == (4, 4, 4):
            return dist
        for dz, dx, dy in DIRECTIONS:
            nz, nx, ny = z + dz, x + dx, y + dy
            if not (0 <= nz < 5 and 0 <= nx < 5 and 0 <= ny < 5):
                continue
            if maze[nz][nx][ny] == 1 and not visited[nz][nx][ny]:
                queue.append((nz, nx, ny, dist + 1))
                visited[nz][nx][ny] = True
    return sys.maxsize


def rotate_cw(board: Board2d) -> Board2d:
    return [list(row) for row in zip(*board[::-1])]


def solve(boards: list[Board2d]) -> int:
    min_dist = sys.maxsize
    rotated_boards = []
    for board in boards:
        rotations = []
        rotations.append(board)
        for _ in range(3):
            board = rotate_cw(board)
            rotations.append(board)
        rotated_boards.append(rotations)

    for selected_boards in product(*rotated_boards):
        for maze in permutations(selected_boards):
            curr_dist = bfs(maze)
            min_dist = min(min_dist, curr_dist)
            if min_dist == 12:
                return min_dist

    return min_dist if min_dist != sys.maxsize else -1


def main() -> None:
    boards = [[list(map(int, sys_input().split())) for _ in range(5)] for _ in range(5)]

    answer: int = solve(boards)
    print(answer)


if __name__ == "__main__":
    main()
