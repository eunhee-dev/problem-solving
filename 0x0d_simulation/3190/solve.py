""" solve.py for 3190번. 뱀 """

import sys
from collections import deque


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def move_snake(n: int, d: int, board: list[list[int]], snake: deque[tuple[int, int]]) -> bool:
    head_x, head_y = snake[0]
    dx, dy = DIRECTIONS[d]
    nx, ny = head_x + dx, head_y + dy

    if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 1:
        return True

    if board[nx][ny] == 0:
        tail_x, tail_y = snake.pop()
        board[tail_x][tail_y] = 0

    board[nx][ny] = 1
    snake.appendleft((nx, ny))
    return False


def solve(n: int, apples: list[tuple[int, int]], ops: list[tuple[int, str]]) -> int:
    board = [[0] * n for _ in range(n)]
    for x, y in apples:
        board[x - 1][y - 1] = 2

    snake = deque([(0, 0)])
    board[0][0] = 1
    direction = 1
    time = 0
    op_idx = 0

    while True:
        time += 1
        is_finished = move_snake(n, direction, board, snake)
        if is_finished:
            break

        if op_idx < len(ops) and ops[op_idx][0] == time:
            rot = ops[op_idx][1]
            if rot == "L":
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4
            op_idx += 1
    return time


def main() -> None:
    n = int(sys_input())
    k = int(sys_input())
    apples = [tuple(map(int, sys_input().split())) for _ in range(k)]
    l = int(sys_input())
    ops = [(int(data[0]), data[1]) for data in (sys_input().split() for _ in range(l))]

    answer: int = solve(n, apples, ops)
    print(answer)


if __name__ == "__main__":
    main()
