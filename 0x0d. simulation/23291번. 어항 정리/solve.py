""" solve.py for 23291번. 어항 정리 """

import sys
from collections import deque


DIRECTIONS = [(0, 1), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def adjust_and_flatten(fish_tanks: deque[deque[int]]) -> deque[deque[int]]:
    diff_tanks = []
    for col in list(fish_tanks):
        diff_tanks.append([0] * len(col))

    for x, col in enumerate(fish_tanks):
        for y, tank in enumerate(col):
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < len(fish_tanks) and 0 <= ny < len(col)) or ny >= len(fish_tanks[nx]):
                    continue

                d = abs(tank - fish_tanks[nx][ny]) // 5
                if tank > fish_tanks[nx][ny]:
                    diff_tanks[x][y] -= d
                    diff_tanks[nx][ny] += d
                else:
                    diff_tanks[x][y] += d
                    diff_tanks[nx][ny] -= d

    for x, col in enumerate(fish_tanks):
        for y, _ in enumerate(col):
            fish_tanks[x][y] += diff_tanks[x][y]

    # 평탄화
    new_fish_tanks = deque()
    for col in list(fish_tanks):
        while col:
            new_fish_tanks.append(deque([col.popleft()]))

    return new_fish_tanks


def solve(n: int, k: int, fish_tanks: deque[deque[int]]) -> int:
    turn = 1

    while True:
        # 물고기 채우기
        min_fish_cnt = min(col[0] for col in fish_tanks)
        for i, col in enumerate(fish_tanks):
            if col[0] == min_fish_cnt:
                fish_tanks[i][0] += 1

        # 제일 왼쪽 어항 옮기기
        left_tank = fish_tanks.popleft()[0]
        fish_tanks[0].append(left_tank)

        # 2개 이상 쌓여있는 어항 옮기기
        while True:
            left_cols = []
            for col in list(fish_tanks):
                if len(col) >= 2:
                    left_cols.append(fish_tanks.popleft())
                else:
                    break

            if len(left_cols[0]) > len(fish_tanks):
                fish_tanks.extendleft(reversed(left_cols))
                break

            while left_cols:
                col = left_cols.pop()
                for i, tank in enumerate(col):
                    fish_tanks[i].append(tank)

        # 어항 조정하고 평탄화하기
        fish_tanks = adjust_and_flatten(fish_tanks)

        # 공중 부양하기
        left_cols = [fish_tanks.popleft() for _ in range(n // 2)]
        for x, col in enumerate(reversed(left_cols)):
            fish_tanks[x].extend(reversed(col))

        left_cols = [fish_tanks.popleft() for _ in range(n // 4)]
        for x, col in enumerate(reversed(left_cols)):
            fish_tanks[x].extend(reversed(col))

        # 어항 조정하고 평탄화 하기
        fish_tanks = adjust_and_flatten(fish_tanks)

        # 종료 조건
        if max(col[0] for col in fish_tanks) - min(col[0] for col in fish_tanks) <= k:
            break

        turn += 1

    return turn


def main() -> None:
    n, k = map(int, sys_input().split())
    fish_tanks = deque(deque([x]) for x in (map(int, sys_input().split())))

    answer: int = solve(n, k, fish_tanks)
    print(answer)


if __name__ == "__main__":
    main()
