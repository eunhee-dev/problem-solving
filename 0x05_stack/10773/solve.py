""" solve.py for 10773번. 제로 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(k: int) -> int:
    stack = []

    for _ in range(k):
        num = sys_input()
        if num == "0":
            if stack:
                stack.pop()
        else:
            stack.append(num)

    return sum(map(int, stack))


def main() -> None:
    k = int(sys_input())

    answer: int = solve(k)
    print(answer)


if __name__ == "__main__":
    main()
