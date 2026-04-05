""" solve.py for 16987번. 계란으로 계란치기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, eggs: list[list[int]]) -> int:
    max_cnt = 0
    broken_eggs = []
    is_broken = [False] * n

    def backtrack(curr_idx: int) -> None:
        nonlocal max_cnt
        if curr_idx == n:
            max_cnt = max(max_cnt, len(broken_eggs))
            return

        if is_broken[curr_idx]:
            backtrack(curr_idx + 1)
        else:
            target_remained = False

            for target_idx in range(n):
                if target_idx == curr_idx:
                    continue
                if is_broken[target_idx]:
                    continue
                target_remained = True
                eggs[curr_idx][0] -= eggs[target_idx][1]
                eggs[target_idx][0] -= eggs[curr_idx][1]
                if eggs[curr_idx][0] <= 0:
                    broken_eggs.append(curr_idx)
                    is_broken[curr_idx] = True
                if eggs[target_idx][0] <= 0:
                    broken_eggs.append(target_idx)
                    is_broken[target_idx] = True

                backtrack(curr_idx + 1)

                eggs[curr_idx][0] += eggs[target_idx][1]
                eggs[target_idx][0] += eggs[curr_idx][1]
                if is_broken[curr_idx]:
                    is_broken[curr_idx] = False
                    broken_eggs.pop()
                if is_broken[target_idx]:
                    is_broken[target_idx] = False
                    broken_eggs.pop()

            if not target_remained:
                backtrack(n)

    backtrack(0)
    return max_cnt


def main() -> None:
    n = int(sys_input())
    eggs = [list(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(n, eggs)
    print(answer)


if __name__ == "__main__":
    main()
