# 2309번. 일곱 난쟁이

## 문제
https://www.acmicpc.net/problem/2309

---

## Key Points

1. 9명 중 7명을 고르는 것 = 제외할 2명을 찾는 것


2. `전체 합 - 100 = 제외할 2명의 키 합`으로 문제를 단순화할 수 있다.


3. 이중 for문(`i`, `j = i+1`)으로 2명 조합을 순회하며 합이 맞는 쌍을 찾는다. [[풀이 - solve.py](./solve.py)]


3. `itertools.combinations`로 더 간결하게 구현할 수 있다. [[풀이 - solve_itertools.py](./solve_itertools.py)]
