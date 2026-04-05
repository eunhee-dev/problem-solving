# 13300번. 방 배정

## 문제
https://www.acmicpc.net/problem/13300

---

## Key Points

1. `student_cnts` 배열을 만들어서 잘 세어주면 된다. (방 개수는 올림하기)

2. collections의 `Counter`나 `defaultdict`를 사용하면 더 멋지게 코딩 가능하다.

    - `Counter` 활용 

        ```python
        from collections import Counter

        def solve(k: int, students_info: list[tuple[int, int]]) -> int:
            student_cnts = Counter(students_info)
            return sum(math.ceil(cnt / k) for cnt in student_cnts.values())
        ```
    
    - `defaultdict` 활용

        ```python
        from collections import defaultdict

        def solve(k: int, students_info: list[tuple[int, int]]) -> int:
            student_cnts = defaultdict(int)
            for s, y in students_info:
                student_cnts[(s, y)] += 1
            return sum(math.ceil(cnt / k) for cnt in student_cnts.values())
        ```
