""" solve_naive.py for 4991번. 로봇 청소기 """

import sys
from collections import deque
from itertools import permutations


DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(board: list[list[str]], start: tuple[int, int]) -> dict[tuple[int, int], int]:
    h = len(board)
    w = len(board[0])
    dist = {}
    distance = 0

    queue = deque([start])
    visited = [[False] * w for _ in range(h)]
    visited[start[0]][start[1]] = True

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] in ("*", "o"):
                dist[(x, y)] = distance

            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w):
                    continue
                if not visited[nx][ny] and board[nx][ny] != "x":
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        distance += 1

    return dist


def solve(w: int, h: int, board: list[list[str]]) -> int:
    min_move = float("inf")
    robot_coord = None
    dirty_coords = []

    for x in range(h):
        for y in range(w):
            if board[x][y] == "o":
                robot_coord = (x, y)
            elif board[x][y] == "*":
                dirty_coords.append((x, y))

    points = [robot_coord] + dirty_coords

    dist = {}
    for p1 in points:
        dist[p1] = {}
        p1_dist = bfs(board, p1)
        if len(p1_dist) != len(points):
            return -1
        dist[p1] = p1_dist

    for order in permutations(dirty_coords):
        curr_move = dist[robot_coord][order[0]]

        for p1, p2 in zip(order, order[1:]):
            curr_move += dist[p1][p2]

        min_move = min(min_move, curr_move)

    return min_move


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
