""" solve_efficient.py for 21608번. 상어 초등학교 """

import sys


DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
SCORE_TABLE = [0, 1, 10, 100, 1000]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, info: dict[int, set[int]]) -> int:
    board = [[0] * n for _ in range(n)]
    student_pos = {}

    for stu, like_set in info.items():
        cand_pos = set()
        for liked_stu in like_set:
            if liked_stu in student_pos:
                x, y = student_pos[liked_stu]
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                        cand_pos.add((nx, ny))

        if not cand_pos:
            for x in range(n):
                for y in range(n):
                    if board[x][y] == 0:
                        cand_pos.add((x, y))

        best_pos = (-1, -1)
        max_like, max_blank = -1, -1

        for x, y in sorted(list(cand_pos)):
            if board[x][y] != 0:
                continue
            curr_like, curr_blank = 0, 0
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < n):
                    continue
                if board[nx][ny] == 0:
                    curr_blank += 1
                elif board[nx][ny] in like_set:
                    curr_like += 1

            if curr_like > max_like:
                max_like = curr_like
                max_blank = curr_blank
                best_pos = (x, y)

            elif curr_like == max_like:
                if curr_blank > max_blank:
                    max_blank = curr_blank
                    best_pos = (x, y)

        board[best_pos[0]][best_pos[1]] = stu
        student_pos[stu] = best_pos

    score = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            like_set = info[board[x][y]]
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in like_set:
                    cnt += 1
            score += SCORE_TABLE[cnt]

    return score


def main() -> None:
    n = int(sys_input())
    info = {x[0]: set(x[1:]) for x in (list(map(int, sys_input().split())) for _ in range(n ** 2))}

    answer: int = solve(n, info)
    print(answer)


if __name__ == "__main__":
    main()
