""" solve.py for 2448번. 별 찍기 - 11 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    board = []
    if n == 3:
        board.append("  *  ")
        board.append(" * * ")
        board.append("*****")
    else:
        prev_n = n // 2
        prev_board = solve(prev_n)
        for row in prev_board:
            board.append(" " * prev_n + row + " " * prev_n)
        for row in prev_board:
            board.append(row + " " + row)
    return board


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
