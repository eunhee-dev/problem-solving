# 3273번. 두 수의 합

## 문제
https://www.acmicpc.net/problem/3273

---

## Key Points

1. 각각의 `a_i`에 대해, `candidate`에 없으면 `x - a_i` 값을 저장하고, 있으면 제거하고 count를 하면 O(n)에 풀 수 있다. [풀이 - solve.py](./solve.py)

    - `a_i`가 서로 다른 수라는 조건이 있으므로, list 대신 set을 활용하면 공간을 절약할 수 있다.

2. 나중에 배우게 될 투포인터 알고리즘으로도 풀이가 가능하다. 정렬 때문에 O(nlogn). [풀이 - solve_two_pointer.py](./solve_two_pointer.py)
