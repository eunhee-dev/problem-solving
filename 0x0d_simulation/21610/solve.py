""" solve.py for 21610번. 마법사 상어와 비바라기 """

import sys


DIRECTIONS = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: list[list[int]], moves: list[tuple[int, int]]) -> int:
    n = len(a)
    clouds = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]

    for d, s in moves:
        for i, (x, y) in enumerate(clouds):
            dx, dy = DIRECTIONS[d]
            nx, ny = (x + dx * s) % n , (y + dy * s) % n
            clouds[i] = (nx, ny)

        for x, y in clouds:
            a[x][y] += 1

        for x, y in clouds:
            for dx, dy in DIRECTIONS[2::2]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and a[nx][ny] > 0:
                    a[x][y] += 1

        prev_clouds = set(clouds)
        clouds = []
        for x in range(n):
            for y in range(n):
                if a[x][y] >= 2 and (x, y) not in prev_clouds:
                    clouds.append((x, y))
                    a[x][y] -= 2

    return sum(sum(row) for row in a)


def main() -> None:
    n, m = map(int, sys_input().split())
    a = [list(map(int, sys_input().split())) for _ in range(n)]
    moves = list((d, s) for d, s in (map(int, sys_input().split()) for _ in range(m)))

    answer: int = solve(a, moves)
    print(answer)


if __name__ == "__main__":
    main()
