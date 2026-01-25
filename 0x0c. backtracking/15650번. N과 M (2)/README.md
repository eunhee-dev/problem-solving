# 15650번. N과 M (2)

## 문제
https://www.acmicpc.net/problem/15650

---

## Key Points

1. [15649번. N과 M (1)](../15649번.%20N과%20M%20(1)/) 문제에서 순열이 오름차순이 되도록 조건만 추가하면 된다. [풀이 - solve.py](./solve.py)

    - i를 1이 아닌 `start`에서 시작하게 하면 된다. (`start`는 직전 호출 i에 1을 더한 값이다.)

    - 숫자 중복 방지를 위한 `is_used` 배열은 `range(start, n+1)`로 인해 없어도 된다. (`i`가 오름차순이기 때문에 중복될 수 없다.)

2. 마찬가지로 `itertools`의 `combinations`를 사용하면 간단하게 구현 가능하다. [풀이 - solve_itertools.py](./solve_itertools.py)
