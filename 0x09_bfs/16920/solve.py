""" solve.py for 16920번. 확장 게임 """

import sys
from collections import deque


DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def expand(n: int, m: int, board: list[list[str]], i: str, queue: deque[tuple[int, int]]) -> int:
    count = 0

    for _ in range(len(queue)):
        x, y  = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m):
                continue
            if board[nx][ny] == ".":
                board[nx][ny] = i
                queue.append((nx, ny))
                count += 1
    return count


def solve(n: int, m: int, p: int, s: dict[str, int], board: list[list[str]]) -> str:
    players_queue = {str(i): deque() for i in range(1, p + 1)}
    players_count = {str(i): 0 for i in range(1, p + 1)}

    for x in range(n):
        for y in range(m):
            if board[x][y] not in [".", "#"]:
                players_queue[board[x][y]].append((x, y))
                players_count[board[x][y]] += 1

    is_expanded = True

    while is_expanded:
        is_expanded = False
        for i in range(1, p + 1):
            i = str(i)
            for _ in range(s.get(i)):  # s_i번 반복
                queue = players_queue.get(i)
                if not queue:
                    break
                count = expand(n, m, board, i, queue)
                if count:
                    is_expanded = True
                    players_count[i] += count

    return " ".join(map(str, players_count.values()))


def main() -> None:
    n, m, p = map(int, sys_input().split())
    s = {str(i+1): s_i for i, s_i in enumerate(map(int, sys_input().split()))}
    board = [list(sys_input()) for _ in range(n)]

    answer: str = solve(n, m, p, s, board)
    print(answer)


if __name__ == "__main__":
    main()
