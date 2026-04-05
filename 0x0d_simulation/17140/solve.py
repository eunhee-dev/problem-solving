""" solve.py for 17140번. 이차원 배열과 연산 """

import sys
from collections import Counter


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(r: int, c: int, k: int, board: list[list[int]]) -> int:
    elapsed_time = 0
    r, c = r - 1, c - 1

    while elapsed_time <= 100:
        n = len(board)
        m = len(board[0])

        if r < n and c < m and board[r][c] == k:
            return elapsed_time

        if n < m:
            board = list(map(list, zip(*board)))

        # R 연산
        max_len = 0
        for x, row in enumerate(board):
            counter = Counter(num for num in row if num != 0)
            count = sorted(counter.items(), key=lambda x: (x[1], x[0]))
            new_row = [item for pair in count for item in pair]
            if len(new_row) > 100:
                new_row = new_row[:100]
            board[x] = new_row
            max_len = max(max_len, len(new_row))

        board = [row + [0] * (max_len - len(row)) for row in board]

        if n < m:
            board = list(map(list, zip(*board)))

        elapsed_time += 1

    return -1


def main() -> None:
    r, c, k = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(3)]

    answer: int = solve(r, c, k, board)
    print(answer)


if __name__ == "__main__":
    main()
