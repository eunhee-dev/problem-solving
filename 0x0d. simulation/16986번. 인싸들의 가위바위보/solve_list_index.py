""" solve_list_index.py for 16986번. 인싸들의 가위바위보 """

import sys
from itertools import permutations


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, k: int, a: list[list[int]], kh: list[int], mh: list[int]) -> int:
    kh = [hand - 1 for hand in kh]
    mh = [hand - 1 for hand in mh]

    for jw in permutations(range(n)):
        winner = -1
        wins = [0, 0, 0]

        players = [list(jw), kh, mh]
        hand_idx = [0, 0, 0]
        p1, p2 = 0, 1

        while hand_idx[0] < n:
            p1_hand = players[p1][hand_idx[p1]]
            p2_hand = players[p2][hand_idx[p2]]
            hand_idx[p1] += 1
            hand_idx[p2] += 1

            if a[p1_hand][p2_hand] == 2:
                wins[p1] += 1
                if wins[p1] == k:
                    winner = p1
                    break
                p2 = 3 - p1 - p2
            else:
                wins[p2] += 1
                if wins[p2] == k:
                    winner = p2
                    break
                p1 = 3 - p1 - p2

            p1, p2 = min(p1, p2), max(p1, p2)

        if winner == 0:
            return 1

    return 0


def main() -> None:
    n, k = map(int, sys_input().split())
    a = [list(map(int, sys_input().split())) for _ in range(n)]
    kh = list(map(int, sys_input().split()))
    mh = list(map(int, sys_input().split()))

    answer: int = solve(n, k, a, kh, mh)
    print(answer)


if __name__ == "__main__":
    main()
