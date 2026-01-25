""" solve.py for 17136번. 색종이 붙이기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def check(board: list[list[int]], x: int, y: int, size: int) -> bool:
    if x + size > 10 or y + size > 10:
        return False
    for dx in range(size):
        for dy in range(size):
            if board[x + dx][y + dy] != 1:
                return False
    return True


def paste(board: list[list[int]], x: int, y: int, size: int, val: int) -> None:
    for dx in range(size):
        for dy in range(size):
            board[x + dx][y + dy] = val


def solve(board: list[list[int]]) -> int:
    min_cnt = float("inf")
    coords = [(x, y) for x in range(10) for y in range(10) if board[x][y] == 1]
    remain = {size: 5 for size in range(1, 6)}

    def get_next_idx(curr_idx: int) -> int:
        for next_idx in range(curr_idx + 1, len(coords)):
            x, y = coords[next_idx]
            if board[x][y] == 1:
                return next_idx
        return len(coords)

    def backtrack(idx: int, cnt: int) -> None:
        nonlocal min_cnt

        if idx == len(coords):
            min_cnt = min(min_cnt, cnt)
            return

        if cnt >= min_cnt:
            return

        x, y = coords[idx]
        for size in range(1, 6):
            if remain[size] == 0:
                continue
            if not check(board, x, y, size):
                break
            paste(board, x, y, size, 2)
            remain[size] -= 1
            backtrack(get_next_idx(idx), cnt + 1)
            remain[size] += 1
            paste(board, x, y, size, 1)

    backtrack(0, 0)

    return min_cnt if min_cnt != float("inf") else -1


def main() -> None:
    board = [list(map(int, sys_input().split())) for _ in range(10)]

    answer: int = solve(board)
    print(answer)


if __name__ == "__main__":
    main()
