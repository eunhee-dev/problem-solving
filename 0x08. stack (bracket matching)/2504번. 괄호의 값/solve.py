""" solve.py for 2504번. 괄호의 값 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(target_str: str) -> int:
    stack = []
    pairs = {
        ")": ("(", 2),
        "]": ("[", 3)
    }

    for ch in target_str:
        if ch in "([":
            stack.append(ch)

        else:
            if ch not in pairs:
                return 0

            # 바로 앞에 숫자가 쌓여 있으면 다 합산
            to_be_sum = 0
            while stack and isinstance(stack[-1], int):
                to_be_sum += stack.pop()

            ch_open, val = pairs[ch]

            # 여는 괄호가 없거나 다른 괄호가 안닫혀 있지 않아야 함
            if not stack or stack[-1] != ch_open:
                return 0

            stack.pop()  # 여는 괄호 제거

            # to_be_sum == 0 이면 단일 괄호 () or [] 이므로 val,
            # 아니면 중첩 괄호로 val * to_be_sum
            stack.append(val if not to_be_sum else val * to_be_sum)

    # 스택에 문자가 포함되어 있지 않아야 함
    if any(isinstance(v, str) for v in stack):
        return 0

    return sum(stack)


def main() -> None:
    target_str = sys_input()

    result: int = solve(target_str)
    print(result)


if __name__ == "__main__":
    main()
