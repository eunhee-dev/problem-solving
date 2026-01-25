""" solve.py for 17471번. 게리맨더링 """

import sys
from itertools import combinations
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def is_connected(group: set[int], graph: list[list[int]]) -> bool:
    if not group:
        return False

    start = next(iter(group))
    queue = deque([start])
    visited = {start}

    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if neighbor in group and neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return len(visited) == len(group)


def solve(n: int, populations: list[int], graph: list[list[int]]) -> int:
    min_diff = sys.maxsize
    all_district = set(range(n))
    for i in range(n // 2 + 1):
        for group_a in combinations(range(n), i):
            group_a = set(group_a)
            group_b = all_district - group_a

            if is_connected(group_a, graph) and is_connected(group_b, graph):
                sum_a = sum(populations[d] for d in group_a)
                sum_b = sum(populations[d] for d in group_b)
                min_diff = min(min_diff, abs(sum_a - sum_b))

    return min_diff if min_diff != sys.maxsize else -1


def main() -> None:
    n = int(sys_input())
    populations = list(map(int, sys_input().split()))
    graph = [list(map(lambda x: x - 1, map(int, sys_input().split()[1:]))) for _ in range(n)]

    answer: int = solve(n, populations, graph)
    print(answer)


if __name__ == "__main__":
    main()
