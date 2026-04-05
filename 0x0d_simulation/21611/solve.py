""" solve.py for 21611번. 마법사 상어와 블리자드 """

import sys


SPIRAL_DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
BLIZARD_DIRS = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def convert_2d_to_1d(board_2d: list[list[int]]) -> tuple[list[int], list[list[int]]]:
    n = len(board_2d[0])
    pow_n = n ** 2

    x, y =  n // 2, n // 2
    board_2d_to_1d = [[-1] * n for _ in range(n)]
    board_2d_to_1d[x][y] = 0

    board_1d = [0] * pow_n

    d, r = 0, 1
    move_cnt = 0
    turn_cnt = 0

    for i in range(1, pow_n):
        dx, dy = SPIRAL_DIRS[d]
        x, y = x + dx, y + dy
        board_1d[i] = board_2d[x][y]
        board_2d_to_1d[x][y] = i
        move_cnt += 1

        if move_cnt == r:
            move_cnt = 0
            d = (d + 1) % 4
            turn_cnt += 1
            if turn_cnt == 2:
                turn_cnt = 0
                r += 1

    return board_1d, board_2d_to_1d


def grouping(board_1d: list[int]) -> list[tuple[int, int]]:
    pow_n = len(board_1d)

    if board_1d[1] == 0:
        return []

    groups = []
    cnt = 1

    for i in range(2, pow_n):
        if board_1d[i] == 0:
            groups.append((cnt, board_1d[i - 1]))
            break

        if board_1d[i] == board_1d[i - 1]:
            cnt += 1
        else:
            groups.append((cnt, board_1d[i - 1]))
            cnt = 1
    else:
        groups.append((cnt, board_1d[pow_n - 1]))

    return groups


def solve(board_2d: list[list[int]], blizards: list[tuple[int, int]]) -> int:
    score = 0
    n = len(board_2d)
    pow_n = n ** 2

    board_1d, board_2d_to_1d = convert_2d_to_1d(board_2d)

    for d, s in blizards:
        # 블리자드 마법 시전
        x, y =  n // 2, n // 2
        dx, dy = BLIZARD_DIRS[d]
        removed_idxs = {board_2d_to_1d[x + i * dx][y + i * dy] for i in range(1, s + 1)}
        board_1d = [board_1d[i] for i in range(pow_n) if i not in removed_idxs]
        board_1d.extend([0] * (pow_n - len(board_1d)))

        # 폭발
        while True:
            groups = grouping(board_1d)

            is_exploded = False
            board_1d = [0]

            for cnt, num in groups:
                if cnt >= 4:
                    score += num * cnt
                    is_exploded = True
                else:
                    board_1d.extend([num] * cnt)

            board_1d.extend([0] * (pow_n - len(board_1d)))

            if not is_exploded:
                break

        # 변화
        groups = grouping(board_1d)
        board_1d = [0]

        for cnt, num in groups:
            if len(board_1d) >= pow_n - 1:
                break
            board_1d.append(cnt)
            board_1d.append(num)

        board_1d.extend([0] * (pow_n - len(board_1d)))

    return score


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]
    blizards = list((d, s) for d, s in (map(int, sys_input().split()) for _ in range(m)))

    answer: int = solve(board, blizards)
    print(answer)


if __name__ == "__main__":
    main()
