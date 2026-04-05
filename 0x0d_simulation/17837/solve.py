""" solve.py for 17837번. 새로운 게임 2 """

import sys


DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, board: list[list[int]], pieces: list[list[int]]) -> int:
    pos_board = [[[] for _ in range(n)] for _ in range(n)]

    for num, (x, y, _) in enumerate(pieces):
        pos_board[x][y].append(num)

    for turn in range(1, 1001):
        for num, (x, y, d) in enumerate(pieces):
            dx, dy = DIRECTIONS[d]
            nx, ny = x + dx, y + dy

            if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                pieces[num][2] = DIRECTIONS.index((-dx, -dy))
                nx, ny = x - dx, y - dy
                if not (0 <= nx < n and 0 <= ny < n) or board[nx][ny] == 2:
                    nx, ny = x, y
                    continue

            idx = pos_board[x][y].index(num)
            moving_pieces = pos_board[x][y][idx:]
            pos_board[x][y] = pos_board[x][y][:idx]

            if board[nx][ny] in (0, 2):
                pos_board[nx][ny].extend(moving_pieces)
            else:
                pos_board[nx][ny].extend(reversed(moving_pieces))

            if len(pos_board[nx][ny]) >= 4:
                return turn

            for m_num in moving_pieces:
                pieces[m_num][0], pieces[m_num][1] = nx, ny

    return -1


def main() -> None:
    n, k = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]
    pieces = [[int(x) - 1 for x in sys_input().split()] for _ in range(k)]

    answer: int = solve(n, board, pieces)
    print(answer)


if __name__ == "__main__":
    main()
