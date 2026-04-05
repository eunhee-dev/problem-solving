""" solve.py for 21608번. 상어 초등학교 """

import sys


DIRECTIONS = [(-1, 0), (0, -1), (0, 1), (1, 0)]
SCORE_TABLE = [0, 1, 10, 100, 1000]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, info: dict[int, set[int]]) -> int:
    board = [[0] * n for _ in range(n)]

    for stu, like_set in info.items():
        counter = {}

        for x in range(n):
            for y in range(n):
                if board[x][y] != 0:
                    continue
                counter[(x, y)] = [0, 0]
                blank_cnt = 0
                for dx, dy in DIRECTIONS:
                    nx, ny = x + dx, y + dy
                    if not (0 <= nx < n and 0 <= ny < n):
                        continue
                    if board[nx][ny] == 0:
                        blank_cnt += 1
                    elif board[nx][ny] in like_set:
                        counter[(x, y)][0] += 1
                counter[(x, y)][1] = blank_cnt

        x, y = sorted(counter.items(), key=lambda x: (-x[1][0], -x[1][1], x[0]))[0][0]
        board[x][y] = stu

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
