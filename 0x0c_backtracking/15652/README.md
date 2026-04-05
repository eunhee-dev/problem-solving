# 15652번. N과 M (4)

## 문제
https://www.acmicpc.net/problem/15652

---

## Key Points

1. [15650번. N과 M (2)](../15650/) 문제에서 오름차순 => 비내림차순으로 바꾸면 된다. [풀이 - solve.py](./solve.py)

    - `start`가 `i + 1`이 아닌 `i`가 되면 된다. 

2. `itertools`의 `combinations_with_replacement`와 기능적으로 같다. [풀이 - solve_itertools.py](./solve_itertools.py)
