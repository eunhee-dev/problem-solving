""" solve.py for 5014번. 스타트링크 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(f: int, s: int, g: int, u: int, d: int) -> int:
    queue = deque([s - 1])
    dist = [-1] * f
    dist[s - 1] = 0

    while queue:
        x = queue.popleft()
        if x == g - 1:
            return dist[x]
        for nx in [x + u, x - d]:
            if 0 <= nx < f and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                queue.append(nx)
    return dist[g - 1]


def solve(f: int, s: int, g: int, u: int, d: int) -> str:
    min_push_button = bfs(f, s, g, u, d)
    return str(min_push_button) if min_push_button != -1 else "use the stairs"


def main() -> None:
    f, s, g, u, d = map(int, sys_input().split())

    answer: str = solve(f, s, g, u, d)
    print(answer)


if __name__ == '__main__':
    main()
