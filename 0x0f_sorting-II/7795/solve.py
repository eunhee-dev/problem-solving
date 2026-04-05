""" solve.py for 7795번. 먹을 것인가 먹힐 것인가 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(a: list[int], b: list[int]) -> int:
    a.sort()
    b.sort()

    total_pairs = 0
    b_idx = 0

    for num_a in a:
        while b_idx < len(b) and b[b_idx] < num_a:
            b_idx += 1
        total_pairs += b_idx  # 0 ~ b_idx-1 까지 총 b_idx 개

    return total_pairs


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        _ = sys_input()
        a = list(map(int, sys_input().split()))
        b = list(map(int, sys_input().split()))

        answer: int = solve(a, b)
        print(answer)


if __name__ == "__main__":
    main()
