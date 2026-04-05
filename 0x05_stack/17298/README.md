# 17298번. 오큰수

## 문제
https://www.acmicpc.net/problem/17298

---

## Key Points

1. monotonic stack (단조 스택) 기본 문제이다. 

2. 스택에 (index, num)을 저장하는게 직관적인 코드이지만, n이 클 수록 시간/공간 손해를 본다.

    - stack을 내림차순으로 유지하는 것을 쉽게 확인할 수 있다.

    - 따라서, n이 작으면 (index, num)을 같이 저장하는게 가독성 측면에서 더 좋은 코드이다. [[풀이 - solve_intuitive.py](./solve_intuitive.py)]

    - 본 문제에서는 n이 꽤 크기 때문에, index만 저장하는 것이 효율성 측면에서 유리하다. [[풀이 - solve.py](./solve.py)]

    ```python
    # 직관적이지만 효율성 손해 (solve_intuitive.py)
    def solve(n: int, nums: list[int]) -> list[int]:
        res = [-1] * n
        stack = []

        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                prev_idx = stack.pop()[0]
                res[prev_idx] = num
            stack.append((i, num))
        return res

    # 효율적이지만 가독성 손해 (solve.py)
    def solve(n: int, nums: list[int]) -> list[int]:
        res = [-1] * n
        stack = []

        for i, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                prev_idx = stack.pop()
                res[prev_idx] = num
            stack.append(i)
        return res
    ```
