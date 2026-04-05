""" solve_itertools.py for 1941번. 소문난 칠공주 """

import sys
from collections import deque
from itertools import combinations


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def is_connected_bfs(path: list[tuple[int, int]]) -> bool:
    start = path[0]
    queue = deque([start])
    visited = {start}
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if (nx, ny) in path and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))
    return len(visited) == 7


def solve(board: list[str]) -> int:
    cnt = 0
    coords = [(x, y) for x in range(5) for y in range(5)]

    for combs in combinations(coords, 7):
        s_count = sum(1 for x, y in combs if board[x][y] == "S")
        if s_count < 4:
            continue
        if is_connected_bfs(combs):
            cnt += 1
    return cnt


def main() -> None:
    board = [sys_input() for _ in range(5)]

    answer: int = solve(board)
    print(answer)


if __name__ == "__main__":
    main()
