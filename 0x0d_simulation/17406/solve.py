""" solve.py for 17406번. 배열 돌리기 4 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_rot_board(board: list[list[int]], op: tuple[int, int, int]) -> list[list[int]]:
    rot_board = [row[::] for row in board]
    r, c, s = op
    for i in range(1, s + 1):
        for nc in range(c + i, c - i, -1):
            rot_board[r - i][nc] = board[r - i][nc - 1]
        for nr in range(r + i, r - i, -1):
            rot_board[nr][c + i] = board[nr - 1][c + i]
        for nc in range(c - i, c + i):
            rot_board[r + i][nc] = board[r + i][nc + 1]
        for nr in range(r - i, r + i):
            rot_board[nr][c - i] = board[nr + 1][c - i]
    return rot_board


def solve(board: list[list[int]], ops: list[tuple[int, int, int]]) -> int:
    k = len(ops)
    min_val = sys.maxsize
    is_used = [False] * k

    def backtrack(depth: int, curr_board: list[list[int]]) -> None:
        nonlocal min_val

        if depth == k:
            min_val = min(min_val, min(sum(row) for row in curr_board))
            return

        for i in range(k):
            if is_used[i]:
                continue
            is_used[i] = True
            rot_board = get_rot_board(curr_board, ops[i])
            backtrack(depth + 1, rot_board)
            is_used[i] = False

    backtrack(0, board)

    return min_val


def main() -> None:
    n, _, k = map(int, sys_input().split())
    a = [list(map(int, sys_input().split())) for _ in range(n)]
    ops = [(r - 1, c - 1, s) for r, c, s in (map(int, sys_input().split()) for _ in range(k))]

    answer: int = solve(a, ops)
    print(answer)


if __name__ == "__main__":
    main()
