""" solve.py for 23288번. 주사위 굴리기 2 """

import sys
from collections import deque


DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
T, BOT, F, BAK, L, R = 0, 1, 2, 3, 4, 5

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_score_board_bfs(board: list[list[int]]) -> list[list[int]]:
    n, m = len(board), len(board[0])
    score_board = [[0] * m for _ in range(n)]

    for sx in range(n):
        for sy in range(m):
            if score_board[sx][sy] != 0:
                continue

            queue = deque([(sx, sy)])
            visited = {(sx, sy)}

            while queue:
                x, y = queue.popleft()
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < m):
                        continue
                    if board[nx][ny] == board[x][y] and (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))

            for x, y in visited:
                score_board[x][y] = board[x][y] * len(visited)

    return score_board


def roll_dice(dice: list[int], direction: int) -> None:
    top, bottom, front, back, left, right = dice

    if direction == 0:
        dice[T], dice[R], dice[BOT], dice[L] = left, top, right, bottom
    elif direction == 2:
        dice[T], dice[R], dice[BOT], dice[L] = right, bottom, left, top
    elif direction == 1:
        dice[T], dice[F], dice[BOT], dice[BAK] = back, top, front, bottom
    else:
        dice[T], dice[F], dice[BOT], dice[BAK] = front, bottom, back, top


def solve(k: int, board: list[list[int]]) -> int:
    n, m = len(board), len(board[0])
    score = 0
    direction = 0

    score_board = get_score_board_bfs(board)

    # dice = [top, bottom, front, back, left, right]
    dice = [1, 6, 5, 2, 4, 3]
    x, y = 0, 0

    for _ in range(k):
        dx, dy = DIRECTIONS[direction]
        if not (0 <= x + dx < n and 0 <= y + dy < m):
            direction = (direction + 2) % 4
            dx, dy = DIRECTIONS[direction]

        roll_dice(dice, direction)
        nx, ny = x + dx, y + dy
        score += score_board[nx][ny]

        b_score = board[nx][ny]
        if dice[BOT] > b_score:
            direction = (direction + 1) % 4
        elif dice[BOT] < b_score:
            direction = (direction - 1) % 4

        x, y = nx, ny

    return score


def main() -> None:
    n, _, k = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(k, board)
    print(answer)


if __name__ == "__main__":
    main()
