# 16933번. 벽 부수고 이동하기 3

## 문제
https://www.acmicpc.net/problem/16933

---

## Key Points

1. 문제 풀이 순서: [solve_4d_fail.py](./solve_4d_fail.py) => [solve_3d.py](./solve_3d.py.py) => [solve.py](./solve.py)

2. 가장 직관적인 풀이는 이전 [2206번. 벽 부수고 이동하기](../2206/) 문제에서 `broken_cnt`에 대해 차원을 추가하여 상태를 관리한 것 처럼, day/night 여부에 대해서도 차원을 추가하여 4차원 배열로 해결하는 것임. ([solve_4d_fail.py](./solve_4d_fail.py))

    - 근데 4차원 배열이라 그런지, PyPy3 에서도 시간초과 발생... 이런 문제는 C++로 푸는게 정신 건강에 좋을 듯 하다.

    - 그럼에도 불구하고 Python으로 최적화하여 풀 수 있는 방법을 찾아보자

3. 약간의 꼼수를 써서 day/night 상태를 관리하지 않고도 3차원 배열로 풀 수 있게 해보자 ([solve_3d.py](./solve_3d.py))

    - `distance % 2 == 1`이면 day 이고, `0` 이면 night 임을 활용

    - 대신 day/night일 때 이미 방문했는지를 확인할 수 없어서 queue에 같은 값이 중복되어 들어갈 수 있음 (필터링되긴 하지만 살짝 비효율적)

    - 굉장히 아슬아슬하게 통과했음... 더 최적화 하면 좋을듯
        - `board`를 `list[str]` 그대로 받기 + `range(len(queue))` 따로 계산 조합 => 시간 초과
        - `board`를 `list[str]` 그대로 받기 + `len_queue = len(queue)` 따로 계산 조합 => 통과
        - `board`를 `list[list[int]]`로 변환하기 + `range(len(queue))` 조합 => 통과
        - `board`를 `list[list[int]]`로 변환하기 + `len_queue = len(queue)` 조합 => 시간 초과

4. [14442번. 벽 부수고 이동하기 2](../14442/)의 [solve_2d.py](../14442/solve_2d.py) 풀이를 활용하여 2차원 배열로 풀 수 있다. ([solve.py](./solve.py))

    - `visited` 배열에 벽을 부순 최소 횟수를 기록
        - 14442번 문제와 다르게, 밤에 벽을 만날 경우 현재 좌표를 큐에 그대로 넣는 경우가 생김
        - 이로 인해 순서가 꼬일 수 있어서, 이를 관리하기 위해 queue에는 x, y 뿐만 아니라 `broken_cnt`도 들어가야함

    - 3d-bfs 방법에서의 `distance % 2`를 통한 낮/밤 상태 확인 방법 활용

    - 3d-bfs에 비해 상대적으로 여유롭게 통과 (벽을 부순 최소 횟수가 아니면 큐에 넣지 않기 때문에 더 효율적)

5. 많이 까다로운 문제였다.
