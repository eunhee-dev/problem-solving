""" solve.py for 16637번. 괄호 추가하기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def calc(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    raise ValueError(f"[-] Not supported operation: {op}")


def solve(n: int, expression: str) -> int:
    max_val = float("-inf")
    nums = list(map(int, expression[::2]))
    ops = expression[1::2]

    def backtrack(depth: int, curr_val: int) -> None:
        nonlocal max_val

        if depth == n // 2:
            max_val = max(max_val, curr_val)
            return

        next_val = calc(curr_val, nums[depth + 1], ops[depth])
        backtrack(depth + 1, next_val)

        if depth + 1 < n // 2:
            bracket_val = calc(nums[depth + 1], nums[depth + 2], ops[depth + 1])
            next_val = calc(curr_val, bracket_val, ops[depth])
            backtrack(depth + 2, next_val)

    backtrack(0, nums[0])
    return max_val



def main() -> None:
    n = int(sys_input())
    expression = sys_input()

    answer: int = solve(n, expression)
    print(answer)


if __name__ == "__main__":
    main()
