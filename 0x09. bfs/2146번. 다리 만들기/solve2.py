""" solve2.py for 2146번. 다리 만들기 """

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


def bfs_min_distance(n: int, island_map: list[list[int]], starts: list[tuple[int, int]]) -> int:
    queue = deque(starts)
    dist = [[-1] * n for _ in range(n)]
    for start in starts:
        dist[start[0]][start[1]] = 0

    min_bridge_len = inf

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # 인접 좌표가 OOB 이거나 같은 섬이면 스킵
            if not (0 <= nx < n and 0 <= ny < n) or island_map[nx][ny] == island_map[x][y]:
                continue
            # 인접 좌표가 바다면, 해당 지역을 현재 섬으로 표시 (땅 따먹기/섬 영역 확장 느낌)
            if island_map[nx][ny] == 0:
                island_map[nx][ny] = island_map[x][y]
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
            # 인접 좌표가 섬이면, 현재까지 거리와 인접 지역에 적혀있는 거리를 더하면 다리 길이
            else:
                bridge_len = dist[x][y] + dist[nx][ny]
                # 최소 다리 길이 선정
                min_bridge_len = min(min_bridge_len, bridge_len)

    return min_bridge_len


def solve(n: int, board: list[list[int]]) -> int:
    island_map = [[0] * n for _ in range(n)]

    # 1. 섬 라벨링
    island_id = 0
    for x in range(n):
        for y in range(n):
            if not island_map[x][y] and board[x][y] == 1:
                island_id += 1
                bfs_labeling(n, board, island_map, (x, y), island_id)

    # 2. 섬의 테두리 좌표 위치 구하기
    starts = []
    for x in range(n):
        for y in range(n):
            if island_map[x][y] == 0:
                continue
            island_id = island_map[x][y]
            if all(island_map[x + dx][y + dy] == island_id
                   for dx, dy in DIRECTIONS
                   if 0 <= x + dx < n and 0 <= y + dy < n):
                continue
            starts.append((x, y))

    # 3. 테두리 위치에 있는 좌표들을 전부 큐에 넣고 bfs 돌림
    return bfs_min_distance(n, island_map, starts)


def main() -> None:
    n = int(sys_input())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, board)
    print(answer)


if __name__ == "__main__":
    main()
