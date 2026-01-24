""" solve_naive.py for 9328번. 열쇠 """

import sys
from collections import deque, defaultdict


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check_coord(x: int, y: int, cell: str, keys: set[str],
                locked_doors: dict[list[tuple[int, int]]]) -> bool:
    if cell == "*":
        return False
    if "A" <= cell <= "Z" and cell not in keys:
        locked_doors[cell].append((x, y))
        return False
    return True


def bfs(h: int, w: int, board: list[str], keys: set[str], visited: list[list[bool]],
        start: tuple[int, int], locked_doors: dict[str, list[tuple[int, int]]]) -> int:
    docs_cnt = 0
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        if board[x][y] == "$":
            docs_cnt += 1
        elif "a" <= board[x][y] <= "z":
            new_key = board[x][y].upper()
            keys.add(new_key)
            if new_key in locked_doors:
                queue.extend(locked_doors.pop(new_key))

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if not visited[nx][ny]:
                if check_coord(nx, ny, board[nx][ny], keys, locked_doors):
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    return docs_cnt


def solve(h: int, w: int, board: list[str], keys: set[str]) -> int:
    total_docs = 0
    locked_doors = defaultdict(list)
    visited = [[False] * w for _ in range(h)]

    border_coords = [(x, y) for x in range(h) for y in range(w)
                     if x == 0 or x == h - 1 or y == 0 or y == w - 1]
    starts = []
    for x, y in border_coords:
        if check_coord(x, y, board[x][y], keys, locked_doors):
            starts.append((x, y))

    for start in starts:
        if not visited[start[0]][start[1]]:
            total_docs += bfs(h, w, board, keys, visited, start, locked_doors)

    return total_docs


def main():
    t = int(sys_input())
    for _ in range(t):
        h, w = map(int, sys_input().split())
        board = [sys_input() for _ in range(h)]
        keys = set(sys_input().upper())

        answer: int = solve(h, w, board, keys)
        print(answer)


if __name__ == "__main__":
    main()
