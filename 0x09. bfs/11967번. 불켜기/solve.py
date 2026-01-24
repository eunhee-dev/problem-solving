""" solve.py for 11967번. 불켜기 """

import sys
from collections import deque, defaultdict


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input():
    return sys.stdin.readline().rstrip()


def solve(n: int, switch: dict[tuple[int, int], list[tuple[int, int]]]) -> int:
    board = [[0] * n for _ in range(n)]  # on: 1 / off: 0
    board[0][0] = 1
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in switch:
            for cx, cy in switch[(x, y)]:
                if board[cx][cy] == 1:
                    continue
                board[cx][cy] = 1
                # 불을 켠 좌표 상하좌우에 이미 방문한 기록이 있으면 바로 방문
                for dx, dy in DIRECTIONS:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < n and 0 <= ny < n and visited[nx][ny]:
                        visited[cx][cy] = True
                        queue.append((cx, cy))
                        break

        # 현재 좌표에서 상하좌우로 불 켜진 방 중에 방문한 적이 없는 곳 체크하여 방문
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n  and 0 <= ny < n):
                continue
            if board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return sum(board[x][y] for x in range(n) for y in range(n))  # board에 1 개수 세기


def main() -> None:
    n, m = map(int, sys_input().split())
    switch = defaultdict(list)
    for _ in range(m):
        x, y, a, b = map(int, sys_input().split())
        switch[(x-1, y-1)].append((a-1, b-1))

    answer: int = solve(n, switch)
    print(answer)


if __name__ == "__main__":
    main()
