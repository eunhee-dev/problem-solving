""" solve.py for 1439번. 뒤집기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target_str: str) -> int:
    count_zero = len([x for x in target_str.split("1") if x != ""])
    count_one = len([x for x in target_str.split("0") if x != ""])

    return min(count_zero, count_one)


def main() -> None:
    target_str = sys_input()

    answer: int = solve(target_str)
    print(answer)


if __name__ == "__main__":
    main()
