""" solve_heapq.py for 8980번. 택배 """

import sys
import heapq


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, c: int, tasks: list[tuple[int, int, int]]) -> int:
    total = 0
    dest_boxes = [0] * (n + 1)
    max_heap = []
    curr = 0

    tasks.sort()
    task_idx = 0

    for town in range(1, n + 1):
        total += dest_boxes[town]
        curr -= dest_boxes[town]

        while task_idx < len(tasks) and tasks[task_idx][0] == town:
            _, dest, boxes = tasks[task_idx]
            task_idx += 1

            heapq.heappush(max_heap, -dest)
            dest_boxes[dest] += boxes
            curr += boxes

        while curr > c:
            max_dest = -heapq.heappop(max_heap)
            remain = min(dest_boxes[max_dest], curr - c)
            dest_boxes[max_dest] -= remain
            curr -= remain
            if dest_boxes[max_dest] > 0:
                heapq.heappush(max_heap, -max_dest)

    return total


def main() -> None:
    n, c = map(int, sys_input().split())
    m = int(sys_input())
    tasks = [(x[0], x[1], x[2]) for x in (list(map(int, sys_input().split())) for _ in range(m))]

    answer: int = solve(n, c, tasks)
    print(answer)


if __name__ == "__main__":
    main()
