""" solve.py for 13913번. 숨바꼭질 4 """

import sys
from collections import deque


MAX_POSITION = 100000


def sys_input():
    return sys.stdin.readline().rstrip()


def bfs(n: int, k: int) -> tuple[int, list[int]]:
    assert 0 <= n <= MAX_POSITION and 0 <= k <= MAX_POSITION

    queue = deque([n])
    dist = [-1] * (MAX_POSITION + 1)
    prev_history = [-1] * (MAX_POSITION + 1)
    dist[n] = 0

    while queue:
        x = queue.popleft()
        if x == k:
            return dist[k], prev_history
        for nx in (2 * x, x - 1, x + 1):
            if 0 <= nx <= MAX_POSITION and dist[nx] == -1:
                dist[nx] = dist[x] + 1
                prev_history[nx] = x
                queue.append(nx)

    raise RuntimeError("[-] Cannot reach here.")


def solve(n: int, k: int) -> tuple[int, str]:
    min_time, prev_history = bfs(n, k)

    curr = k
    path = deque([k])

    # 경로 복원
    while curr != n:
        prev = prev_history[curr]
        path.appendleft(prev)
        curr = prev

    return min_time, " ".join(map(str, path))


def main() -> None:
    n, k = map(int, sys_input().split())

    answer: tuple[int, str] = solve(n, k)
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    main()
