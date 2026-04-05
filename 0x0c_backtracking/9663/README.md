# 9663번. N-Queen

## 문제
https://www.acmicpc.net/problem/9663

---

## Key Points

1. 중복 방문을 체크하는 `is_used` 배열을 퀸이 움직일 수 있는 [열(column), ↙ 대각선, ↘ 대각선] 3개에 대해 체크할 수 있도록 각각 만들어줘야 함

    - 행(row)을 기준으로 하나씩 놓기 때문에, 행은 체크해줄 필요 없음
    - 열(column) 체크: `is_used_col[col_idx]`
    - ↙ 대각선 체크: `is_used_diag1[row_idx + col_idx]`
    - ↘ 대각선 체크: `is_used_diag2[row_idx - col_idx + (n - 1)]`

2. 그 외에 것은 백트래킹 기본 문제들과 동일하다.

3. `count`를 `solve()` 함수에서 선언하고, `backtrack()` 내부에서 `nonlocal count`로 외부 함수의 변수를 갱신해도 된다.

    - side-effect로 함수 밖의 변수를 갱신하는 방법 (`backtrack()` 함수의 반환 값이 없어도 됨)

    - [15649번. N과 M (1)](../15649/) 문제와 비슷한 구조를 갖출 수 있음 (`sequences` 에 직접 수열 append)

    ```python
    def solve(n: int) -> int:
        count = 0
        # ...

        def backtrack(row_idx: int) -> None:
            nonlocal count
            if row_idx == n:
                count += 1
                return
            # ...
            backtrack(row_idx + 1)
            # ...
        
        backtrack(0)
        return count
    ```
