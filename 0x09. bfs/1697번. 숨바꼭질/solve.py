""" solve.py for 1697번. 숨바꼭질 """

import sys
from collections import deque


MAX_POSITION = 100000


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, k: int) -> int:
    assert 0 <= n <= MAX_POSITION and 0 <= k <= MAX_POSITION

    queue = deque([n])
    dist = [-1] * (MAX_POSITION + 1)
    dist[n] = 0

    while queue:
        x = queue.popleft()
        # k에 도달하면 return
        if x == k:
            return dist[x]
        for nx in (2 * x, x - 1, x + 1):
            if 0 <= nx <= MAX_POSITION and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                queue.append(nx)

    raise RuntimeError("Cannot reach here.")


def solve(n: int, k: int) -> int:
    return bfs(n, k)


def main() -> None:
    n, k = map(int, sys_input().split())

    answer: int = solve(n, k)
    print(answer)


if __name__ == "__main__":
    main()
