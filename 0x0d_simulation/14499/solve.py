""" solve.py for 14499번. 주사위 굴리기 """

import sys


DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]
T, BOT, F, BAK, L, R = 0, 1, 2, 3, 4, 5


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def roll_dice(dice: list[int], direction: int) -> None:
    top, bottom, front, back, left, right = dice

    # top, right, bottom, left
    if direction == 1:
        dice[T], dice[R], dice[BOT], dice[L] = left, top, right, bottom
    elif direction == 2:
        dice[T], dice[R], dice[BOT], dice[L] = right, bottom, left, top
    # top, front, bottom, back
    elif direction == 3:
        dice[T], dice[F], dice[BOT], dice[BAK] = front, bottom, back, top
    else:
        dice[T], dice[F], dice[BOT], dice[BAK] = back, top, front, bottom


def solve(n: int, m: int, x: int, y: int, board: list[list[int]], ops: list[int]) -> list[int]:
    top_sides = []

    # dice = [top, bottom, front, back, left, right]
    dice = [0] * 6

    for op in ops:
        dx, dy = DIRECTIONS[op - 1]
        nx, ny = x + dx, y + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue

        roll_dice(dice, op)

        if board[nx][ny] == 0:
            board[nx][ny] = dice[BOT]
        else:
            dice[BOT] = board[nx][ny]
            board[nx][ny] = 0

        top_sides.append(dice[T])
        x, y = nx, ny

    return top_sides


def main() -> None:
    n, m, x, y, _ = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]
    ops = list(map(int, sys_input().split()))

    answer: list[int] = solve(n, m, x, y, board, ops)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
