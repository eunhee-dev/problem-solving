# 2480번. 주사위 세개

## 문제
https://www.acmicpc.net/problem/2480

---

## Key Points

1. 조건 순서가 중요하다: 3개 같음 → 2개 같음 → 모두 다름 순으로 체크해야 한다.


2. 2개 같은 경우, `b in (a, c)`이면 b가 같은 눈이고, `a==c`이면 `a`가 같은 눈이다. [[풀이 - solve.py](./solve.py)]


3. `Counter`를 활용하면 좀 더 의미를 살려 명확하게 코딩할 수 있다. [[풀이 - solve_counter.py](./solve_counter.py)]
    - 원소의 개수가 몇개인지 세 주기 -> 최빈값 구하기에 활용 가능 : `most_common`
        - `most_common(k)` 로 top-k 쉽게 구할 수 있음
        - ref) https://he-kate1130.tistory.com/123
    - Note) 삼성 코테에서도 `collections` 사용 가능
