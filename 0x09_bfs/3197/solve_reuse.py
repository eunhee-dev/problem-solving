""" solve_reuse.py for 3197번. 백조의 호수 """

import sys
from array import array


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def swan_bfs(board: list[bytearray], visited: list[bytearray],
             swan_queue: array, dest: int) -> tuple[bool, array]:
    r = len(board)
    c = len(board[0])

    for idx in swan_queue:
        x, y = divmod(idx, c)
        visited[x][y] = 1

    next_day_queue = array("I")
    head = 0

    while head < len(swan_queue):
        idx = swan_queue[head]
        head += 1

        if idx == dest:
            return True, array("I")
        x, y = divmod(idx, c)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                visited[nx][ny] = 1
                if board[nx][ny] == ord("X"):
                    next_day_queue.append(nx*c + ny)
                else:
                    swan_queue.append(nx*c + ny)

    return False, next_day_queue


def melt_bfs(board: list[bytearray], water_queue: array) -> array:
    r = len(board)
    c = len(board[0])

    next_day_queue = array("I")

    for idx in water_queue:
        x, y = divmod(idx, c)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == ord("X"):
                board[nx][ny] = ord(".")
                next_day_queue.append(nx*c + ny)

    return next_day_queue


def solve(r: int, c: int, board: list[bytearray]) -> int:
    swans = []
    water_queue = array("I")
    for x in range(r):
        for y in range(c):
            if board[x][y] == ord("X"):
                continue
            water_queue.append(x*c + y)
            if board[x][y] == ord("L"):
                swans.append(x*c + y)

    swan_queue = array("I", [swans[0]])
    visited = [bytearray(c) for _ in range(r)]
    day = 0

    while True:
        is_meet, swan_queue = swan_bfs(board, visited, swan_queue, swans[1])
        if is_meet:
            return day
        water_queue = melt_bfs(board, water_queue)
        day += 1


def main() -> None:
    r, c = map(int, sys_input().split())
    board = [bytearray(sys_input(), "ascii") for _ in range(r)]

    answer: int = solve(r, c, board)
    print(answer)


if __name__ == "__main__":
    main()
