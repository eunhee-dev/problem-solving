""" solve.py for 1931번. 회의실 배정 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(meetings: list[tuple[int, int]]) -> int:
    meetings.sort(key=lambda x: (x[1], x[0]))
    count = 0
    time = 0
    for start, end in meetings:
        if time > start:
            continue
        count += 1
        time = end
    return count


def main() -> None:
    n = int(sys_input())
    meetings = [(s, e) for s, e in (map(int, sys_input().split()) for _ in range(n))]

    answer: int = solve(meetings)
    print(answer)


if __name__ == "__main__":
    main()
