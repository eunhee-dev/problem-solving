""" solve_4d_fail.py for 16933번. 벽 부수고 이동하기 3 """
# Python3/PyPy3: 시간 초과

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, m: int, k: int, board: list[str]) -> int:
    queue = deque([(0, 0, 0, 1)])  # (x, y, broken_cnt, is_day)
    visited = [[[[False] * 2 for _ in range(k + 1)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0][1] = True   # is_day == 1 이면 낮, 0 이면 밤
    distance = 1

    while queue:
        for _ in range(len(queue)):
            x, y, broken_cnt, is_day = queue.popleft()
            if (x, y) == (n-1, m-1):
                return distance
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                next_is_day = is_day ^ 1  # xor 1 하여 day/night 계산
                if not (0 <= nx < n and 0 <= ny < m):
                    continue
                if board[nx][ny] == "0":  # 벽이 아니면 그냥 가기
                    if not visited[nx][ny][broken_cnt][next_is_day]:
                        visited[nx][ny][broken_cnt][next_is_day] = True
                        queue.append((nx, ny, broken_cnt, next_is_day))
                elif board[nx][ny] == "1" and broken_cnt < k:  # 벽이고 아직 부술 수 있으면
                    if is_day == 1:  # 낮이면 부수고 가기
                        if not visited[nx][ny][broken_cnt + 1][next_is_day]:  # 안 가본 경우에만 부수기
                            visited[nx][ny][broken_cnt + 1][next_is_day] = True
                            queue.append((nx, ny, broken_cnt + 1, next_is_day))
                    else:  # 밤인 경우 기다리기
                        # 안 가본 경우에만 큐에 넣기, 중복/무한루프 방지
                        if not visited[x][y][broken_cnt][next_is_day]:
                            visited[x][y][broken_cnt][next_is_day] = True
                            queue.append((x, y, broken_cnt, next_is_day))
                            # nx, ny가 아닌 현재 위치 x, y를 next_is_day로 상태로 변환하여 큐에 넣기
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
