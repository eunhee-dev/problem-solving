# 1919번. 애너그램 만들기

## 문제
https://www.acmicpc.net/problem/1919

---

## Key Points

1. `collections`의 `Counter`의 빼기(`__sub__`)를 활용하면 쉽게 구현 가능하다. \[[풀이 - solve.py](./solve.py)\]

2. `Counter`를 안쓰고 raw하게 구현하면 다음과 같다.

   ```python
    def main(s1: str, s2: str) -> int:
        s1_dict = {}
        s2_dict = {}

        for ch in s1:
            if not s1_dict.get(ch):
                s1_dict[ch] = 1
            else:
                s1_dict[ch] += 1
            if not s2_dict.get(ch):
                s2_dict[ch] = 0

        for ch in s2:
            if not s2_dict.get(ch):
                s2_dict[ch] = 1
            else:
                s2_dict[ch] +=1
            if not s1_dict.get(ch):
                s1_dict[ch]  = 0

        ans = 0
        for ch in s1_dict:
            min_val = min(s1_dict.get(ch), s2_dict.get(ch))
            ans += s1_dict.get(ch) - min_val
            ans += s2_dict.get(ch) - min_val
        return ans
    ```

    - `dict.get()`, `set()`, `abs()`, `sum()` 등의 내장 함수를 적절히 사용하면 깔끔한 구현이 가능하다. \[[풀이 - solve_no_counter.py](./solve_no_counter.py)\]
