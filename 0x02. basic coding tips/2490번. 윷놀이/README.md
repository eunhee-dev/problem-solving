# 2490번. 윷놀이

## 문제
https://www.acmicpc.net/problem/2490

---

## Key Points

1. 등(1)의 개수 = 4개 숫자의 합이므로, `sum()`으로 간단히 구할 수 있다.


2. 등의 개수에 따른 결과 매핑: `{0: 'D', 1: 'C', 2: 'B', 3: 'A', 4: 'E'}` 또는 인덱싱 `"DCBAE"[합]`으로 처리 가능하다.


3. list comprehension을 통해 간결하게 return이 가능하다.

    ```python
    # w/o list comprehension
    def solve(yuts: list[list[int]]) -> list[str]:
        result = []
        for yut in yuts:
            result.append("DCBAE"[sum(yut)])
        return result

    # w/ list comprehension
    def solve(yuts: list[list[int]]) -> list[str]:
        return ["DCBAE"[sum(yut)] for yut in yuts]
    ```
