""" solve.py for 4949번. 균형잡힌 세상 """ 

import sys


def solve(target_str: str) -> bool:
    stack = []

    for ch in target_str:
        if ch in ["(", "["]:
            stack.append(ch)
        elif ch == ")":
            if not stack or stack[-1] != "(":
                return False
            stack.pop()
        elif ch == "]":
            if not stack or stack[-1] != "[":
                return False
            stack.pop()
    return not stack


if __name__ == "__main__":
    sys_input = sys.stdin.readline

    while True:
        input_str = sys_input().rstrip()
        if input_str == ".":
            break

        answer: bool = solve(input_str)
        print("yes" if answer else "no")
