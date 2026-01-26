""" solve.py for 1541번. 잃어버린 괄호 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(equation: str) -> int:
    equation_parts = equation.split("-")

    first_part = equation_parts[0]
    total = sum(map(int, first_part.split("+")))

    for part in equation_parts[1:]:
        total -= sum(map(int, part.split("+")))

    return total


def main() -> None:
    equation = sys_input()

    answer: int = solve(equation)
    print(answer)


if __name__ == "__main__":
    main()
