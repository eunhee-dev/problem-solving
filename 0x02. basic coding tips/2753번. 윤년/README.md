# 2753번. 윤년

## 문제
https://www.acmicpc.net/problem/2753

---

## Key Points

1. 문제에 적힌 윤년 조건에 따라 if문과 and/or 조건을 활용하여 윤년 판별이 가능하다.


2. `return 1 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 0`과 같이 한 줄로 작성도 가능하다.


3. python의 `calendar` 모듈을 사용할 수도 있다.

    ```python
    from calendar import isleap

    def solve(year: int) -> int:
        return 1 if isleap(year) else 0
    ```
