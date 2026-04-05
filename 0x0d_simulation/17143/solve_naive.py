""" solve_naive.py for 17143번. 낚시왕 """

import sys


DIRECTIONS = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(r: int, c: int, sharks_info: list[tuple[int, int, int, int, int]]) -> int:
    total = 0
    board = [[-1] * c for _ in range(r)]
    sharks = {}

    for i, (x, y, s, d, z) in enumerate(sharks_info):
        board[x - 1][y - 1] = i
        d -= 1
        sharks[i] = (x - 1, y - 1, s, d, z)

    for y in range(c):
        for x in range(r):
            if board[x][y] != -1:
                i = board[x][y]
                total += sharks[i][4]
                del sharks[i]
                break

        board = [[-1] * c for _ in range(r)]
        removed_sharks = []

        for i, (x, y, s, d, z) in sharks.items():
            dx, dy = DIRECTIONS[d]
            nx, ny = x, y

            for _ in range(s):
                nx, ny = nx + dx, ny + dy
                if not (0 <= nx < r and 0 <= ny < c):
                    nx, ny = nx - dx, ny - dy

                    dx, dy = -dx, -dy
                    if d % 2 == 0:
                        d += 1
                    else:
                        d -= 1

                    nx, ny = nx + dx, ny + dy

            if board[nx][ny] != -1:
                j = board[nx][ny]
                if sharks[j][4] > sharks[i][4]:
                    removed_sharks.append(i)
                    continue
                removed_sharks.append(j)

            sharks[i] = (nx, ny, s, d, z)
            board[nx][ny] = i

        for i in removed_sharks:
            del sharks[i]

    return total


def main() -> None:
    r, c, m = map(int, sys_input().split())
    sharks = [tuple(map(int ,sys_input().split())) for _ in range(m)]

    answer: int = solve(r, c, sharks)
    print(answer)


if __name__ == "__main__":
    main()
