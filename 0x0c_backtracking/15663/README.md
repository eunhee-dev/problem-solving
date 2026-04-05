# 15663번. N과 M (9)

## 문제
https://www.acmicpc.net/problem/15663

---

## Key Points

1. [15654번. N과 M (5)](../15654/)의 응용 문제. [[풀이 - solve.py](./solve.py)]

    - 중복되는 수열을 출력하면 안된다.
    
    - `integers`를 정렬시켜 놓기 때문에, 직전 `integers[i]`이 현재 `integers[i]`과 같으면 스킵하면 된다.

2. `itertools`의 `permutations`로 좀 더 간단하게 구현 가능하다. [[풀이 - solve_itertools.py](./solve_itertools.py)]

    - 순서를 유지하면서 중복을 제거하기 위해, `set`이 아닌 `dict.fromkeys()`를 활용하여 중복을 제거해주었다.
