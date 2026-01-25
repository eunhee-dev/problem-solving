# 1941번. 소문난 칠공주

## 문제
https://www.acmicpc.net/problem/1941

---

## Key Points

1. 이 문제의 가장 직관적인 풀이는 `itertools`의 `combinations`를 활용해 $25C7$의 (x, y) 좌표를 뽑고, `S`가 더 많은 경우에 좌표가 서로 연결되어 있는지 bfs로 확인하는 것이다. [[풀이 - solve_itertools.py](./solve_itertools.py)]

    - 시작점을 잡아서 bfs를 돌려보고 `visited`의 길이가 7인지만 체크하면 된다. 따라서, 보통의 bfs처럼 `list`가 아니라 `set`로 `visited`를 구현하였다.
        - `visited = [[False] * 5 for _ in range(5)]`를 하면 7명을 방문했는지 체크하기가 어렵다.
        - `set`는 `(nx, ny) not in visited`이 O(1)이다.

2. N과 M 시리즈와 마찬가지의 원리로 백트래킹으로 풀이 가능하다. 순열을 구하는 방법 외의 풀이 방식은 1번과 동일하다. [[풀이 - solve.py](./solve.py)]

    - `divmod(i, 5)`를 활용하면 x, y 좌표를 더 쉽게 구할 수 있다.

    - `s_count + (7 - depth) < 4`인지 체크하여 애초에 이다솜파가 더 많을 수 없는 조합을 미리 버릴 수 있다. (가지치기)
        - `s_count + (7 - depth) < 4`를 매번 계산하기 때문에 가지치기 한다고해서 무조건 성능이 좋아지는 것은 아니다. (실제로 이 문제에서는 시간이 더 걸렸다...)
