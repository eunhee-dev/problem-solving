# 14889번. 스타트와 링크

## 문제
https://www.acmicpc.net/problem/14889

---

## Key Points

1. 이 문제는 아래와 같이 나누어 생각하면 좋다.

    - 모든 team1 조합 구하기

    - 각 team1에 대해 team2 구하기

    - 각 팀의 시너지 합 구해서 최소값 업데이트 하기

2. `itertools.combinations`를 사용하면 쉽게 team1 조합을 구할 수 있다.

    - 백트래킹으로도 구현 가능하지만, 얻을 수 있는 이점이 거의 없다.

3. team2는 전체 멤버와 team1을 set()으로 바꿔서 빼면 쉽게 구할 수 있다.
