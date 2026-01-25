# 15649번. N과 M (1)

## 문제
https://www.acmicpc.net/problem/15649

---

## Key Points

1. 백트래킹 기초 문제. 재귀와 상태 복원을 통해 모든 경우 탐색 [풀이 - solve.py](./solve.py)

    - `is_used` 배열로 숫자 중복 사용 방지 (1-based로 계산하기 위해 n+1 크기로 만듬)

    - 재귀 깊이(`depth`)가 `m`에 도달하면 현재까지 뽑은 숫자들을 하나의 수열로 저장

    - 돌아올 때마다(재귀에서 복귀할 때) 상태를 원래대로 복원(`pop` + `is_used[i] = False`)하며 모든 경우를 탐색

2. 사실 이 문제는, 백트래킹 연습 목적이 아니라면 `itertools`의 `permutations`를 쓰면 쉽게 구현 가능하다. [풀이 - solve_itertools.py](./solve_itertools.py)
