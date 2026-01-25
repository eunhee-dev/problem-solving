# 15665번. N과 M (11)

## 문제
https://www.acmicpc.net/problem/15665

---

## Key Points

1. [15656번. N과 M (7)](../15656번.%20N과%20M%20(7)/)의 응용 문제. [[풀이 - solve.py](./solve.py)]

    - [15663번. N과 M (9)](../15663번.%20N과%20M%20(9)/)문제와 같이 중복을 제거해주면 된다.

2. `itertools`의 `product`로 좀 더 간단하게 구현 가능하다. [[풀이 - solve_itertools.py](./solve_itertools.py)]

    - 순서를 유지하면서 중복을 제거하기 위해, `set`이 아닌 `dict.fromkeys()`를 활용하여 중복을 제거해주었다.
