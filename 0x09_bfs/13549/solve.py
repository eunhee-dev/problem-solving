""" solve.py for 13549번. 숨바꼭질 3 """

import sys
from collections import deque


MAX_POSITION = 100000


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, k: int) -> int:
    assert 0 <= n <= MAX_POSITION and 0 <= k <= MAX_POSITION

    deq = deque([n])
    dist = [-1] * (MAX_POSITION + 1)
    dist[n] = 0

    while deq:
        x = deq.popleft()
        if x == k:
            return dist[x]
        for nx in [2*x, x-1, x+1]:
            if not (0 <= nx <= MAX_POSITION) or dist[nx] != -1:
                continue
            if nx == 2 * x:
                dist[nx] = dist[x]
                deq.appendleft(nx)
            else:
                dist[nx] = dist[x] + 1
                deq.append(nx)

    raise RuntimeError("[-] Cannot reach here.")


def solve(n: int, k: int) -> int:
    return bfs(n, k)


def main() -> None:
    n, k = map(int, sys_input().split())

    answer: int = solve(n, k)
    print(answer)


if __name__ == "__main__":
    main()
