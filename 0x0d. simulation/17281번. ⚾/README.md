# 17281번. ⚾

## 문제
https://www.acmicpc.net/problem/17281

---

## Key Points

1. 이 문제는 아래와 같이 나눠 생각할 수 있다.

    - 모든 타순 조합 구하기 (`itertools.permutations`)
        - 1번 선수는 무조건 4번 타자임에 유의해야한다. (8!)

    - 각 타순 조합으로 획득 점수 구하여 최대값 구하기

2. 풀이 아이디어는 단순한데, 제한 시간이 팍팍한 문제였다.

    - 원래는 각 이닝 별 점수 획득을 아래와 같이 deque을 사용하여 구현하였다.

        ```python
        from collections import deque

        def play(inning: list[int], order: tuple[int, ...], batter_idx: int) -> tuple[int, int]:
            inning_score = 0
            out_count = 0
            runners = deque([0, 0 ,0])
            while out_count < 3:
                res = inning[order[batter_idx]]
                if res == 0:
                    out_count += 1
                else:
                    runners.appendleft(1)
                    for _ in range(res):
                        inning_score += runners.pop()
                    for _ in range(res - 1):
                        runners.appendleft(0)
                batter_idx = (batter_idx + 1) % 9

            return batter_idx, inning_score
        ```

    - 하지만 위 방식은 시간 초과가 발생했다. 비트마스킹 방식으로 바꿔도 시간 초과가 발생했다.

    - 여러 시행착오 끝에 현재 [풀이 코드](./solve.py)와 같이 하드코딩 비슷하게 코딩하니 통과하였다.
        - `deque`을 사용하여 구현한 코드는 홈런 한 방에 8번의 append/pop 호출이 있다.
        - `deque`을 쓰지 않고, 풀이 코드와 같이 각 안타/홈런에 대해 하나 하나 결과를 구현해주면 비용을 아낄 수 있다.
        - 이미 8! * 50 * 27 번 = 약 5천만 번의 반복문을 돌기 때문에 이런 사소한 차이가 성공/실패를 결정 지을 수 있다.

    - 제한 시간이 빡셀 때는, (나름) 세련된 코드보다는 단순하고 우직한 코드가 더 유리하다는 것을 알 수 있었다. (JIT가 최적화하기 쉽다.)

    - PyPy3로 제출해야한다. Python3로는 제한 시간 안에 풀기 어렵다.
