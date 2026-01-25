# 3190번. 뱀

## 문제
https://www.acmicpc.net/problem/3190

---

## Key Points

1. 이 문제는 설명대로 아래와 같이 나누어 생각하면 좋다.

    - 주어진 방향으로 벰 이동하기
        - 종료 조건: `board`를 벗어나거나 몸통에 부딪히면 => `board`에 snake 표시
        - 사과를 안 먹으면 꼬리 없애주기 => snake를 `deque`으로 저장

    - 벰 이동방향 회전하기
        - `DIRECTIONS`를 `[top, right, bottom, left]`로 정의하고 왼쪽이면 인덱스 -1, 오른쪽이면 +1

2. 꼬리를 없애주기 위해 `snake`를 따로 deque로 관리하면 `snake.pop()`만 하면 되어서 편하다.
