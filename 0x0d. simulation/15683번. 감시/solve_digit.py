""" solve_digit.py for 15683번. 감시 """

import sys


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상, 우, 하, 좌

CCTV_MODES = {
    "1": [[0], [1], [2], [3]],
    "2": [[0, 2], [1, 3]],
    "3": [[0, 1], [1, 2], [2, 3], [3, 0]],
    "4": [[0, 1, 3], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    "5": [[0, 1, 2, 3]]
}


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def mark(board: list[list[str]], x: int, y: int, dir_comb: list[int]) -> list[tuple[int, int]]:
    n, m = len(board), len(board[0])
    modified = []
    for d in dir_comb:
        dx, dy = DIRECTIONS[d]
        nx, ny = x, y
        while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != "6":
            if board[nx][ny] == "0":
                board[nx][ny] = "#"
                modified.append((nx, ny))
            nx, ny = nx + dx, ny + dy
    return modified


def unmark(board: list[list[str]], modified: list[tuple[int, int]]) -> None:
    for x, y in modified:
        board[x][y] = "0"


def count_blind_spots(board: list[list[str]]) -> int:
    return sum(1 if val == "0" else 0 for row in board for val in row)


def solve(n: int, m: int, board: list[list[str]]) -> int:
    ans = float("inf")
    cctv = []
    for x in range(n):
        for y in range(m):
            cctv_mode = board[x][y]
            if cctv_mode == "5":
                _ = mark(board, x, y, CCTV_MODES["5"][0])
            elif cctv_mode in ("1", "2", "3", "4"):
                cctv.append((x, y, cctv_mode))

    for tmp in range(1 << (2 * len(cctv))):  # 4 ** len(cctv)
        modified = []
        for x, y, cctv_mode in cctv:
            tmp, choice = divmod(tmp, 4)
            if cctv_mode == "2":
                choice %= 2
            dir_comb = CCTV_MODES[cctv_mode][choice]
            modified.extend(mark(board, x, y, dir_comb))
        ans = min(ans, count_blind_spots(board))
        unmark(board, modified)

    return ans


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [sys_input().split() for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
