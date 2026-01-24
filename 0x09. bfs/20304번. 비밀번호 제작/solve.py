""" solve.py for 20304번. 비밀번호 제작 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, p: list[int]) -> int:
    max_bin_len = n.bit_length()
    dist = [-1] * (n + 1)
    queue = deque(p)
    for p_i in p:
        dist[p_i] = 0

    next_dist = 1
    while queue:
        for _ in range(len(queue)):
            x = queue.popleft()
            for k in range(max_bin_len):
                nx = x ^ (2**k)
                if nx <= n and dist[nx] == -1:
                    dist[nx] = next_dist
                    queue.append(nx)
        next_dist += 1

    return max(dist)


def main() -> None:
    n = int(sys_input())
    _ = int(sys_input())
    p = list(map(int, sys_input().split()))

    answer: int = solve(n, p)
    print(answer)


if __name__ == "__main__":
    main()
