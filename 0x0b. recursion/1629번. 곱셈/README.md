# 1629번. 곱셈

## 문제
https://www.acmicpc.net/problem/1629

---

## Key Points

1. a^(2b) = a^b * a^b 임을 활용하여 재귀를 구현하면 된다. (2b+1 일 경우 a^b * a^b * a)

2. python에서는 해당 문제 요구사항을 완전히 충족시키는 `pow(base, exp, mod)` 함수를 지원한다.

    - 실전에서는 그냥 `pow(a, b, c)` 하면 된다.

    - 참고로 `pow()` 는 CPython 기준 반복문으로 구현되어 있다.

3. python으로 구현한 반복문 코드는 아래와 같다.

    ```python
    def solve(a: int, b: int, c: int) -> int:
        result = 1
        a = a % c

        while b > 0:
            if b % 2 == 1:
                result = (result * a) % c
            a = (a * a) % c
            b //= 2
        return result

    ```
