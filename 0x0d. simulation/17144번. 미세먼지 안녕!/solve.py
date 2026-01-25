""" solve.py for 17144번. 미세먼지 안녕! """

import sys


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(r: int, c: int, t: int, board: list[list[int]]) -> int:
    purifier_rows = [x for x in range(r) if board[x][0] == -1]

    for _ in range(t):
        # 1. 미세먼지 확산
        next_board = [[0] * c for _ in range(r)]
        for px in purifier_rows:
            next_board[px][0] = -1

        for x in range(r):
            for y in range(c):
                if board[x][y] <= 0:
                    continue

                diffused_amount = board[x][y] // 5
                diffusion_count = 0

                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < r and 0 <= ny < c) or board[nx][ny] == -1:
                        continue
                    next_board[nx][ny] += diffused_amount
                    diffusion_count += 1

                next_board[x][y] += board[x][y] - diffusion_count * diffused_amount

        board = next_board

        # 2. 공기청정기 작동
        px = purifier_rows[0]
        for x in range(px - 1, 0, -1):
            board[x][0] = board[x - 1][0]
        for y in range(c - 1):
            board[0][y] = board[0][y + 1]
        for x in range(px):
            board[x][c - 1] = board[x + 1][c - 1]
        for y in range(c - 1, 1, -1):
            board[px][y] = board[px][y - 1]
        board[px][1] = 0

        px = purifier_rows[1]
        for x in range(px + 1, r - 1):
            board[x][0] = board[x + 1][0]
        for y in range(c - 1):
            board[r - 1][y] = board[r - 1][y + 1]
        for x in range(r - 1, px, -1):
            board[x][c - 1] = board[x - 1][c - 1]
        for y in range(c - 1, 0, -1):
            board[px][y] = board[px][y - 1]
        board[px][1] = 0

    return sum(val for row in board for val in row if val > 0)


def main() -> None:
    r, c, t = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(r)]

    answer: int = solve(r, c, t, board)
    print(answer)


if __name__ == "__main__":
    main()
