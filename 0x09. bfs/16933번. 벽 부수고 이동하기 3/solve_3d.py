""" solve_3d.py for 16933번. 벽 부수고 이동하기 3 """ 
# Python3: 시간 초과, PyPy3: 통과

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, k: int, board: list[str]) -> int:
    queue = deque([(0, 0, 0)])
    visited = [[[False] * (k + 1) for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True
    distance = 1

    while queue:
        len_queue = len(queue)  # 이거 해주거나, board를 list[list[int]]로 변환하면 통과
        for _ in range(len_queue):
            x, y, broken_cnt = queue.popleft()
            if (x, y) == (n-1, m-1):
                return distance
            is_day = distance % 2  # 낮/밤 확인
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if board[nx][ny] == "0" and not visited[nx][ny][broken_cnt]:
                    visited[nx][ny][broken_cnt] = True
                    queue.append((nx, ny, broken_cnt))
                elif board[nx][ny] == "1" and broken_cnt < k and not visited[nx][ny][broken_cnt + 1]:
                    if is_day == 1:
                        visited[nx][ny][broken_cnt + 1] = True
                        queue.append((nx, ny, broken_cnt + 1))
                    else:
                        # 거리만 늘려주는 효과, visited 배열에는 영향을 주지 않음
                        queue.append((x, y, broken_cnt))
        distance += 1

    return -1


def solve(n: int, m: int, k: int, board: list[str]) -> int:
    return bfs(n, m, k, board)


def main() -> None:
    n, m, k = map(int, sys_input().split())
    board = [sys_input() for _ in range(n)]

    answer: int = solve(n, m, k, board)
    print(answer)


if __name__ == "__main__":
    main()
