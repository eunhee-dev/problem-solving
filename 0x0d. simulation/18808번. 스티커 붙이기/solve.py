""" solve.py for 18808번. 스티커 붙이기 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def stick(board: list[list[int]], paper: list[list[int]], bx: int, by: int) -> bool:
    r, c = len(paper), len(paper[0])
    sticker_coords = []
    for i in range(r):
        for j in range(c):
            if paper[i][j] != 1:
                continue
            if board[bx + i][by + j] == 1:
                return False
            sticker_coords.append((bx + i, by + j))

    for sx, sy in sticker_coords:
        board[sx][sy] = 1
    return True


def try_stick(board: list[list[int]], paper: list[list[int]]) -> bool:
    n, m = len(board), len(board[0])
    r, c = len(paper), len(paper[0])
    for bx in range(n - r + 1):
        for by in range(m - c + 1):
            if stick(board, paper, bx, by):
                return True
    return False


def rotate(paper: list[list[int]]) -> list[list[int]]:
    r, c = len(paper), len(paper[0])
    rot_paper = [[0] * r for _ in range(c)]
    for x in range(c):
        for y in range(r):
            rot_paper[x][y] = paper[r - 1 - y][x]
    return rot_paper


def solve(n: int, m: int, papers: list[list[list[int]]]) -> int:
    board = [[0] * m for _ in range(n)]
    for paper in papers:
        for _ in range(4):
            if try_stick(board, paper):
                break
            paper = rotate(paper)
    return sum(1 for x in range(n) for y in range(m) if board[x][y] == 1)


def main() -> None:
    n, m, k = map(int, sys_input().split())
    papers = []
    for _ in range(k):
        r, _ = map(int, sys_input().split())
        papers.append([list(map(int, sys_input().split())) for _ in range(r)])

    answer: int = solve(n, m, papers)
    print(answer)


if __name__ == "__main__":
    main()
