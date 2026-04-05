""" solve.py for 1267. 핸드폰 요금 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(calls: list[int]) -> str:
    y_cost = sum((c // 30 + 1) * 10 for c in calls)
    m_cost = sum((c // 60 + 1) * 15 for c in calls)

    if y_cost < m_cost:
        return f"Y {y_cost}"
    if m_cost < y_cost:
        return f"M {m_cost}"
    return f"Y M {y_cost}"


def main() -> None:
    _ = int(sys_input())
    calls = list(map(int, sys_input().split()))

    answer: str = solve(calls)
    print(answer)


if __name__ == "__main__":
    main()
