""" solve_no_counter.py for 1919번. 애너그램 만들기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(s1: str, s2: str) -> int:
    s1_dict, s2_dict = {}, {}

    for ch in s1:
        s1_dict[ch] = s1_dict.get(ch, 0) + 1
    for ch in s2:
        s2_dict[ch] = s2_dict.get(ch, 0) + 1

    keys = set(s1_dict) | set(s2_dict)
    return sum(abs(s1_dict.get(ch, 0) - s2_dict.get(ch, 0)) for ch in keys)


def main() -> None:
    s1 = sys_input()
    s2 = sys_input()

    answer: int = solve(s1, s2)
    print(answer)


if __name__ == "__main__":
    main()
