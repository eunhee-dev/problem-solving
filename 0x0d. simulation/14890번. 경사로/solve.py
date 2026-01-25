""" solve.py for 14890번. 경사로 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check(n: int, l: int, line: list[int]) -> bool:
    visited = [False] * n
    for x in range(n - 1):
        if line[x] == line[x + 1]:
            continue

        if abs(line[x] - line[x + 1]) > 1:
            return False

        if line[x] < line[x + 1]:
            for bx in range(x, x - l, -1):
                if bx < 0 or line[bx] != line[x] or visited[bx]:
                    return False
                visited[bx] = True

        else:
            for nx in range(x + 1, x + 1 + l):
                if nx >= n or line[nx] != line[x + 1] or visited[nx]:
                    return False
                visited[nx] = True
    return True


def solve(n: int, l: int, board: list[list[int]]) -> int:
    count = 0

    for row in board:
        if check(n, l, row):
            count += 1

    for col in map(list, zip(*board)):
        if check(n, l, col):
            count += 1

    return count


def main() -> None:
    n, l = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, l, board)
    print(answer)


if __name__ == "__main__":
    main()
