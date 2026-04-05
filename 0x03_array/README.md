# 0x03. 배열

## 개요

- 배열은 가장 기본적인 자료구조로, 연속된 메모리 공간에 같은 타입의 데이터를 저장한다.

- Python에서는 `list`가 배열 역할을 하며, 동적 크기 조절이 가능하다.

- 인덱스를 통한 접근이 O(1)이므로, 빈도수 카운팅 등에 유용하다.


## 문제 풀이 현황

| 분류 | 번호 | 문제 | 풀이 |
|------|------|------|------|
| 연습 문제 | 10808 | [알파벳 개수](https://www.acmicpc.net/problem/10808) | [코드](./10808/) |
| 기본 문제✔ | 2577 | [숫자의 개수](https://www.acmicpc.net/problem/2577) | [코드](./2577/) |
| 기본 문제✔ | 1475 | [방 번호](https://www.acmicpc.net/problem/1475) | [코드](./1475/) |
| 기본 문제✔ | 3273 | [두 수의 합](https://www.acmicpc.net/problem/3273) | [코드](./3273/) |
| 기본 문제 | 10807 | [개수 세기](https://www.acmicpc.net/problem/10807) | [코드](./10807/) |
| 기본 문제 | 13300 | [방 배정](https://www.acmicpc.net/problem/13300) | [코드](./13300/) |
| 기본 문제 | 11328 | [Strfry](https://www.acmicpc.net/problem/11328) | [코드](./11328/) |
| 기본 문제 | 1919 | [애너그램 만들기](https://www.acmicpc.net/problem/1919) | [코드](./1919/) |

<details>
<summary>힌트 보기</summary>

- 10808: 빈도수 배열
- 2577: 빈도수 배열
- 1475: 6, 9 처리
- 3273: set 또는 투포인터
- 11328: Counter 활용
- 1919: Counter 활용
</details>


## 핵심 포인트

<details>
<summary>펼쳐 보기 (문제 풀이 스포일러 포함)</summary>

- **빈도수 카운팅**: 알파벳이나 숫자의 개수를 셀 때는 크기가 고정된 배열을 사용한다.
    ```python
    count = [0] * 26  # 알파벳 개수
    for c in s:
        count[ord(c) - ord('a')] += 1
    ```

- **Counter 활용**: `collections.Counter`를 사용하면 더 깔끔하게 빈도수를 셀 수 있다.
    ```python
    from collections import Counter
    Counter(s1) == Counter(s2)  # 애너그램 판별
    ```

</details>
