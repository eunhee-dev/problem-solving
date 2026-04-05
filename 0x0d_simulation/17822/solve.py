""" solve.py for 17822번. 원판 돌리기 """

import sys
from collections import deque


DIRECTIONS = [(0, 1), (0, -1), (-1, 0), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(plates: list[deque[int]], visited: list[list[bool]], start: tuple[int, int]) -> bool:
    n, m = len(plates), len(plates[0])

    queue = deque([start])
    visited[start[0]][start[1]] = True
    path = [start]

    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, (y + dy) % m
            if not 0 <= nx < n:
                continue
            if visited[nx][ny]:
                continue
            if plates[nx][ny] == plates[x][y]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                path.append((nx, ny))

    if len(path) >= 2:
        for x, y in path:
            plates[x][y] = 0
        return True
    return False


def solve(n: int, m: int, plates: list[deque[int]], rotates: list[tuple[int, int, int]]) -> int:
    for x, d, k in rotates:
        # 원판 돌리기
        d = 1 if d == 0 else -1

        for i in range(x, n + 1, x):
            plates[i - 1].rotate(d * k)

        # 인접한 같은 수 지우기
        visited = [[False] * m for _ in range(n)]
        is_removed = False

        for x in range(n):
            for y in range(m):
                if plates[x][y] != 0 and not visited[x][y]:
                    if bfs(plates, visited, (x, y)):
                        is_removed = True

        # 평균 구하여 보정하기
        if not is_removed:
            nums = [num for plate in plates for num in plate if num != 0]
            if not nums:
                return 0
            avg = sum(nums) / len(nums)
            for x in range(n):
                for y in range(m):
                    if plates[x][y] != 0:
                        if plates[x][y] > avg:
                            plates[x][y] -= 1
                        elif plates[x][y] < avg:
                            plates[x][y] += 1

    return sum(num for plate in plates for num in plate)


def main() -> None:
    n, m, t = map(int, sys_input().split())
    plates = [deque(map(int, sys_input().split())) for _ in range(n)]
    rotates = [tuple(map(int, sys_input().split())) for _ in range(t)]

    answer: int = solve(n, m, plates, rotates)
    print(answer)


if __name__ == "__main__":
    main()
