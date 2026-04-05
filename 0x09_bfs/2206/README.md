# 2206번. 벽 부수고 이동하기

## 문제
https://www.acmicpc.net/problem/2206

---

## Key Points

1. 3d-bfs와 2d-bfs 두 가지 방식으로 풀 수 있다.

2. [3d-bfs 풀이](solve.py): bfs + DP적인 요소 포함

    - 3차원으로 `dist` 배열 구성: `dist[x][y][broken_cnt]`

    - `broken_cnt < MAX_BROKEN_CNT` 이면 벽을 한 번 뿌셔보고 그 시나리오를 queue에 저장
        - 해당 시나리오에 대해서는 `broken_cnt += 1` 되는 효과

    - 나머지는 기존 bfs와 동일

3. [2d-bfs 풀이 - Combine](solve_2d_combine.py): bfs + 그리디적인 요소 포함

    - 3d-bfs 풀이는 노베이스에서 떠올리기 쉽지 않았음

    - 그래서 먼저 떠올린 풀이가 우리가 계속 하던 bfs를 2번 수행하기

        - 출발점에서 bfs 수행 후 결과 `start_dist` 맵 리턴
            - 도착점에 도달하면 `d_min = start_dist[n-1][m-1]`
            - 도달하지 못하면 `d_min = inf`

        - 도착점에서 bfs 수행 후 결과 `end_dist` 맵 리턴

    - 모든 벽에 대해서 (상, 하, 좌, 우)로 `start_dist`와 `end_dist` 에 `-1`이 아닌 값이 있으면 각각 `starts`와 `ends` 배열에 저장

    - `starts`와 `ends` 가 둘 다 하나라도 있으면, `d_min = min(d_min, min(starts) + 1 + min(ends))` 수행
        - 벽 (상, 하, 좌, 우)에 -1이 아닌 `start_dist`와 `end_dist`가 존재하는 경우를 의미
        - 벽 기준으로 나를 부셨을 때 `start_dist`와 `end_dist`가 이어지나 확인 하는 작업
        - `starts`와 `ends` 각각의 최소 값을 뽑으면 `두 최소값의 합 + 1`이 자기를 부셨을 때의 최소값이 됨 (그리디적인 요소)

4. 정리: 확장성을 고려해서라도 (벽을 2번 이상 부술 수 있는 경우) 3d-bfs가 더 깔끔한 방법임
    
    - 그러나 3d-bfs로 풀 수 있다는 사실을 모르면 쉽게 떠올리기 어려울 수 있음

    - 그런 상황에서는 3번과 같은 꼼수 방법도 가능함
