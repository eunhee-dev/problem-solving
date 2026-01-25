""" solve.py for 19238번. 스타트 택시 """

import sys
from collections import deque


Board = list[list[int]]
Coord = tuple[int, int]


DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def pick_up_bfs(board: Board, start: Coord) -> tuple[int, int]:
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dist = 0
    pick_up_list = []

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] > 1:
                pick_up_list.append((x, y))
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if not visited[nx][ny] and board[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

        if pick_up_list:
            pick_up_list.sort(key=lambda x: (x[0], x[1]))
            px, py = pick_up_list[0]
            return board[px][py], dist

        dist += 1

    return -1, -1


def drop_off_bfs(board: Board, start: Coord, end: Coord) -> int:
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dist = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == end:
                return dist
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if not visited[nx][ny] and board[nx][ny] != 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        dist += 1

    return -1


def solve(fuel: int, board: Board, taxi_start: Coord, pass_info: list[list[int]]) -> int:
    passengers = {}
    for i, (s_x, s_y, d_x, d_y) in enumerate(pass_info):
        board[s_x][s_y] = i + 2
        passengers[i + 2] = ((s_x, s_y), (d_x, d_y))

    while passengers:
        next_pass, pick_up_dist = pick_up_bfs(board, taxi_start)
        if next_pass == -1 or fuel < pick_up_dist:
            return -1

        taxi_start, taxi_end = passengers[next_pass]
        fuel -= pick_up_dist

        board[taxi_start[0]][taxi_start[1]] = 0

        drop_off_dist = drop_off_bfs(board, taxi_start, taxi_end)
        if drop_off_dist == -1 or fuel < drop_off_dist:
            return -1

        taxi_start = taxi_end
        fuel += drop_off_dist

        del passengers[next_pass]

    return fuel


def main() -> None:
    n, m, fuel = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]
    taxi_start = tuple(map(lambda x: x - 1, map(int, sys_input().split())))
    pass_info = [list(map(lambda x: x - 1, map(int, sys_input().split()))) for _ in range(m)]

    answer: int = solve(fuel, board, taxi_start, pass_info)
    print(answer)


if __name__ == "__main__":
    main()
