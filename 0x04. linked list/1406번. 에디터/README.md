# 1406번. 에디터

## 문제
https://www.acmicpc.net/problem/1406

---

## Key Points

1. linked list로 풀면 좋지만, 에디터가 한 칸만 이동하기 때문에 double stack을 쓰면 꽤 효율적으로 풀 수 있다.

2. 입력이 상당히 길기 때문에 (n <= 100,000, m <= 500,000), 내장 함수인 `input()`을 쓰면 시간 초과가 난다.

    - 버퍼를 활용하는 `sys.stdin.readline()`을 사용하여 input을 받으면 된다.
    
        - 대량의 데이터를 처리할 때 유용

        - 자동으로 문자열의 양끝 공백을 제거하지 않으므로, 필요 시 .rstrip()을 통해 개행문자를 떼어내어야 한다.

    - 앞으로 백준 문제를 풀 때, 아래와 같이 `sys_input()` 함수를 정의해서 입력을 받기로 결정하였다.

        ```python
        import sys

        def sys_input() -> str:
            return sys.stdin.readline().rstrip()

        
        def main() -> None:
            n = int(sys_input())
            
            answer: str = solve(n)
            print(answer)
        ```

3. 보통은 `main()`에서 모든 입력을 처리했는데, 이 문제는 특성상 m 크기의 명령어 배열을 들고 있는 것이 비효율적인 것 같아, `solve()`에서 명령어를 입력 받고 바로바로 처리하는 방식으로 구현하였다. 
