# 11559번. Puyo Puyo

## 문제
https://www.acmicpc.net/problem/11559

---

## Key Points

1. 이 문제도 아래와 같이 두 단계로 나누어 생각하면 좋다.  [[풀이 - solve.py](./solve.py)]

    - 이번 턴에 폭발할 뿌요들(4개가 인접한 뿌요) 찾기 

    - 찾은 뿌요들을 폭발시키고 중력을 구현하여 board 재구성하기

2. 인접한 뿌요를 찾는 것은 bfs를 사용하면 쉽게 구현 가능하다. (`check_adjacent_bfs()`)

    - 여기서 포인트는 하나의 턴에서 `visited` 배열을 공유하는 것이다.
        - 이미 방문한 좌표는 같은 턴에서 방문하지 않기 때문에, O(r * c) 가능
        - 대충 생각하면, 2중 for문에 bfs()를 돌리니 O(r^2 * c^2) 처럼 보이지만,
        - 실제로 방문하는 좌표들을 생각해보면 `board`를 한 번만 순회한다.

3. 찾은 뿌요들을 폭발시키는 것은 아래와 같은 방법으로 구현 가능하다.

    - 찾은 뿌요 위에 칸부터 한 칸씩 내리고, 제일 위에 칸을 `.`으로 채운다. (O(r^2 * c))

        ```python
        def explode(board, explode_candidates):
            for x, y in explode_candidates:
                while x >= 0:
                    board[x][y] = board[x-1][y]
                    x -= 1
                board[0][y] = "."
        ```

    - 위 방식이 조금 비효율적인 것 같으면, 풀이 코드와 같이 O(r * c)에 구현 가능하다.
        - 각 열에 대해 터트릴 뿌요들 `.`으로 바꾸고, 남은 뿌요들을 `.`으로 초기화된 열에 아래에서 부터 차례대로 채워주는 방식

        ```python
        def explode(board, explode_candidates):
            for x, y in explode_candidates:
                board[x][y] = "."

            for y in range(6):
                puyo_in_col = []
                for x in range(12):
                    if board[x][y] != ".":
                        puyo_in_col.append(board[x][y])
                        board[x][y] = "."
                for x, puyo in enumerate(reversed(puyo_in_col)):
                    board[11-x][y] = puyo
        ```

4. 시간복잡도를 계산해보면, 한 턴에 O(r * c)가 소요되고(탐색 / 폭발), 턴은 최대 O(r * c) / 4 만큼 발생할 수 있으므로 O(r^2 * c^2)이 소요되어, 13^2 * 6^2로 제한시간 내 충분히 통과 가능하다.
