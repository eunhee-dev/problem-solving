""" solve.py for 9012번. 괄호 """ 

import sys


def solve(paren_str: str) -> bool:
    if len(paren_str) % 2:
        return False

    paren_cnt = 0

    for ch in paren_str:
        if ch == "(":
            paren_cnt += 1
        elif ch == ")":
            paren_cnt -= 1

        if paren_cnt < 0:
            return False

    return paren_cnt == 0


if __name__ == "__main__":
    sys_input = sys.stdin.readline

    input_n = int(input())

    for _ in range(input_n):
        input_paren_str = sys_input().rstrip()

        answer: bool = solve(input_paren_str)
        print("YES" if answer else "NO")
