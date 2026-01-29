""" solve.py for 10866번. 덱 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    my_deque = deque()
    output = []

    for _ in range(n):
        cmd = sys_input().split()
        op = cmd[0]

        if op == "push_front":
            my_deque.appendleft(cmd[1])

        elif op == "push_back":
            my_deque.append(cmd[1])

        elif op == "pop_front":
            output.append(my_deque.popleft() if my_deque else "-1")

        elif op == "pop_back":
            output.append(my_deque.pop() if my_deque else "-1")

        elif op == "size":
            output.append(str(len(my_deque)))

        elif op == "empty":
            output.append("0" if my_deque else "1")

        elif op == "front":
            output.append(my_deque[0] if my_deque else "-1")

        elif op == "back":
            output.append(my_deque[-1] if my_deque else "-1")

        else:
            raise ValueError()

    return output


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
