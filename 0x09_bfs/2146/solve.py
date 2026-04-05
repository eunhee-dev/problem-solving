""" solve.py for 2146번. 다리 만들기 """

import sys
from collections import deque
from math import inf


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs_labeling(n: int, board: list[list[int]], island_map: list[list[int]],
                 start: tuple[int, int], island_id: int) -> None:
    queue = deque([start])
    island_map[start[0]][start[1]] = island_id

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not island_map[nx][ny] and board[nx][ny] == 1:
                island_map[nx][ny] = island_id
                queue.append((nx, ny))


def bfs(n: int, island_map: list[list[int]], start: tuple[int, int], island_id: int) -> int:
    queue = deque([start])
    dist = [[-1] * n for _ in range(n)]
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        if island_map[x][y] != 0 and island_map[x][y] != island_id:
            return dist[x][y]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    raise ValueError("[-] Invalid input. 2 islands should be exist.")


def solve(n: int, board: list[list[int]]) -> int:
    island_map = [[0] * n for _ in range(n)]

    # 1. 섬 라벨링
    island_id = 0
    for x in range(n):
        for y in range(n):
            if not island_map[x][y] and board[x][y] == 1:
                island_id += 1
                bfs_labeling(n, board, island_map, (x, y), island_id)

    # 2. 섬의 테두리에 위치하는 각각의 좌표에 대해 bfs 수행
    min_bridge_len = inf
    for x in range(n):
        for y in range(n):
            # 바다인 경우 스킵
            if island_map[x][y] == 0:
                continue
            island_id = island_map[x][y]
            # 테두리가 아닌 경우 스킵
            if all(island_map[x + dx][y + dy] != 0
                   for dx, dy in DIRECTIONS
                   if 0 <= x + dx < n and 0 <= y + dy < n):
                continue
            # 섬의 테두리에 위치하는 각각의 좌표에 대해 bfs를 통해 다른 섬까지의 최소 거리 측정
            bridge_len = bfs(n, island_map, (x, y), island_id) - 1  # 다리 길이 = 최소 거리 - 1
            # 최소 다리 길이 선정
            min_bridge_len = min(min_bridge_len, bridge_len)

    return min_bridge_len


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
