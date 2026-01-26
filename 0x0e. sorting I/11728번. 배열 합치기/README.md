# 11728번. 배열 합치기

## 문제
https://www.acmicpc.net/problem/11728

---

## Key Points

1. [머지 소트](../merge_sort.py) 구현을 위한 배열 합치기 코드이다.

    - a와 b를 정렬한 후, 각각 인덱스를 0부터 시작하여 작은 값을 c에 넣어주면 된다.

    - 둘 중에 하나의 인덱스라도 끝에 도달하면 멈추고, 남은 값을 모두 c에 넣어준다. (`a_i`, `b_i` 중 하나는 끝에 도달했기 때문에, 실제로는 하나의 배열에서만 값이 들어간다.)

2. 사실 python에서는 내장 함수를 쓰는 것이 가장 효율적이다.

    ```python
    def solve(a: list[int], b: list[int]) -> list[int]:
        return sorted(a + b)
    ```
