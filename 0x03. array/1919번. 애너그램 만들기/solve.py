""" solve.py for 1919번. 애너그램 만들기 """

import sys
from collections import Counter


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s1: str, s2: str) -> int:
    s1_count = Counter(s1)
    s2_count = Counter(s2)
    return sum((s1_count - s2_count).values()) + sum((s2_count - s1_count).values())


def main() -> None:
    s1 = sys_input()
    s2 = sys_input()

    answer: int = solve(s1, s2)
    print(answer)


if __name__ == "__main__":
    main()
