""" solve.py for 6549번. 히스토그램에서 가장 큰 직사각형 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(n: int, heights: list[int]) -> int:
    stack = []
    max_area = 0

    for idx, height in enumerate(heights):
        # 오작수 구하기 (작은 사각형이 나오면, 더 큰 사각형들 모두 스택에서 제거)
        while stack and heights[stack[-1]] > height:
            prev_idx = stack.pop()
            # idx: heights[prev_idx]의 오작수 인덱스
            # width 계산 (스택이 비어있으면 제일 앞까지의 거리)
            width = idx - stack[-1] - 1 if stack else idx
            max_area = max(max_area, width * heights[prev_idx])
        stack.append(idx)

    # 남은 스택(오작수가 없는 경우)에 대한 처리 => 끝을 기준으로 함
    while stack:
        remaining_idx = stack.pop()
        width = n - stack[-1] - 1 if stack else n
        max_area = max(max_area, width * heights[remaining_idx])

    return max_area


def main() -> None:
    while True:
        line = list(map(int, sys_input().split()))
        n = line[0]
        if n == 0:
            break
        heights = line[1:]

        answer: int = solve(n, heights)
        print(answer)


if __name__ == "__main__":
    main()
