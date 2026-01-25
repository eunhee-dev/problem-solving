""" solve.py for 2630번. 색종이 만들기 """

import sys
from collections import Counter


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check_equal(board: list[list[str]]) -> str:
    for row in board:
        if any(val != board[0][0] for val in row):
            return "Not Equal"
    return board[0][0]


def divide(sub_n: int, board: list[list[str]]) -> list[list[list[str]]]:
    sub_boards = [[] for _ in range(4)]
    for i, row in enumerate(board):
        base_idx = (i // sub_n) * 2
        sub_boards[base_idx].append(row[:sub_n])
        sub_boards[base_idx + 1].append(row[sub_n:])
    return sub_boards


def solve(n: int, board: list[list[str]]) -> Counter[str]:
    count = Counter({"0": 0, "1": 0})
    check_res = check_equal(board)
    if check_res == "Not Equal":
        sub_n = n // 2
        for sub_board in divide(sub_n, board):
            count += solve(sub_n, sub_board)
    else:
        count[check_res] += 1
    return count


def main() -> None:
    n = int(sys_input())
    board = [sys_input().split() for _ in range(n)]

    answer: Counter[str] = solve(n, board)
    print(answer["0"])
    print(answer["1"])


if __name__ == "__main__":
    main()
