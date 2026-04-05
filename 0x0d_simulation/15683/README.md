# 15683번. 감시

## 문제
https://www.acmicpc.net/problem/15683

---

## Key Points

1. 이 문제는 아래 단계로 나누어 생각하면 좋다.

    - (1) 각 cctv의 방향 정하기
        - 각 cctv 방향의 모든 조합을 구하는 법 생각하기

    - (2) (1)에서 정한 cctv 방향 조합의 사각지대 구하기
        - cctv가 볼 수 있는 구역 `board`에 `#`으로 마킹하기
        - 사각지대 개수 세기 (=`board`에서 `0` 개수 세기)

2. 1.(1)의 모든 조합을 구하는 방법으로 백트래킹을 활용, 생각나는대로 구현하였다. [[풀이 - solve_draft.py](./solve_draft.py)]

    - cctv가 최대 8개 있을 수 있고, cctv는 최대 4가지 방향이 있어서 4^8 으로 모든 경우의 수를 확인해볼 수 있다.

    - 백트래킹을 통해 각각의 cctv 방향의 조합을 모두 탐색 가능

    - 기존 `board`를 유지해야 하기 때문에, 마킹할 때는 `copy.deepcopy()`를 활용하여 `board`를 복사하여 마킹

    - 상하좌우에 대해 마킹을 각각 함수로 구현

    - `count_blind_spots()` 함수를 통해 `0`의 개수를 세어서 최소 사각지대 개수 구하기

    - 5번 cctv의 경우 경우의 수가 고정되어 있기 때문에, 미리 마킹해두고 시작하면 효율적

3. 위의 초안에서 중복되거나 비효율적인 부분을 정리하였다. [[풀이 - solve.py](./solve.py)]

    - 상하좌우에 대해 각각의 함수가 있는 것이 비효율적이라고 생각함
        - 각 CCTV 번호에 대한 방향 조합(`dir_comb`)을 미리 정의 (`CCTV_MODE`)
        - `mark()` 함수에서 `dir_comb`를 인자로 받아 하나의 함수로 처리 가능하도록 통합

    - 마킹할 때 매번 `copy.deepcopy()`를 하는 것이 비효율적인 것 같음
        - 마킹할 때 변경한 좌표를 기록해두고, `unmark()` 함수를 구현하여 변경한 좌표를 원상 복구

4. 백트래킹이 아닌 진법을 활용하여 재귀 없이 문제를 풀 수도 있다. [[풀이 - solve_digit.py](./solve_digit.py)]

    - cctv 개수가 3개라면, 132(4) 와 같이 4진법을 통해 각 cctv에 대해 최대 4가지 방향의 경우의 수를 정의할 수 있음
      - 첫번째 cctv `dir_comb` : 1, 두번째 cctv `dir_comb` : 3, 세번째 cctv `dir_comb` : 2
      - 000 ~ 333으로 모든 경우의 수 표현 가능

    - 2번, 5번 cctv를 제외하고는 방향이 4가지이므로 4진법 활용
        - 5번 cctv의 경우 방향이 1가지이므로 백트래킹과 마찬가지로 미리 마킹하고 시작
        - 2번 cctv는 `cctv %= 2`를 통해 0이나 1의 결과가 나오도록 하였음
            - 사실 각 cctv의 경우의 수에 따라 유연하게 진법을 구성할 수 있지만,
            - 이 문제에서는 2번 cctv만 예외라서 조금 비효율적이더라도 간결함을 위해 4진법으로 통일하였음

    - 같은 원리로 `itertools.product()`도 활용할 수 있을 것 같다. [[풀이 - solve_itertools.py](./solve_itertools.py)]
        ```python
        from itertools import product

        # ...
        def solve(n, m, board):
            # ...
            mode_lists = [CCTV_MODES[mode] for _, _, mode in cctv]
            for dir_comb in product(*mode_lists):
                modified = []
                for (x, y, _), dirs in zip(cctv, dir_comb):
                    modified.extend(mark(board, x, y, dirs))
                ans = min(ans, count_blind_spots(board))
                unmark(board, modified)
            return ans
        ```
