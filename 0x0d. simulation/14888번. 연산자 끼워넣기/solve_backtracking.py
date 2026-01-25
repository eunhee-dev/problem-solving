""" solve_backtracking.py for 14888번. 연산자 끼워넣기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(sequence: list[int], ops: tuple[int, int, int, int]) -> tuple[int, int]:
    max_val = float("-inf")
    min_val = float("inf")

    add, sub, mul, div = ops

    def backtrack(idx: int, curr_val: int, add: int, sub: int, mul: int, div: int) -> None:
        nonlocal max_val, min_val

        if idx == len(sequence):
            max_val = max(max_val, curr_val)
            min_val = min(min_val, curr_val)
            return

        if add > 0:
            backtrack(idx + 1, curr_val + sequence[idx], add - 1, sub, mul, div)
        if sub > 0:
            backtrack(idx + 1, curr_val - sequence[idx], add, sub - 1, mul, div)
        if mul > 0:
            backtrack(idx + 1, curr_val * sequence[idx], add, sub, mul - 1, div)
        if div > 0:
            backtrack(idx + 1, int(curr_val / sequence[idx]), add, sub, mul, div - 1)

    backtrack(1, sequence[0], add, sub, mul, div)
    return max_val, min_val


def main() -> None:
    _ = int(sys_input())
    sequence = list(map(int, sys_input().split()))
    ops = tuple(map(int, sys_input().split()))

    answer: tuple[int, int] = solve(sequence, ops)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
