""" solve.py for 1941번. 소문난 칠공주 """

import sys
from collections import deque


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
    path = []

    def backtrack(start: int, depth: int, s_count: int) -> None:
        nonlocal cnt
        if s_count + (7 - depth) < 4:  # pruning
            return

        if depth == 7:
            if s_count >= 4 and is_connected_bfs(path):
                cnt += 1
            return

        for i in range(start, 25):
            x, y = divmod(i, 5)
            path.append((x, y))
            backtrack(i + 1, depth + 1, s_count + (board[x][y] == "S"))
            path.pop()

    backtrack(0, 0, 0)
    return cnt


def main() -> None:
    board = [sys_input() for _ in range(5)]

    answer: int = solve(board)
    print(answer)


if __name__ == "__main__":
    main()
