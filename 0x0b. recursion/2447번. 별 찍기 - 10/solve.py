""" solve.py for 2447번. 별 찍기 - 10 """

import sys
import math


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    assert math.isclose(math.log(n, 3), round(math.log(n, 3)))

    board = []
    sub_n = n // 3
    if sub_n == 1:
        board.append("*" * 3)
        board.append("* *")
        board.append("*" * 3)
    else:
        prev_board = solve(sub_n)
        for i in range(3):
            for row in prev_board:
                if i == 1:
                    board.append(row + " " * sub_n + row)
                else:
                    board.append(row * 3)
    return board


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
