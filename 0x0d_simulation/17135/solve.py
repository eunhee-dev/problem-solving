import sys
from itertools import combinations
from collections import deque


DIRECTIONS = [(0, -1), (-1, 0), (0, 1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_nearest_enemy(board: list[list[int]], archer: int, d: int) -> tuple[int, int]:
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    visited[n - 1][archer] = True
    queue = deque([(n - 1, archer)])

    while queue and d > 0:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if board[x][y] == 1:
                return x, y
            for dx, dy in DIRECTIONS:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
        d -= 1

    return -1, -1


def solve(d: int, board: list[list[int]]) -> int:
    m = len(board[0])
    max_removed = 0
    total_enemy = sum(sum(row) for row in board)

    for archer_comb in combinations(range(m), 3):
        tmp_board = [row[::] for row in board]
        curr_enemy = total_enemy
        removed = 0

        while curr_enemy > 0:
            removed_enemy = {pos for archer in archer_comb
                             if (pos := get_nearest_enemy(tmp_board, archer, d)) != (-1, -1)}

            for x, y in removed_enemy:
                tmp_board[x][y] = 0
                curr_enemy -= 1
                removed += 1

            curr_enemy -= sum(tmp_board.pop())

        max_removed = max(max_removed, removed)

    return max_removed


def main() -> None:
    n, _, d = map(int, sys_input().split())
    board = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(d, board)
    print(answer)


if __name__ == "__main__":
    main()
