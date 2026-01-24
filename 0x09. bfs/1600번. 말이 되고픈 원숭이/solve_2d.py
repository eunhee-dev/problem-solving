""" solve_2d.py for 1600번. 말이 되고픈 원숭이 """ 

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
HORSE_DIRECTIONS = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(h: int, w: int, k: int, board: list[str]) -> int:
    inf = k + 1  # 최대 k번 말처럼 이동할 수 있어서, inf를 k+1로 설정
    queue = deque([(0, 0)])
    visited = [[inf] * (w) for _ in range(h)]  # visited[x][y] = (x, y)까지 말처럼 이동한 최소 횟수
    visited[0][0] = 0
    distance = 0

    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if (x, y) == (h-1, w-1):
                return distance

            horse_move_cnt = visited[x][y]  # (방문이 순차적으로 이뤄지기 때문에, 큐에 안 넣고 visited에서 꺼내 써도 무방함)

            # 일반적인 방향으로 이동해보기 (상하좌우)
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == 1:
                    continue
                if visited[nx][ny] > horse_move_cnt:  # 더 적게 말처럼 이동할 수 있는 경우 갱신
                    visited[nx][ny] = horse_move_cnt
                    queue.append((nx, ny))

            # 말처럼 이동할 수 있는 최대 횟수를 넘었으면 아래 과정 skip
            if horse_move_cnt >= k:
                continue

            # 말처럼 이동해보기
            for dx, dy in HORSE_DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < h and 0 <= ny < w) or board[nx][ny] == 1:
                    continue
                if visited[nx][ny] > horse_move_cnt + 1:  # 더 적게 말처럼 이동할 수 있는 경우 갱신
                    visited[nx][ny] = horse_move_cnt + 1
                    queue.append((nx, ny))

        distance += 1

    return -1


def solve(h: int, w: int, k: int, board: list[str]) -> int:
    return bfs(h, w, k, board)


def main() -> None:
    k = int(sys_input())
    w, h = map(int, sys_input().split())  # (x, y) = (h, w) 임에 유의
    board = [[*map(int, sys_input().split())] for _ in range(h)]

    answer: int = solve(h, w, k, board)
    print(answer)


if __name__ == "__main__":
    main()
