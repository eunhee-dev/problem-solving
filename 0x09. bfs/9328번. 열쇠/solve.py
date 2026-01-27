""" solve.py for 9328번. 열쇠 """

import sys
from collections import deque, defaultdict


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(h: int, w: int, board: list[str], keys: set[str]) -> int:
    docs_cnt = 0
    queue = deque([(0, 0)])
    visited = [[False] * w for _ in range(h)]
    visited[0][0] = True
    locked_doors = defaultdict(list)

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < h and 0 <= ny < w):
                continue
            if not visited[nx][ny]:
                if board[nx][ny] == "*":
                    continue
                if "A" <= board[nx][ny] <= "Z" and board[nx][ny] not in keys:
                    locked_doors[board[nx][ny]].append((nx, ny))
                    continue

                if "a" <= board[nx][ny] <= "z":
                    new_key = board[nx][ny].upper()
                    keys.add(new_key)
                    if new_key in locked_doors:
                        queue.extend(locked_doors.pop(new_key))
                elif board[nx][ny] == "$":
                    docs_cnt += 1

                visited[nx][ny] = True
                queue.append((nx, ny))

    return docs_cnt


def solve(h: int, w: int, board: list[str], keys: set[str]) -> int:
    return bfs(h, w, board, keys)


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        h, w = map(int, sys_input().split())
        board = ["." + sys_input() + "." for _ in range(h)]
        board = ["." * (w+2)] + board + ["." * (w+2)]
        keys = set(sys_input().upper())

        answer: int = solve(h+2, w+2, board, keys)
        print(answer)


if __name__ == "__main__":
    main()
