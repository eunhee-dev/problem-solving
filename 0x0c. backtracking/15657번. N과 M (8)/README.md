# 15657번. N과 M (8)

## 문제
https://www.acmicpc.net/problem/15657

---

## Key Points

1. [15652번. N과 M (4)](../15651번.%20N과%20M%20(4)/) 문제와 똑같다. [[풀이 - solve.py](./solve.py)]

    - `integers`를 정렬한 뒤, `path`에 있는 `i` 대신 `integers[i]`를 `sequences`에 넣어주면 된다.

2. `itertools`의 `combinations_with_replacement`로 간단하게 구현 가능하다. [[풀이 - solve_itertools.py](./solve_itertools.py)]
