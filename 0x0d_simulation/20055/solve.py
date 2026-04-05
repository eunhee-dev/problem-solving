""" solve.py for 20055번. 컨베이어 벨트 위의 로봇 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, a: deque[list[int]], k: int) -> int:
    step = 0
    zero_durability_count = 0

    while zero_durability_count < k:
        step += 1

        a.rotate(1)

        if a[n - 1][1] == 1:
            a[n - 1][1] = 0

        for i in range(n - 2, -1 , -1):
            if a[i][1] == 1 and a[i + 1][1] == 0 and a[i + 1][0] >= 1:
                a[i][1], a[i + 1][1] = 0, 1
                a[i + 1][0] -= 1
                if a[i + 1][0] == 0:
                    zero_durability_count += 1

        if a[n - 1][1] == 1:
            a[n - 1][1] = 0

        if a[0][0] > 0:
            a[0][1] = 1
            a[0][0] -= 1
            if a[0][0] == 0:
                zero_durability_count += 1

    return step


def main() -> None:
    n, k = map(int, sys_input().split())
    a =  deque([int(d), 0] for d in sys_input().split())

    answer: int = solve(n, a, k)
    print(answer)


if __name__ == "__main__":
    main()
