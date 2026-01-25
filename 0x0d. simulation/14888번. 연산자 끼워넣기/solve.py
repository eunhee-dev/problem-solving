""" solve.py for 14888번. 연산자 끼워넣기 """

import sys
from itertools import permutations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def cpp14_division(a: int, b: int) -> int:
    return -(-a // b) if a < 0 else a // b


def solve(sequence: list[int], ops: tuple[int, int, int, int]) -> tuple[int, int]:
    max_val = float("-inf")
    min_val = float("inf")

    op_list = ["+"] * ops[0] + ["-"] * ops[1] + ["*"] * ops[2] + ["/"] * ops[3]

    for op_combs in set(permutations(op_list)):
        curr_val = sequence[0]
        for i, op in enumerate(op_combs):
            if op == "+":
                curr_val += sequence[i+1]
            elif op == "-":
                curr_val -= sequence[i+1]
            elif op == "*":
                curr_val *= sequence[i+1]
            else:
                curr_val = cpp14_division(curr_val, sequence[i+1])

        max_val = max(max_val, curr_val)
        min_val = min(min_val, curr_val)

    return max_val, min_val


def main() -> None:
    _ = int(sys_input())
    sequence = list(map(int, sys_input().split()))
    ops = tuple(map(int, sys_input().split()))

    answer: tuple[int, int] = solve(sequence, ops)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
