""" solve.py for 14500번. 테트로미노 """

import sys


DIRECTIONS = [(-1, 0), (0, 1), (1, 0)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, m: int, board: list[list[int]]) -> int:
    max_sum = 0
    visited = [[False] * m for _ in range(n)]

    def backtrack(depth: int, x: int, y: int, curr_sum: int) -> None:
        nonlocal max_sum

        if depth == 4:
            max_sum = max(max_sum, curr_sum)
            return

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if visited[nx][ny]:
                continue
            visited[nx][ny] = True
            curr_sum += board[nx][ny]
            backtrack(depth + 1, nx, ny, curr_sum)
            if depth == 2:  # depth + 1 == 3
                backtrack(depth + 1, x, y, curr_sum)
            visited[nx][ny] = False
            curr_sum -= board[nx][ny]

    for x in range(n):
        for y in range(m):
            visited[x][y] = True
            backtrack(1, x, y, board[x][y])
            visited[x][y] = False

    return max_sum


def main() -> None:
    n, m = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, m, board)
    print(answer)


if __name__ == "__main__":
    main()
