""" solve.py for 3986번. 좋은 단어 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


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


def main() -> None:
    n = int(sys_input())
    strs = (sys_input() for _ in range(n))

    answer: int = sum(1 for s in strs if solve(s))
    print(answer)


if __name__ == "__main__":
    main()
