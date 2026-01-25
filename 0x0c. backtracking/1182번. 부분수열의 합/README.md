# 1182번. 부분수열의 합

## 문제
https://www.acmicpc.net/problem/1182

---

## Key Points

1. 0 ~ n-1의 인덱스 `idx`에 대해 `intergers[idx]` 값을 더할지 말지 모든 경우의 수를 확인해보는 백트래킹 방식으로 문제 해결이 가능하다. [풀이 - solve.py](./solve.py)

    - `backtrack(idx + 1, total)`: 안 더하기

    - `backtrack(idx + 1, total + integers[idx])`: 더하기

    -  `s = 0`의 경우, 공집합을 더해서 0이 되는 케이스를 제외해줘야 하는 것을 유의해야 한다.

2. [15649번. N과 M (1)](../15649번.%20N과%20M%20(1)/) 문제와 마찬가지로, 백트래킹 연습 목적이 아니라면 `itertools의`의 `combinations`를 활용하여 쉽게 풀이가 가능하다. [풀이 - solve_itertools.py](./solve_itertools.py)
