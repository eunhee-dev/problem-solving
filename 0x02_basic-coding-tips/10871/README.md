# 10871번. X보다 작은 수

## 문제
https://www.acmicpc.net/problem/10871

---

## Key Points
- List comprehension을 사용하면 간단하게 구현 가능하다.

    ```python
    answer: list[int] = [num for num in a if num < x]
    print(*answer)
    ```

    - `list`, `tuple` 같이 iterable한 객체 앞에 `*`를 붙이면 언패킹이 가능하다.

    - `print()` 함수는 기본 구분자 `sep = ' '`를 사용하기 때문에 한 칸 띄워서 출력 가능하다.

- python에서는 `list` 크기를 동적으로 할당하기 때문에 n이 필요 없다.
