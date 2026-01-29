""" solve.py for 10845번. 큐 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[str]:
    queue = deque()
    output = []

    for _ in range(n):
        cmd = sys_input().split()
        op = cmd[0]

        if op == "push":
            queue.append(cmd[1])

        elif op == "pop":
            output.append(queue.popleft() if queue else "-1")

        elif op == "size":
            output.append(str(len(queue)))

        elif op == "empty":
            output.append("0" if queue else "1")

        elif op == "front":
            output.append(queue[0] if queue else "-1")

        elif op == "back":
            output.append(queue[-1] if queue else "-1")

        else:
            raise ValueError()

    return output


def main() -> None:
    n = int(sys_input())

    answer: list[str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
