import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(w: int, l: int, trucks: deque[int]) -> int:
    total_time = 0
    bridge = deque([0] * w, maxlen=w)
    sum_bridge = 0

    while bridge:
        finished_truck = bridge.pop()
        if finished_truck:
            sum_bridge -= finished_truck

        if trucks:
            if trucks[0] <= l - sum_bridge:
                truck = trucks.popleft()
                bridge.appendleft(truck)
                sum_bridge += truck
            else:
                bridge.appendleft(0)
        total_time += 1

    return total_time


def main() -> None:
    _, w, l = map(int, sys_input().split())
    trucks = deque(map(int, sys_input().split()))

    answer: int = solve(w, l, trucks)
    print(answer)


if __name__ == "__main__":
    main()
