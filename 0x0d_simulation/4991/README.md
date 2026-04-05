# 4991번. 로봇 청소기

## 문제
https://www.acmicpc.net/problem/4991

---

## Key Points

1. 더러운 칸의 수가 10가지를 넘지 않는다. => 순서 조합이 10!이여서 모든 경우의 수 탐색이 가능하다. [[풀이 - solve_naive.py](./solve_naive.py)]

    - bfs로 각 points(로봇 청소기 + 더러운 칸) 사이의 거리를 모두 구한다. (20 x 20 x 11)

    - `itertools.permutations`로 모든 순서 조합을 시도해서 가장 작은 이동 횟수를 구한다. (10!)

2. 비트마스킹과 3d-bfs를 사용하면 조금 더 효율적으로 풀이 가능하다. [[풀이 - solve.py](./solve.py)]

    - queue에 (x, y, mask)를 넣는다.
        - mask는 청소된 칸 정보를 담고있다. ex. 0010 => 2번째 더러운 칸 청소
        - 20 x 20 x 2^10의 시간복잡도로 10!보다 유리함

    - distance로 layer를 나눠놓았기 때문에, `mask == (1 << len(dirty_coords)) - 1`를 처음 만족하는 순간이 모든 칸이 청소된 최소 distance이다.

    - 1번 방식과 2번 방식을 혼합하는 방법도 좋을 것 같다. (미리 거리 구하기 + 3d-bfs)
