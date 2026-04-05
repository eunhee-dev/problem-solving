""" solve.py for 15898번. 피아의 아틀리에 ~신비한 대회의 연금술사~ """
# Python3: 시간 초과, PyPy3: 통과

import sys


Int2d = list[list[int]]

CHAR_TO_INT = {"W": 0, "R": 1, "B": 2, "G": 3, "Y": 4}
INT_TO_QUAL = [0, 7, 5, 3, 2]
W_INT = 0


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate_cw(board: Int2d) -> Int2d:
    return [list(row) for row in zip(*board[::-1])]


def paste(curr_eff: Int2d, curr_elm: Int2d, eff: Int2d, elm: Int2d,
          start: tuple[int, int]) -> tuple[Int2d, Int2d]:
    next_eff, next_elm = [row[::] for row in curr_eff], [row[::] for row in curr_elm]
    sx, sy = start
    for x in range(4):
        for y in range(4):
            new_val = next_eff[sx + x][sy + y] + eff[x][y]
            if new_val < 0:
                new_val = 0
            elif new_val > 9:
                new_val = 9
            next_eff[sx + x][sy + y] = new_val
            if elm[x][y] != W_INT:
                next_elm[sx + x][sy + y] = elm[x][y]

    return next_eff, next_elm


def solve(n: int, efficacy: list[Int2d], elements: list[Int2d]) -> int:
    max_qual = 0
    is_used = [False] * n

    def backtrack(depth: int, curr_eff: Int2d, curr_elm: Int2d) -> None:
        nonlocal max_qual

        if depth == 3:
            qual = sum(curr_eff[x][y] * INT_TO_QUAL[curr_elm[x][y]]
                       for x in range(5) for y in range(5))
            max_qual = max(max_qual, qual)
            return

        positions = [(0, 0)] if depth == 0 else [(0, 0), (0, 1), (1, 0), (1, 1)]

        for i in range(n):
            if is_used[i]:
                continue
            is_used[i] = True
            eff, elm = efficacy[i], elements[i]
            for _ in range(4):
                eff, elm = rotate_cw(eff), rotate_cw(elm)
                for sx, sy in positions:
                    next_eff, next_elm = paste(curr_eff, curr_elm, eff, elm, (sx, sy))
                    backtrack(depth + 1, next_eff, next_elm)
            is_used[i] = False

    backtrack(0, [[0] * 5 for _ in range(5)], [[W_INT] * 5 for _ in range(5)])
    return max_qual


def main() -> None:
    n = int(sys_input())
    efficacy, elements = [], []
    for _ in range(n):
        efficacy.append([list(map(int, sys_input().split())) for _ in range(4)])
        elements.append([[CHAR_TO_INT[c] for c in sys_input().split()] for _ in range(4)])

    answer: int = solve(n, efficacy, elements)
    print(answer)


if __name__ == "__main__":
    main()
