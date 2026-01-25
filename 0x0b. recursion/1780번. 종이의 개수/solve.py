""" solve.py for 1780번. 종이의 개수 """

import sys
from collections import Counter


def sys_input():
    return sys.stdin.readline().rstrip()


def check_equal(board: list[list[str]]) -> str:
    for row in board:
        if any(val != board[0][0] for val in row):
            return "Not Equal"
    return board[0][0]


def divide(n: int, board: list[list[str]]) -> list[list[list[str]]]:
    sub_boards = [[] for _ in range(9)]
    sub_n = n // 3
    for i, row in enumerate(board):
        base_idx = (i // sub_n) * 3
        sub_boards[base_idx].append(row[:sub_n])
        sub_boards[base_idx + 1].append(row[sub_n:2*sub_n])
        sub_boards[base_idx + 2].append(row[2*sub_n:])
    return sub_boards


def solve(n: int, board: list[list[str]]) -> Counter[str]:
    count = Counter({"-1": 0, "0": 0, "1": 0})
    check_res = check_equal(board)
    if check_res == "Not Equal":
        for sub_board in divide(n, board):
            count += solve(n // 3, sub_board)
    else:
        count[check_res] += 1
    return count


def main() -> None:
    n = int(sys_input())
    board = [sys_input().split() for _ in range(n)]

    answer: Counter[str] = solve(n, board)
    print(answer["-1"])
    print(answer["0"])
    print(answer["1"])


if __name__ == "__main__":
    main()
