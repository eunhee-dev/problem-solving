""" solve_2.py for 1439번. 뒤집기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target_str: str) -> int:
    cnt = 0
    for i in range(len(target_str) - 1):
        if target_str[i] != target_str[i + 1]:
            cnt += 1
    return (cnt + 1) // 2


def main() -> None:
    target_str = sys_input()

    answer: int = solve(target_str)
    print(answer)


if __name__ == "__main__":
    main()
