""" solve.py for 10799번. 쇠막대기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target_str: str) -> int:
    count = 0
    open_brackets = 0
    prev = ""

    for ch in target_str:
        if ch == "(":
            open_brackets += 1
        elif ch == ")":
            open_brackets -= 1
            if prev == "(":
                count += open_brackets
            else:
                count += 1
        prev = ch

    return count


def main() -> None:
    target_str = sys_input()

    answer: int = solve(target_str)
    print(answer)


if __name__ == "__main__":
    main()
