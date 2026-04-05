""" solve.py for 14891번. 톱니바퀴 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate_bfs(wheels: list[deque[int]], start_x: int, start_direction: int) -> None:
    is_rotated = [False] * 4
    queue = deque([(start_x, start_direction)])
    while queue:
        x, direction = queue.popleft()
        is_rotated[x] = True

        x_right_pole = wheels[x][2]
        x_left_pole = wheels[x][-2]

        wheels[x].rotate(direction)

        if x + 1 < 4 and not is_rotated[x + 1] and x_right_pole != wheels[x + 1][-2]:
            queue.append((x + 1, -direction))
        if x - 1 >= 0 and not is_rotated[x - 1] and x_left_pole != wheels[x - 1][2]:
            queue.append((x - 1, -direction))


def solve(wheels: list[deque[int]], rotates: list[tuple[int, int]]) -> int:
    for num, direction in rotates:
        rotate_bfs(wheels, num - 1, direction)
    return sum(2 ** i for i in range(4) if wheels[i][0] == 1)


def main() -> None:
    wheels = [deque(map(int, sys_input())) for _ in range(4)]
    k = int(sys_input())
    rotates = [tuple(map(int, sys_input().split())) for _ in range(k)]

    answer: int = solve(wheels, rotates)
    print(answer)


if __name__ == "__main__":
    main()
