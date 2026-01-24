""" solve.py for 3986번. 좋은 단어 """ 

import sys


def solve(target_str: str) -> bool:
    if len(target_str) % 2:
        return False

    stack = []

    for ch in target_str:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    sys_input = sys.stdin.readline

    input_n = int(input())
    input_strs = (sys_input().rstrip() for _ in range(input_n))

    answer: int = sum(1 for input_str in input_strs if solve(input_str))
    print(answer)
