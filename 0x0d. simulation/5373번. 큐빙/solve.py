""" solve.py for 5373번. 큐빙 """

import sys


UP = 0
DOWN = 1
FRONT = 2
BACK = 3
LEFT = 4
RIGHT = 5
COLORS = ["w", "y", "r", "o", "g", "b"]


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def rotate_cw(face: list[list[str]]):
    return [list(row) for row in zip(*face[::-1])]


def rotate(cube: list[list[list[str]]], op: str):
    target_face, direction = op[0], op[1]
    rot_num = 3 if direction == "-" else 1

    for _ in range(rot_num):
        if target_face == "U":
            cube[UP] = rotate_cw(cube[UP])
            for i in range(3):
                f, r, b, l = (cube[FRONT][0][i], cube[RIGHT][0][i],
                              cube[BACK][2][2 - i], cube[LEFT][0][i])
                cube[FRONT][0][i] = r
                cube[RIGHT][0][i] = b
                cube[BACK][2][2-i] = l
                cube[LEFT][0][i] = f

        elif target_face == "D":
            cube[DOWN] = rotate_cw(cube[DOWN])
            for i in range(3):
                f, r, b, l = (cube[FRONT][2][i], cube[RIGHT][2][i],
                              cube[BACK][0][2 - i], cube[LEFT][2][i])
                cube[FRONT][2][i] = l
                cube[RIGHT][2][i] = f
                cube[BACK][0][2-i] = r
                cube[LEFT][2][i] = b

        elif target_face == "F":
            cube[FRONT] = rotate_cw(cube[FRONT])
            for i in range(3):
                u, r, d, l = (cube[UP][2][i], cube[RIGHT][i][0],
                              cube[DOWN][0][2 - i], cube[LEFT][2 - i][2])
                cube[UP][2][i] = l
                cube[RIGHT][i][0] = u
                cube[DOWN][0][2-i] = r
                cube[LEFT][2-i][2] = d

        elif target_face == "B":
            cube[BACK] = rotate_cw(cube[BACK])
            for i in range(3):
                u, r, d, l = (cube[UP][0][i], cube[RIGHT][i][2],
                              cube[DOWN][2][2-i], cube[LEFT][2-i][0])
                cube[UP][0][i] = r
                cube[RIGHT][i][2] = d
                cube[DOWN][2][2-i] = l
                cube[LEFT][2-i][0] = u

        elif target_face == "L":
            cube[LEFT] = rotate_cw(cube[LEFT])
            for i in range(3):
                u, f, d, b = (cube[UP][i][0], cube[FRONT][i][0],
                              cube[DOWN][i][0], cube[BACK][i][0])
                cube[UP][i][0] = b
                cube[FRONT][i][0] = u
                cube[DOWN][i][0] = f
                cube[BACK][i][0] = d

        elif target_face == "R":
            cube[RIGHT] = rotate_cw(cube[RIGHT])
            for i in range(3):
                u, f, d, b = (cube[UP][i][2], cube[FRONT][i][2],
                              cube[DOWN][i][2], cube[BACK][i][2])
                cube[UP][i][2] = f
                cube[FRONT][i][2] = d
                cube[DOWN][i][2] = b
                cube[BACK][i][2] = u


def solve(ops: list[str]) -> list[list[str]]:
    cube = [[[color] * 3 for _ in range(3)] for color in COLORS]
    for op in ops:
        rotate(cube, op)
    return cube[0]


def main() -> None:
    t = int(sys_input())
    for _ in range(t):
        _ = int(sys_input())
        ops = sys_input().split()

        answer: list[list[str]] = solve(ops)
        for row in answer:
            print(*row, sep="")


if __name__ == "__main__":
    main()
