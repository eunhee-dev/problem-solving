# 0x02. 기초 코드 작성 요령

## 개요

- 알고리즘 문제 풀이의 기본이 되는 입출력 처리, 반복문, 조건문 등을 다룬다.

- Python에서는 `sys.stdin.readline()`을 사용하면 `input()`보다 빠르게 입력을 받을 수 있다.

- 출력이 많을 경우 `print()`를 반복 호출하는 것보다 문자열을 모아서 한 번에 출력하는 것이 효율적이다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 10871 | [X보다 작은 수](https://www.acmicpc.net/problem/10871) | [코드](./10871번.%20X보다%20작은%20수/) |
| 기본 문제✔ | 1000 | [A+B](https://www.acmicpc.net/problem/1000) | [코드](./1000번.%20A+B/) |
| 기본 문제✔ | 2557 | [Hello World](https://www.acmicpc.net/problem/2557) | [코드](./2557번.%20Hello%20World/) |
| 기본 문제✔ | 10171 | [고양이](https://www.acmicpc.net/problem/10171) | [코드](./10171번.%20고양이/) |
| 기본 문제✔ | 10869 | [사칙연산](https://www.acmicpc.net/problem/10869) | [코드](./10869번.%20사칙연산/) |
| 기본 문제✔ | 9498 | [시험 성적](https://www.acmicpc.net/problem/9498) | [코드](./9498번.%20시험%20성적/) |
| 기본 문제✔ | 2752 | [세수정렬](https://www.acmicpc.net/problem/2752) | - |
| 기본 문제✔ | 2753 | [윤년](https://www.acmicpc.net/problem/2753) | - |
| 기본 문제✔ | 2480 | [주사위 세개](https://www.acmicpc.net/problem/2480) | - |
| 기본 문제✔ | 2490 | [윷놀이](https://www.acmicpc.net/problem/2490) | - |
| 기본 문제✔ | 2576 | [홀수](https://www.acmicpc.net/problem/2576) | - |
| 기본 문제✔ | 2587 | [대표값2](https://www.acmicpc.net/problem/2587) | - |
| 기본 문제✔ | 2309 | [일곱 난쟁이](https://www.acmicpc.net/problem/2309) | - |
| 기본 문제✔ | 10093 | [숫자](https://www.acmicpc.net/problem/10093) | - |
| 기본 문제✔ | 1267 | [핸드폰 요금](https://www.acmicpc.net/problem/1267) | - |
| 기본 문제✔ | 10804 | [카드 역배치](https://www.acmicpc.net/problem/10804) | - |
| 기본 문제✔ | 15552 | [빠른 A+B](https://www.acmicpc.net/problem/15552) | - |
| 기본 문제✔ | 2438 | [별 찍기 - 1](https://www.acmicpc.net/problem/2438) | - |
| 기본 문제✔ | 2439 | [별 찍기 - 2](https://www.acmicpc.net/problem/2439) | - |
| 기본 문제✔ | 2440 | [별 찍기 - 3](https://www.acmicpc.net/problem/2440) | - |
| 기본 문제✔ | 2441 | [별 찍기 - 4](https://www.acmicpc.net/problem/2441) | - |
| 기본 문제✔ | 2442 | [별 찍기 - 5](https://www.acmicpc.net/problem/2442) | - |
| 기본 문제✔ | 2443 | [별 찍기 - 6](https://www.acmicpc.net/problem/2443) | - |
| 기본 문제✔ | 2444 | [별 찍기 - 7](https://www.acmicpc.net/problem/2444) | - |
| 기본 문제✔ | 2445 | [별 찍기 - 8](https://www.acmicpc.net/problem/2445) | - |
| 기본 문제✔ | 2446 | [별 찍기 - 9](https://www.acmicpc.net/problem/2446) | - |
| 기본 문제✔ | 2562 | [최댓값](https://www.acmicpc.net/problem/2562) | - |


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **입출력 패턴**: `sys.stdin.readline().rstrip()`으로 입력받고, `main()`에서 `solve()` 결과를 출력하는 구조를 권장한다.

- **List comprehension**: 조건에 맞는 요소를 필터링할 때 유용하다.
    ```python
    answer = [num for num in a if num < x]
    print(*answer)  # 언패킹으로 공백 구분 출력
    ```

- **Python 특성**: 리스트 크기를 동적으로 할당하므로 C++처럼 n을 미리 알 필요가 없는 경우가 많다.

</details>
