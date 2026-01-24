""" solve.py for 1600번. 말이 되고픈 원숭이 """ 

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
HORSE_DIRECTIONS = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(h: int, w: int, k: int, board: list[str]) -> int:
    queue = deque([(0, 0, 0)])
    dist = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
    dist[0][0][0] = 0

    while queue:
        x, y, horse_move_cnt = queue.popleft()

        if (x, y) == (h-1, w-1):
            return dist[x][y][horse_move_cnt]

        nd = dist[x][y][horse_move_cnt] + 1

        # 일반적인 방향으로 이동해보기 (상하좌우)
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == 1:
                continue
            if dist[nx][ny][horse_move_cnt] != -1:
                continue
            dist[nx][ny][horse_move_cnt] = nd
            queue.append((nx, ny, horse_move_cnt))

        # 말처럼 이동할 수 있는 횟수를 초과했으면 아래 과정 skip
        if horse_move_cnt >= k:
            continue

        # 말처럼 이동해보기
        for dx, dy in HORSE_DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == 1:
                continue
            if dist[nx][ny][horse_move_cnt + 1] != -1:
                continue
            dist[nx][ny][horse_move_cnt + 1] = nd
            queue.append((nx, ny, horse_move_cnt + 1))

    return -1


def solve(h: int, w: int, k: int, board: list[str]) -> int:
    return bfs(h, w, k, board)


def main() -> None:
    k = int(sys_input())
    w, h = map(int, sys_input().split())
    board = [[*map(int, sys_input().split())] for _ in range(h)]

    answer: int = solve(h, w, k, board)
    print(answer)


if __name__ == "__main__":
    main()
