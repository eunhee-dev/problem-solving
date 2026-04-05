# 16236번. 아기 상어

## 문제
https://www.acmicpc.net/problem/16236

---

## Key Points

1. bfs를 사용하여 아기 상어가 먹을 수 있는 가장 가까운 물고기를 찾아주면 되는 문제이다.

    - distance 별로 구분하여, 해당 distance에 먹을 수 있는 물고기를 찾으면 그 distance 까지만 탐색하고 종료한다.

    - 해당 distance에서 먹을 수 있는 물고기를 `candidates`에 저장하여, 좌표가 가장 작은 값으로 아기 상어를 이동 시키면 된다.
