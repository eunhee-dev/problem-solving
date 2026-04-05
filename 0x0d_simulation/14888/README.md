# 14888번. 연산자 끼워넣기

## 문제
https://www.acmicpc.net/problem/14888

---

## Key Points

1. 이 문제는 다음 단계로 나누어 생각해 볼 수 있다.

    - 연산자 순열 구하기

    - 연산자 순열에 맞게 계산하기

2. 연산자 조합을 구하는 법은 `itertools.permutations`를 쓰면 간단하다. [[풀이 - solve.py](./solve.py)]

    - N-1이 10 이하이기 때문에 10! = 3,628,800로 모든 순열을 고려해도 충분하다.

    - set을 활용해 중복되는 순열을 제거한 후 계산할 수 있다.
        - 다항계수 공식에 의해 조합 수를 10! / add! * sub! * mul! * div! 으로 줄여 효율성 증가

    - 연산자를 "+"와 같은 문자열이 아닌 함수 자체를 순열로 넣어서 구현하면 더 멋진 구현도 가능하다.

        ```python
        import operator
        
        #...
        def solve(sequence: list[int], ops: tuple[int, int, int, int]) -> tuple[int, int]:
            max_val = float("-inf")
            min_val = float("inf")

            op_list = [operator.add] * ops[0] + [operator.sub] * ops[1] + [operator.mul] * ops[2] + [cpp14_division] * ops[3]

            for op_combs in set(permutations(op_list)):
                curr_val = sequence[0]
                for i, op in enumerate(op_combs):
                    curr_val = op(curr_val, sequence[i+1])

                max_val = max(max_val, curr_val)
                min_val = min(min_val, curr_val)

            return max_val, min_val
        ```

3. C++14 기준 나눗셈은 `cpp14_division()`로 문제 요구대로 구현하였다.

    - 음수일 때 소수점을 버리는거라 단순하게 `int(a / b)`로 구현해도 된다.

4. N이 2만 커져도 순수 permutations이 12!이 되어 시간이 초과될 수 있다. 백트래킹을 쓰면 다항계수 만큼만 고려해주면 된다. [[풀이 - solve_backtracking.py](./solve_backtracking.py)]

    - 예를들어 N=13일 때, 12! = 479,001,600으로 4억개의 순열을 만들고 중복을 제거해줘야 하는데,

    - 백트래킹은 중복을 제거한 조합만큼만 시행하면 된다. 12! / (3! * 4) = 19,958,400으로 더 여유롭다.

    - 실제로 백준 실행 시간도 백트래킹 버전이 더 짧게 나왔다. (itertools: 400ms, 백트래킹:  50ms)
