""" solve.py for 11000번. 강의실 배정 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(time_table: list[tuple[int, int]]) -> int:
    events = []

    for s, t in time_table:
        events.append((s, 1))
        events.append((t, -1))

    events.sort(key=lambda x: (x[0], x[1]))

    curr_rooms = 0
    max_rooms = 0

    for _, state in events:
        curr_rooms += state
        max_rooms = max(max_rooms, curr_rooms)

    return max_rooms


def main() -> None:
    n = int(sys_input())
    time_table = [(int(x[0]), int(x[1])) for x in (sys_input().split() for _ in range(n))]

    answer: int = solve(time_table)
    print(answer)


if __name__ == "__main__":
    main()
