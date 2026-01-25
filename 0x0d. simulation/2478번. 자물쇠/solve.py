""" solve.py for 2478번. 자물쇠 """

import sys
from collections import deque


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, target_seq: list[int]) -> tuple[int, tuple[int, int], int]:
    org_seq = list(range(n))
    target_seq = list(map(lambda x: x - 1, target_seq))

    for k2 in range(1, n):
        cand_seq = deque(target_seq[::])
        cand_seq.rotate(k2)
        cand_seq = list(cand_seq)

        p, q = -1, -1
        for i in range(n):
            expected_val = (cand_seq[i] + 1) % n
            actual_val = cand_seq[(i + 1) % n]
            if expected_val != actual_val:
                p = (i + 1) % n
                break
        if p == -1:
            continue

        for i in range(p + 1, n):
            excepted_val = (cand_seq[i] - 1) % n
            actual_val = cand_seq[(i + 1) % n]
            if excepted_val != actual_val:
                q = i
                break
        if q == -1:
            p, q = 0, n - 1

        cand_seq = cand_seq[:p] + list(reversed(cand_seq[p:q + 1])) + cand_seq[q + 1:]

        k1 = cand_seq[0]
        if k1 == 0:
            continue

        cand_seq = deque(cand_seq)
        cand_seq.rotate(k1)
        cand_seq = list(cand_seq)

        if cand_seq == org_seq:
            return k1, (p + 1, q + 1), k2

    raise ValueError("[-] Wrong input.")


def main() -> None:
    n = int(sys_input())
    target_seq = list(map(int, sys_input().split()))

    answer: tuple[int, tuple[int, int], int] = solve(n, target_seq)
    print(answer[0])
    print(*answer[1])
    print(answer[2])


if __name__ == "__main__":
    main()
