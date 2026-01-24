""" solve.py for 5430번. AC """ 

import sys
from collections import deque


def solve(t: int) -> None:
    sys_input = sys.stdin.readline

    for _ in range(t):
        funcs = sys_input().rstrip()
        _ = sys_input()
        list_str = sys_input().rstrip()[1:-1]
        deq = deque(list_str.split(",")) if list_str else deque()

        reversed_flag = False
        error_flag = False

        for func in funcs:
            if func == "R":
                reversed_flag = not reversed_flag
            elif func == "D":
                if not deq:
                    error_flag = True
                    break
                if reversed_flag:
                    deq.pop()
                else:
                    deq.popleft()

        if error_flag:
            print("error")
            continue

        if reversed_flag:
            deq.reverse()

        output_str = "[" + ",".join(str(ch) for ch in deq) + "]"
        print(output_str)


if __name__ == "__main__":
    input_t = int(input())
    solve(input_t)
