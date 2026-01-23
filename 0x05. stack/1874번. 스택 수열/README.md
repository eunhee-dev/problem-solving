# 1874번. 스택 수열

## 문제
https://www.acmicpc.net/problem/1874

---

## Key Points

1. monotonic stack을 활용하여 풀이 가능하다.

    - stack에 1부터 n까지 오름차순으로 push
    - 현재 체크하는 sequence의 값이 stack에 top에 있으면 그렇지 않을 때까지 pop
    - sequence가 끝까지 체크되지 않았으면 return "NO" 

2. 문제의 설명 순서대로, 1 ~ n 까지 수를 stack에 넣으면서 계산하는 방법이 직관적인 풀이이다.

    - 그러나 이 방법은 무조건 n번을 돌아야 하므로, 불가능한 경우("NO"를 return 하는 경우)를 미리 알 수 있는 경우에는 시간적 손해를 볼 수 있음

    ```python
    def solve_intuitive(n:int, sequence: list[int]) -> str:
        stack = []
        ops = []
        curr_seq_idx = 0

        for i in range(1, n + 1):
            stack.append(i)
            ops.append("+")
            while stack and stack[-1] == sequence[curr_seq_idx]:
                stack.pop()
                ops.append("-")
                curr_seq_idx += 1

        if curr_seq_idx != len(sequence):
            return "NO"

        return "\n".join(ops)
    ```

    - 더 효율적으로 짜려면, [solve.py](./solve.py)와 같이 sequence를 기준으로 돌면 불가능한 경우를 바로 체크하여 NO를 return 할 수 있음

        - 체크할 sequence의 값이 나올 때까지 stack에 1부터 차례대로 push
        - 체크할 sequence의 값을 stack top과 비교
            - 다르면 return "NO"
            - 같으면 stack에서 해당 값 pop

3. 2번 항목의 경우 deque를 사용하면 더욱 pythonic한 코드를 작성할 수 있다.

    - deque.popleft()의 호출 오버헤드 때문에 시간은 solve_intuitive()에 비해 약간의 손해를 볼 수 있음

    - 그럼에도 불구하고, 가독성이 더 좋은 pythonic한 코드임

    ```python
    from collections import deque

    def solve_deque(n:int, sequence: list[int]) -> str:
        stack = []
        result = []
        sequence = deque(sequence)

        for i in range(1, n + 1):
            stack.append(i)
            result.append('+')
            while stack and stack[-1] == sequence[0]:
                stack.pop()
                sequence.popleft()
                result.append('-')

        if sequence:
            return "NO"

        return '\n'.join(result)
    ```
