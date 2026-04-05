""" solve.py for 2170번. 선 긋기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(lines: list[tuple[int, int]]) -> int:
    lines.sort(key=lambda x: (x[0], x[1]))
    total = 0

    max_s = lines[0][0]
    max_e = lines[0][1]
    for x1, x2 in lines[1:]:
        if x1 <= max_e:
            max_e = max(max_e, x2)
        else:
            total += max_e - max_s
            max_s, max_e = x1, x2

    total += max_e - max_s

    return total


def main() -> None:
    n = int(sys_input())
    lines = [(x[0], x[1]) for x in (list(map(int, sys_input().split())) for _ in range(n))]

    answer: int = solve(lines)
    print(answer)


if __name__ == "__main__":
    main()
