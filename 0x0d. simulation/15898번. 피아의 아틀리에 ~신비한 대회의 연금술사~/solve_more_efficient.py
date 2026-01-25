""" solve_more_efficient.py for 15898번. 피아의 아틀리에 ~신비한 대회의 연금술사~ """
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
    pre_efficacy, pre_elements = [], []
    for i in range(n):
        eff, elm = efficacy[i], elements[i]
        rot_effs, rot_elms = [eff], [elm]
        for _ in range(3):
            eff, elm = rotate_cw(eff), rotate_cw(elm)
            rot_effs.append(eff)
            rot_elms.append(elm)
        pre_efficacy.append(rot_effs)
        pre_elements.append(rot_elms)

    max_qual = 0
    is_used = [False] * n

    def backtrack(depth: int, curr_qual: int, curr_eff: Int2d, curr_elm: Int2d) -> None:
        nonlocal max_qual

        if depth == 3:
            max_qual = max(max_qual, curr_qual)
            return

        positions = [(0, 0)] if depth == 0 else [(0, 0), (0, 1), (1, 0), (1, 1)]

        for i in range(n):
            if is_used[i]:
                continue
            is_used[i] = True
            for r in range(4):
                eff, elm = pre_efficacy[i][r], pre_elements[i][r]
                for sx, sy in positions:
                    qual_before = 0
                    for x in range(4):
                        for y in range(4):
                            qual_before += (curr_eff[sx + x][sy + y]
                                            * INT_TO_QUAL[curr_elm[sx + x][sy + y]])

                    next_eff, next_elm = paste(curr_eff, curr_elm, eff, elm, (sx, sy))

                    qual_after = 0
                    for x in range(4):
                        for y in range(4):
                            qual_after += (next_eff[sx + x][sy + y]
                                           * INT_TO_QUAL[next_elm[sx + x][sy + y]])

                    next_qual = curr_qual - qual_before + qual_after
                    backtrack(depth + 1, next_qual, next_eff, next_elm)
            is_used[i] = False

    backtrack(0, 0, [[0] * 5 for _ in range(5)], [[W_INT] * 5 for _ in range(5)])
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
