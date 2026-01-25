# 12100번. 2048 (Easy)

## 문제
https://www.acmicpc.net/problem/12100

---

## Key Points

1. 이 문제도 아래 두 단계로 나누어 생각하면 좋다.

    - 게임판을 5번 기울이는 방향 조합 구하기

    - 게임판을 상하좌우로 기울이기

2. 게임판을 5번 기울이는 방향 조합 구하기의 경우 [백트래킹 파트](../../0x0c.%20backtracking/)에서 했던 것들을 그대로 활용하면 된다.

    - 백트래킹 활용 [[풀이 - solve.py](./solve.py)]

    - `itertools.product` 활용 [[풀이 - solve_itertools.py](./solve_itertools.py)]

3. 게임판을 상하좌우로 기울이는 것은 아래 과정대로 생각하면 좋다.

    - (1) 게임판을 왼쪽으로 기울이는 경우 (왼쪽부터 시작하는 리스트 구조 상 가장 자연스러운 방향)
        - `blocks` 리스트를 만들어서 0이 아닌 값을 append 해준다. (`blocks = [(block, is_merged) ...]`)
        - `blocks`에 값이 들어있고, blocks의 가장 최신 값이 현재 블록 값과 같고, 이번 턴에 머지된 블록이 아닌 경우 그 블록을 pop해서 더한 후 append 해준다.

            ```python
            blocks = []  # (block, is_merged)
            for block in row:
                if block != 0:
                    if blocks and blocks[-1][0] == block and not blocks[-1][1]:
                        blocks.append((blocks.pop()[0] + block, True))
                    else:
                        blocks.append((block, False))
            ```
        - `blocks`에 있는 값을 왼쪽부터 차례대로 `new_board`에 옮긴다.

    - (2) 게임판을 아래, 오른쪽, 위로 기울이는 경우
        - 약간의 꼼수를 떠올리면 좋은데, 아래로 기울이는 경우를 생각해보면 `board`를 시계방향으로 90도 회전하고 왼쪽으로 기울이는 것과 동일하다.
        - 마찬가지로 오른쪽은 180도, 위는 270도 `board`를 돌리고 왼쪽으로 기울이면 된다.
        - 현재 [풀이 코드](./solve.py)에서는 `board`를 기울이고 다시 회전시켜 원위치 시켰는데, 안해줘도 문제를 푸는데는 영향이 없다.
