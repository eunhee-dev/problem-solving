import sys


DIRECTIONS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

memo_curves = {}
memo_curves[(0, 0)] = [(0, 0), (0, 1)]  # curves_memo[(g, d)]: g세대 d방향 시작 드래곤 커브 좌표 메모


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate_ccw(curve: list[tuple[int ,int]]) -> list[tuple[int, int]]:
    return [(-y, x) for x, y in curve]


def get_curve(g: int, d: int) -> list[tuple[int, int]]:
    if (g, d) in memo_curves:
        return memo_curves.get((g, d))

    if (g, 0) not in memo_curves:
        prev_curve = get_curve(g - 1, 0)
        end_x, end_y = prev_curve[-1]
        new_points = []

        # (0, 0) 으로 평행 이동 => 시계 방향 회전 => 끝 점으로 평행 이동
        for x, y in reversed(prev_curve[:-1]):
            x, y = x - end_x, y - end_y
            x, y = y, -x
            x, y = x + end_x, y + end_y
            new_points.append((x, y))

        memo_curves[(g, 0)] = prev_curve + new_points

    for i in range(1, d + 1):
        if (g, i) not in memo_curves:
            memo_curves[(g, i)] = rotate_ccw(memo_curves[(g, i - 1)])

    return memo_curves.get((g, d))


def solve(curves_info: list[tuple[int, int, int, int]]) -> int:
    count = 0
    board = [[0] * 101 for _ in range(101)]

    for y, x, d, g in curves_info:  # (x, y): (행, 열)로 변환
        curve = get_curve(g, d)
        for cx, cy in curve:
            board[x + cx][y + cy] = 1

    for x in range(100):
        for y in range(100):
            if all((board[x][y], board[x+1][y], board[x][y+1], board[x+1][y+1])):
                count += 1

    return count


def main() -> None:
    n = int(sys_input())
    curves_info = [tuple(map(int, sys_input().split())) for _ in range(n)]

    answer: int = solve(curves_info)
    print(answer)


if __name__ == "__main__":
    main()
