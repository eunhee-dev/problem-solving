""" solve.py for 13460번. 구슬 탈출 2 """

import sys
from collections import deque


DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def find_pos(board: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    n = len(board)
    m = len(board[0])
    red, blue, goal = None, None, None
    for x in range(n):
        for y in range(m):
            if board[x][y] == "R":
                red = (x, y)
            elif board[x][y] == "B":
                blue = (x, y)
            elif board[x][y] == "O":
                goal = (x, y)
    return red, blue, goal


def solve(board: list[list[str]]) -> int:
    red, blue, goal = find_pos(board)

    queue = deque([(1, red, blue)])
    visited = set([(red, blue)])

    while queue:
        count, red, blue = queue.popleft()

        if count > 10:
            return -1

        for d_idx in range(4):
            dx, dy = DIRECTIONS[d_idx]
            r_move, b_move = 0, 0

            nrx, nry = red
            while board[nrx + dx][nry + dy] != "#" and board[nrx][nry] != "O":
                nrx, nry = nrx + dx, nry + dy
                r_move += 1

            nbx, nby = blue
            while board[nbx + dx][nby + dy] != "#" and board[nbx][nby] != "O":
                nbx, nby = nbx + dx, nby + dy
                b_move += 1

            # 파란 구슬이 들어간 경우 (해당 케이스는 더 안봐도 됨)
            if (nbx, nby) == goal:
                continue

            # 빨간 구슬이 들어간 경우 (최소 시행횟수)
            if (nrx, nry) == goal:
                return count

            # 구슬이 겹친 경우 보정
            if (nrx, nry) == (nbx, nby):
                if r_move > b_move:
                    nrx, nry = nrx - dx, nry - dy
                else:
                    nbx, nby = nbx - dx, nby - dy

            if ((nrx, nry), (nbx, nby)) not in visited:
                visited.add(((nrx, nry), (nbx, nby)))
                queue.append((count + 1, (nrx, nry), (nbx, nby)))

    return -1


def main() -> None:
    n, _ = map(int, sys_input().split())
    board = [list(sys_input()) for _ in range(n)]

    answer: int = solve(board)
    print(answer)


if __name__ == "__main__":
    main()
