""" solve.py for 10828번. 스택 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> list[int | str]:
    output = []
    stack = []

    for _ in range(n):
        cmd = sys_input().split()
        op = cmd[0]

        if op == "push":
            stack.append(cmd[1])

        elif op == "pop":
            output.append(stack.pop() if stack else -1)

        elif op == "size":
            output.append(len(stack))

        elif op == "empty":
            output.append(0 if stack else 1)

        elif op == "top":
            output.append(stack[-1] if stack else -1)

        else:
            raise ValueError()

    return output


def main() -> None:
    n = int(sys_input())

    answer: list[int | str] = solve(n)
    print(*answer, sep="\n")


if __name__ == "__main__":
    main()
