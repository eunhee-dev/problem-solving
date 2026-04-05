""" solve.py for 1992번. 쿼드트리 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check_equal(board: list[str]) -> str:
    for row in board:
        if any(val != board[0][0] for val in row):
            return "Not Equal"
    return board[0][0]


def divide(sub_n :int, board: list[str]) -> list[list[str]]:
    sub_boards = [[] for _ in range(4)]
    for i, row in enumerate(board):
        base_idx = (i // sub_n) * 2
        sub_boards[base_idx].append(row[:sub_n])
        sub_boards[base_idx + 1].append(row[sub_n:])
    return sub_boards


def solve(n: int, board: list[str]) -> str:
    ans = ""
    check_res = check_equal(board)
    if check_res == "Not Equal":
        sub_n = n // 2
        ans += "("
        for sub_board in divide(sub_n, board):
            ans += solve(sub_n, sub_board)
        ans += ")"
    else:
        ans += check_res
    return ans


def main() -> None:
    n = int(sys_input())
    board = [sys_input() for _ in range(n)]

    answer: str = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
