""" solve.py for 17071번. 숨바꼭질 5 """

import sys
from collections import deque


MAX_POSITION = 500000


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def bfs(n: int, dist: list[list[int]]) -> None:
    queue = deque([(n, 0)])
    dist[n][0] = 0

    while queue:
        x, t = queue.popleft()
        for nx in [x-1, x+1, 2*x]:
            if not 0 <= nx <= MAX_POSITION:
                continue
            if dist[nx][(t + 1) % 2] == -1:
                dist[nx][(t + 1) % 2] = t + 1
                queue.append((nx, t + 1))


def solve(n: int, k: int) -> int:
    dist = [[-1] * 2 for _ in range (MAX_POSITION + 1)]
    bfs(n, dist)

    # 동생을 움직여서 최소 시간 찾기
    curr_bro_loc = k
    t = 0
    while curr_bro_loc <= MAX_POSITION:
        if dist[curr_bro_loc][t % 2] <= t:  # dist에 -1은 없어 체크 안해도 됨 (짝수/홀수 시간 모두 모든 지점에 도달 가능)
            return t
        t += 1
        curr_bro_loc += t

    return -1


def main() -> None:
    n, k = map(int, sys_input().split())

    answer: int = solve(n, k)
    print(answer)


if __name__ == "__main__":
    main()
