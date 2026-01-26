""" solve.py for 1700번. 멀티탭 스케줄링 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, devices: list[int]) -> int:
    total = 0
    plugs = set()

    for i, device in enumerate(devices):
        if device in plugs:
            continue

        if len(plugs) >= n:
            farthest_idx = -1
            target_plug = -1

            for plug in plugs:
                try:
                    farthest_idx = max(farthest_idx, devices[i + 1:].index(plug))
                except ValueError:
                    target_plug = plug
                    break

            if target_plug == -1:
                target_plug = devices[i + 1:][farthest_idx]
            plugs.remove(target_plug)
            total += 1

        plugs.add(device)

    return total


def main() -> None:
    n, _ = map(int, sys_input().split())
    devices = list(map(int, sys_input().split()))

    answer: int = solve(n, devices)
    print(answer)


if __name__ == "__main__":
    main()
