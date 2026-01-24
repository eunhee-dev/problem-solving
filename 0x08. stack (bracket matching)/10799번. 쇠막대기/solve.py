""" solve.py for 10799번. 쇠막대기 """ 

import sys


def solve(target_str: str) -> int:
    count = 0
    open_brackets = 0
    prev = ""

    for ch in target_str:
        if ch == "(":
            open_brackets += 1
        elif ch == ")":
            open_brackets -= 1
            if prev == "(":
                count += open_brackets
            else:
                count += 1
        prev = ch

    return count


if __name__ == '__main__':
    sys_input = sys.stdin.readline
    input_target_str = sys_input().rstrip()

    answer: int = solve(input_target_str)
    print(answer)
