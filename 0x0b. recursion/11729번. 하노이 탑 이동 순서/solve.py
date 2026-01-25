""" solve.py for 11729번. 하노이 탑 이동 순서 """

import sys


POLES = {1, 2, 3}


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def record_path(src: int, dest: int, n: int, path: list[str]) -> None:
    if n == 0:
        return
    remain = (POLES - {src, dest}).pop()  # 6 - src - dest
    record_path(src, remain, n-1, path)
    path.append(f"{src} {dest}")
    record_path(remain, dest, n-1, path)


def solve(n: int) -> tuple[int, list[str]]:
    path = []
    record_path(1, 3, n, path)
    return len(path), path


def main() -> None:
    n = int(sys_input())

    answer: tuple[int, list[str]] = solve(n)
    print(answer[0])
    for path_str in answer[1]:
        print(path_str)


if __name__ == "__main__":
    main()
