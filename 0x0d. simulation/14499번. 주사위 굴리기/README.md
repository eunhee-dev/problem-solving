# 14499번. 주사위 굴리기

## 문제
https://www.acmicpc.net/problem/14499

---

## Key Points

1. 주사위 굴리기 + 문제 조건에 맞게 구현해주면 되는 문제이다.

2. 주사위가 굴러가면 각 면의 위치가 어떻게 바뀌는지를 잘 관찰해보면 된다.

    - 주사위의 윗면(top)이 굴리는 방향으로 간다고 생각하면 쉽다.

    - 동/서쪽으로 굴리는 경우: top, right, bottom, left이 각각 +1/-1 만큼 rotate 된다.

    - 북/남쪽으로 굴리는 경우: top, front, bottom, back이 각각 -1/+1 만큼 rotate 된다.
