# 1780번. 종이의 개수

## 문제
https://www.acmicpc.net/problem/1780

---

## Key Points

1. 문제에서 제시하는 순서대로 코드를 구현하면 된다.

    - 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다. (`check_equal(board)`)
  
    - (1)이 아닌 경우에는 종이를 같은 크기의 종이 9개로 자르고(`divide(n, board)`), 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다. (`solve(n // 3, sub_board)`)

2. `Counter` 대신 `defaultdict`나 `list`를 사용해도 된다.

    ```python
    from collections import defaultdict

    def solve(n: int, board: list[list[str]], count: defaultdict[str, int]) -> defaultdict[str, int]:
    check_res = check_equal(board)
    if check_res == "Not Equal":
        for new_board in divide(n, board):
            solve(n // 3, new_board, count)
    else:
        count[check_res] += 1
    return count

    answer: defaultdict[str, int] = solve(n, board, defaultdict(int))
    ```
