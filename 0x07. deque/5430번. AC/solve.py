""" solve.py for 5430번. AC """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(funcs: str, list_str: str) -> str:
    deq = deque(list_str.split(",")) if list_str else deque()

    reversed_flag = False

    for func in funcs:
        if func == "R":
            reversed_flag = not reversed_flag
        elif func == "D":
            if not deq:
                return "error"
            if reversed_flag:
                deq.pop()
            else:
                deq.popleft()

    if reversed_flag:
        deq.reverse()

    return "[" + ",".join(deq) + "]"


def main() -> None:
    t = int(sys_input())

    for _ in range(t):
        funcs = sys_input()
        _ = sys_input()
        list_str = sys_input()[1:-1]

        result: str = solve(funcs, list_str)
        print(result)


if __name__ == "__main__":
    main()
