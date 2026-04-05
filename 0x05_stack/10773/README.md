# 10773번. 제로

## 문제
https://www.acmicpc.net/problem/10773

---

## Key Points

1. `0`이 들어오면 stack을 pop하고, 다른 정수가 들어오면 stack에 append 한 후, 마지막에 stack의 합을 구한다.

2. 이 문제의 경우 입력받는 즉시 stack에 반영하는게 자연스러워서, K개의 정수 입력은 `solve()` 함수에서 받았다.

3. `sum()`을 쓰는 대신에 for문에서 합을 계산하는 코드를 작성할 수도 있다.

    ```python
    # for문에서 합 계산 처리
    def solve(k: int) -> int:
        stack = []
        total = 0

        for _ in range(k):
            num = sys_input()

            if num == "0":
                if stack:
                    total -= stack.pop()

            else:
                num = int(num)
                stack.append(num)
                total += num

        return total
    ```

    - 그러나 `sum()`이 더 빠르다.
        - `sum()`은 C level에서 구현된 함수
        - for문에서의 덧셈/뺄셈은 python level이라 더 느림

    - `sum()`으로 처리하는 것이 더 깔끔하고 pythonic 하다.
        - python은 가독성을 중요시한다.
