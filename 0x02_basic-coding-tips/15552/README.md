# 15552번. 빠른 A+B

## 문제
https://www.acmicpc.net/problem/15552

---

## Key Points

1. T가 최대 1,000,000이므로 입출력 최적화가 필수다.

    - 입력: `sys.stdin.readline()` 사용

    - 출력: `print()`를 여러 번 호출하는 대신 `"\n".join()`으로 합쳐서 `sys.stdout.write()`로 한 번에 출력한다.
