""" solve.py for 8980번. 택배 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, c: int, tasks: list[tuple[int, int, int]]) -> int:
    total = 0
    used = [0] * (n + 1)

    tasks.sort(key=lambda x: x[1])
    for src, dest, boxes in tasks:
        max_used = max(used[i] for i in range(src, dest))
        available = c - max_used

        load = min(boxes, available)
        total += load

        for i in range(src, dest):
            used[i] += load

    return total


def main() -> None:
    n, c = map(int, sys_input().split())
    m = int(sys_input())
    tasks = [(x[0], x[1], x[2]) for x in (list(map(int, sys_input().split())) for _ in range(m))]

    answer: int = solve(n, c, tasks)
    print(answer)


if __name__ == "__main__":
    main()
