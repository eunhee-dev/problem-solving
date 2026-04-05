""" solve_n.py for 2478번. 자물쇠 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, target_seq: list[int]) -> tuple[int, tuple[int, int], int]:
    target_seq = list(map(lambda x: x - 1, target_seq))

    trends = []
    change_points = []
    for i in range(n):
        expected_asc_val = (target_seq[i] + 1) % n
        expected_desc_val = (target_seq[i] - 1) % n
        actual_val = target_seq[(i + 1) % n]
        if expected_asc_val == actual_val:
            trends.append("+")
        elif expected_desc_val == actual_val:
            trends.append("-")
        else:
            trends.append("x")
            change_points.append(i)

    p, q = -1, -1
    if not change_points:
        p, q = n - 1, n - 2
    else:
        for idx in change_points:
            if trends[(idx - 1) % n] == "+" and trends[(idx + 1) % n] == "-":
                p = (idx + 1) % n
            elif trends[(idx - 1) % n] == "-" and trends[(idx + 1) % n] == "+":
                q = idx

    k2 = 0
    while True:
        p = (p + 1) % n
        q = (q + 1) % n
        k2 += 1
        if p < q:
            if p == 0:
                k1 = target_seq[(q - k2) % n]
            else:
                k1 = target_seq[-k2]
            if k1 != 0:
                return k1, (p + 1, q + 1), k2


def main() -> None:
    n = int(sys_input())
    target_seq = list(map(int, sys_input().split()))

    answer: tuple[int, tuple[int, int], int] = solve(n, target_seq)
    print(answer[0])
    print(*answer[1])
    print(answer[2])


if __name__ == "__main__":
    main()
