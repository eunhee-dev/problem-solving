""" solve.py for 17472번. 다리 만들기 2 """

import sys
from collections import deque, defaultdict


Int2d = list[list[int]]
Coord = tuple[int, int]


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MIN_BRIDGE_LEN = 2


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs_labeling(board: Int2d, island_map: Int2d, start: Coord, island_id: int) -> set[Coord]:
    n, m = len(board), len(board[0])
    queue = deque([start])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    island_map[start[0]][start[1]] = island_id
    border_coords = set()

    while queue:
        x, y = queue.popleft()
        is_border = False
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if board[nx][ny] == 0:
                is_border = True

            if board[nx][ny] == 1 and not visited[nx][ny]:
                island_map[nx][ny] = island_id
                visited[nx][ny] = True
                queue.append((nx, ny))

        if is_border:
            border_coords.add((x, y))

    return border_coords


def kruscal(num_vertices: int, edges: list[tuple[int, int, int]]) -> int:
    parent = list(range(num_vertices + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> bool:
        root_a, root_b = find(a), find(b)

        if root_a == root_b:
            return False

        parent[root_b] = root_a
        return True

    total_cost = 0
    edge_cnt = 0

    for cost, u, v in edges:
        if union(u, v):
            total_cost += cost
            edge_cnt += 1

    if edge_cnt != num_vertices - 1:
        return -1
    return total_cost


def solve(n: int, m: int, board: Int2d) -> int:
    island_map = [[0] * m for _ in range(n)]
    island_id = 0
    island_border_coords = {}
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1 and not island_map[x][y]:
                island_id += 1
                border_coords = bfs_labeling(board, island_map, (x, y), island_id)
                island_border_coords[island_id] = border_coords

    island_len = island_id
    min_distance = defaultdict(lambda: sys.maxsize)

    for i in range(1, island_len + 1):
        for x, y in island_border_coords[i]:
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                bridge_len = 0

                while 0 <= nx < n and 0 <= ny < m:
                    if island_map[nx][ny] != 0:
                        j = island_map[nx][ny]
                        if j > i and bridge_len >= MIN_BRIDGE_LEN:
                            min_distance[(i, j)] = min(min_distance[(i, j)], bridge_len)
                        break

                    nx, ny = nx + dx, ny + dy
                    bridge_len += 1

    edges = sorted((cost, u, v) for (u, v), cost in min_distance.items())
    return kruscal(island_len, edges)


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
