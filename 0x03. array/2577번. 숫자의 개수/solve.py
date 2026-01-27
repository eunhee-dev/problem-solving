""" solve.py for 2577번. 숫자의 개수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: int, b: int, c: int) -> str:
    counts = [0] * 10
    num = str(a * b * c)
    for ch in num:
        counts[int(ch)] += 1
    return "\n".join(str(cnt) for cnt in counts)


def main() -> None:
    a = int(sys_input())
    b = int(sys_input())
    c = int(sys_input())

    answer: str = solve(a, b, c)
    print(answer)


if __name__ == "__main__":
    main()
