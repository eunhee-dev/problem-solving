# 14891번. 톱니바퀴

## 문제
https://www.acmicpc.net/problem/14891

---

## Key Points

1. 이 문제는 각 회전에 대해 주변 톱니바퀴가 어떻게 움직일지 bfs로 구현해주면 되는 문제이다.

    - 왼쪽, 오른쪽만 신경써줘서 구현해주면 된다.

    - `x`를 회전시키기 전에 미리 `x_right_pole`과 `x_left_pole`을 계산해 놓아야 함

    - 회전시키기 편하게 `wheels`를 `list[deque[int]]`로 받는 것이 포인트
