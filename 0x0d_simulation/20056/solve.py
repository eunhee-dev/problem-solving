""" solve.py for 20056번. 마법사 상어와 파이어볼 """

import sys
from collections import defaultdict


DIRECTIONS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, k: int, fireballs: list[list[int]]) -> int:
    fireballs_dict = dict(enumerate(fireballs))
    next_idx = len(fireballs)

    for _ in range(k):
        board = defaultdict(list)
        for i in fireballs_dict:
            r, c, _, s, d = fireballs_dict[i]
            dr, dc = DIRECTIONS[d]
            nr, nc = (r + dr * s) % n, (c + dc * s) % n
            board[(nr, nc)].append(i)
            fireballs_dict[i][0] = nr
            fireballs_dict[i][1] = nc

        for (r, c), ball_idxs in board.items():
            if len(ball_idxs) <= 1:
                continue
            nm = sum(fireballs_dict[i][2] for i in ball_idxs) // 5
            if nm != 0:
                ns = sum(fireballs_dict[i][3] for i in ball_idxs) // len(ball_idxs)
                d_parity = [fireballs_dict[i][4] % 2 for i in ball_idxs]
                if all(d_parity) or not any(d_parity):
                    divided_balls = [[r, c, nm, ns, nd] for nd in range(0, 8, 2)]
                else:
                    divided_balls = [[r, c, nm, ns, nd] for nd in range(1, 8 ,2)]
                for i in range(4):
                    fireballs_dict[next_idx + i] = divided_balls[i]
                next_idx += 4

            for i in ball_idxs:
                del fireballs_dict[i]

    return sum(fireball[2] for fireball in fireballs_dict.values())


def main() -> None:
    n, m, k = map(int, sys_input().split())
    fireballs = []
    for _ in range(m):
        r, c, mass, s, d = map(int, sys_input().split())
        fireballs.append([r - 1, c - 1, mass, s, d])

    answer: int = solve(n, k, fireballs)
    print(answer)


if __name__ == "__main__":
    main()
