""" solve_dataclass.py for 20055번. 컨베이어 벨트 위의 로봇 """

import sys
from collections import deque
from dataclasses import dataclass


@dataclass
class Block:
    durability: int
    has_robot: bool = False


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, a: deque[Block], k: int) -> int:
    step = 0
    zero_durability_count = 0

    while zero_durability_count < k:
        step += 1

        a.rotate(1)

        if a[n - 1].has_robot:
            a[n - 1].has_robot = False

        for i in range(n - 2, -1 , -1):
            if a[i].has_robot and not a[i + 1].has_robot and a[i + 1].durability >= 1:
                a[i].has_robot, a[i + 1].has_robot = False, True
                a[i + 1].durability -= 1
                if a[i + 1].durability == 0:
                    zero_durability_count += 1

        if a[n - 1].has_robot:
            a[n - 1].has_robot = False

        if a[0].durability > 0:
            a[0].has_robot = True
            a[0].durability -= 1
            if a[0].durability == 0:
                zero_durability_count += 1

    return step


def main() -> None:
    n, k = map(int, sys_input().split())
    a =  deque(Block(int(d), False) for d in sys_input().split())

    answer: int = solve(n, a, k)
    print(answer)


if __name__ == "__main__":
    main()
