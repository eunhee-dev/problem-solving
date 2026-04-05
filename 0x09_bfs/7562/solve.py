""" solve.py for 7562번. 나이트의 이동 """

import sys
from collections import deque


DIRECTIONS = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1), (-1, 2), (-2, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(l: int, start: tuple[int, int], dest: tuple[int, int]) -> int:
    queue = deque([start])
    dist = [[-1] * l for _ in range(l)]
    dist[start[0]][start[1]] = 0

    while queue:
        x, y = queue.popleft()
        if (x, y) == dest:
            return dist[x][y]
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < l and 0 <= ny < l and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    raise RuntimeError("[-] Cannot reach here.")


def solve(l: int, start: tuple[int, int], dest: tuple[int, int]) -> int:
    return bfs(l, start, dest)


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        l = int(sys_input())
        start = tuple(map(int, sys_input().split()))
        dest = tuple(map(int, sys_input().split()))

        answer: int = solve(l, start, dest)
        print(answer)


if __name__ == "__main__":
    main()
