""" solve.py for 19237번. 어른 상어 """

import sys

Int1d = list[int]
Int2d = list[list[int]]
Int3d = list[list[list[int]]]
Sharks = dict[int, tuple[tuple[int, int], int]]


DIRECTIONS = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def get_next_sharks(sharks: Sharks, board: Int3d, priorities: Int3d) -> Sharks:
    n = len(board)
    next_sharks = {}
    for num, ((x, y), shark_d) in sharks.items():
        next_d = -1
        for d in priorities[num - 1][shark_d - 1]:
            dx, dy = DIRECTIONS[d]
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if board[nx][ny][0] == 0:
                next_d = d
                break
            if next_d == -1 and board[nx][ny][0] == num:
                next_d = d
        dx, dy = DIRECTIONS[next_d]
        next_sharks[num] = ((x + dx, y + dy), next_d)
    return next_sharks


def solve(k: int, grid: Int2d, directions: Int1d, priorities: Int3d) -> int:
    n = len(grid)
    elapsed_time = 0
    sharks = {num: ((x, y), directions[grid[x][y] - 1])
              for x in range(n) for y in range(n) if (num := grid[x][y]) != 0}
    sharks = dict(sorted(sharks.items()))  # 오름차순 정렬

    board = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for num, ((x, y), _) in sharks.items():
        board[x][y] = [num, k]

    while len(sharks) > 1 and elapsed_time <= 1000:
        # 다음 상어 좌표/방향 계산
        sharks = get_next_sharks(sharks, board, priorities)

        # 냄새 감소
        for x in range(n):
            for y in range(n):
                if board[x][y][1] != 0:
                    board[x][y][1] -= 1
                    if board[x][y][1] == 0:
                        board[x][y][0] = 0

        # 상어 이동 및 충돌 반영
        removed = []
        for num, ((x, y), _) in sharks.items():
            # board[x][y][1] == k면 지금 추가된 냄새인데, sharks가 오름차순이므로 제거
            if board[x][y][1] == k:
                removed.append(num)
            else:
                board[x][y] = [num, k]
        for num in removed:
            del sharks[num]

        elapsed_time += 1

    return elapsed_time if elapsed_time <= 1000 else -1


def main() -> None:
    n, m, k = map(int, sys_input().split())
    grid = [list(map(int, sys_input().split())) for _ in range(n)]
    directions = list(map(int, sys_input().split()))
    priorities = [[list(map(int, sys_input().split())) for _ in range(4)] for _ in range(m)]

    answer: int = solve(k, grid, directions, priorities)
    print(answer)


if __name__ == "__main__":
    main()
