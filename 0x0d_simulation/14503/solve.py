""" solve.py for 14503번. 로봇 청소기 """

import sys


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(board: list[list[int]], r: int, c: int, d: int) -> int:
    count = 0

    while True:
        if board[r][c] == 0:
            board[r][c] = 2
            count += 1

        can_clean_nearby = any(
            board[r + dr][c + dc] == 0
            for dr, dc in DIRECTIONS
        )

        if not can_clean_nearby:
            dr, dc = DIRECTIONS[(d + 2) % 4]
            nr, nc = r + dr, c + dc
            if board[nr][nc] == 1:
                break
        else:
            for _ in range(4):
                d = (d - 1) % 4
                dr, dc = DIRECTIONS[d]
                nr, nc = r + dr, c + dc
                if board[nr][nc] == 0:
                    break

        r, c = nr, nc

    return count


def main() -> None:
    n, _ = map(int, sys_input().split())
    r, c, d = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(board, r, c, d)
    print(answer)


if __name__ == "__main__":
    main()
