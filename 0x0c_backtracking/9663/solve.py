""" solve.py for 9663번. N-Queen """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int) -> int:
    is_used_col = [False] * n
    is_used_diag1 = [False] * (2*n - 1)  # ↙ 대각선: row + col = 0 ~ 2n-2
    is_used_diag2 = [False] * (2*n - 1)  # ↘ 대각선: row - col + (n-1) = 0 ~ 2n-2

    def backtrack(row_idx: int) -> int:
        if row_idx == n:
            return 1
        count = 0
        for col_idx in range(n):
            diag1 = row_idx + col_idx
            diag2 = row_idx - col_idx + (n - 1)
            if is_used_col[col_idx] or is_used_diag1[diag1] or is_used_diag2[diag2]:
                continue
            is_used_col[col_idx] = True
            is_used_diag1[diag1] = True
            is_used_diag2[diag2] = True
            count += backtrack(row_idx + 1)
            is_used_col[col_idx] = False
            is_used_diag1[diag1] = False
            is_used_diag2[diag2] = False
        return count

    return backtrack(0)


def main() -> None:
    n = int(sys_input())

    answer: int = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
