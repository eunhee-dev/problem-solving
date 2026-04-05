# 바킹독 실전 알고리즘 강좌 - Python 풀이 🐍

[바킹독의 실전 알고리즘 강좌](https://blog.encrypted.gg/category/강좌/실전%20알고리즘)와 [워크북](https://github.com/encrypted-def/basic-algo-lecture/blob/master/workbook.md) 문제들을 Python으로 풀이한 저장소입니다.

원본 워크북에는 C++ 풀이만 있어서, Python으로 코딩테스트를 준비하시는 분들을 위해 Python 버전을 작성했습니다. 강좌를 따라가면서 참고하시면 좋을 것 같습니다!!


## 목차

- [풀이 활용법](#풀이-활용법)
- [Python 코딩 스타일에 관하여](#python-코딩-스타일에-관하여)
- [코드 구조](#코드-구조)
- [폴더 구조](#폴더-구조)
- [진행 상황](#진행-상황)
- [권장 자료 및 도구](#권장-자료-및-도구)
- [참고 사항](#참고-사항)

## 풀이 활용법

1. **먼저 직접 풀어보세요.** 답을 바로 보면 실력이 늘지 않습니다. 최소 30분~1시간은 고민해보시는 걸 추천드립니다.
2. **막히면 힌트로 활용하세요.** 코드 전체를 보기보다는, 어떤 자료구조나 알고리즘을 썼는지만 확인하고 다시 도전해보세요.
3. **풀고 나서 비교해보세요.** 본인 풀이와 비교하면서 "이런 방식도 있구나" 하고 참고하시면 됩니다.
4. **나만의 규칙을 만들어보세요.** Python 코딩 규칙을 지키면서 본인만의 코딩 스타일을 정해보세요. 예를 들어 입력 함수는 항상 이렇게 쓴다, BFS는 이런 구조로 짠다 등등. 규칙이 있으면 매번 고민할 필요 없이 문제 풀이에 집중할 수 있고, 실수도 줄어듭니다.


## Python 코딩 스타일에 관하여

Python에는 나름의 코딩 규칙들이 있습니다. 코딩테스트나 PS에서 코딩할 때 "일단 돌아가면 장땡이지!"라고 생각하고 대충 코딩하기 쉬운데, 저는 이런 규칙들을 지키면서 짜는 편입니다.

실제 개발도 아닌데 조금 과하다고 느낄 수 있습니다. 하지만 코딩테스트에서도 시간이 촉박하다고 대충 짜면 오히려 디버깅에서 시간을 더 잡아먹습니다. 몇 분 전에 짠 코드도 돌아서면 까먹거든요. "이 변수가 뭐였지?", "이 함수 반환값이 뭐였더라?" 하면서 코드를 다시 읽는 시간이 쌓입니다.

타입 힌트 하나, 함수 분리 하나가 이런 실수를 줄여줍니다. 처음엔 조금 느린 것 같아도, 결국 제대로 돌아가는 코드를 짜는 게 가장 빠른 길입니다.

실무에서도 보면 코딩 잘하는 신입들도 이런 규칙 없이 본인 스타일대로 짜는 경우가 많습니다. 그러면 나중에 "이 함수 뭘 받는 거지?" 하고 코드를 뒤져보고 분석해야 합니다. 이러한 경험이 있는 면접관이 코드를 본다면, 깔끔하게 정리된 코드가 좋은 인상을 줄 수 있지 않을까요?

물론 알고리즘 효율이 우선인 경우엔 Pythonic하지 않은 방식이 나을 때도 있고, 상황에 따라 애매한 지점이 있습니다. 저도 완벽하지 않아서 일관성이 부족한 부분이 있을 수 있으니 참고용으로 봐주세요!!


### PEP8이란?

[PEP8](https://peps.python.org/pep-0008/)은 Python 공식 스타일 가이드입니다. 들여쓰기는 스페이스 4칸, 한 줄은 79자 이내, 함수명은 snake_case 등 이런 규칙들을 정해둔 문서입니다.

이게 왜 필요하냐면, 모두가 비슷한 스타일로 코드를 작성하면 다른 사람 코드를 읽기가 훨씬 편해지기 때문입니다. 협업할 때 특히 중요합니다.

물론 처음부터 이 모든 규칙을 외울 수는 없습니다. 그래서 VSCode 같은 IDE를 쓸 때 Pylint 같은 linter의 도움을 받으면 좋습니다. 코드를 짜면서 실시간으로 "여기 스타일이 잘못됐어요"라고 알려주거든요.


### Type Annotation이란?

함수의 인자와 반환값에 타입을 명시하는 것입니다.

```python
# Type Annotation X
def add(a, b):
    return a + b

# Type Annotation O
def add(a: int, b: int) -> int:
    return a + b
```

Python은 타입을 안 써도 돌아가지만, 써두면 "이 함수는 정수 두 개를 받아서 정수를 반환한다"는 의도가 명확해집니다. IDE 자동완성도 잘 되고, 실수도 미리 잡아줍니다.


### Pythonic code란?

Python에는 "The Zen of Python"이라는 철학이 있습니다. 터미널에서 `import this`를 입력하면 볼 수 있습니다. 핵심은 **가독성**, **간결함**, **명료함**입니다.

Pythonic한 코드란 Python의 특성을 잘 활용해서 간결하고 읽기 쉽게 작성한 코드를 말합니다. 몇 가지 예시를 보면:

```python
# 1. 반복문 - range(len()) 대신 enumerate 사용
# Bad
for i in range(len(numbers)):
    print(numbers[i])

# Good
for i, num in enumerate(numbers):
    print(i, num)

# 2. 리스트 생성 - for loop 대신 list comprehension
# Bad
squares = []
for i in range(10):
    squares.append(i * i)

# Good
squares = [i * i for i in range(10)]

# 3. 변수 교환 - temp 변수 대신 튜플 언패킹
# Bad
temp = a
a = b
b = temp

# Good
a, b = b, a
```

처음엔 어색할 수 있지만, 익숙해지면 코드가 훨씬 깔끔해집니다.


## 코드 구조

모든 풀이는 이런 구조를 따릅니다:

```python
""" solve.py for {문제번호}. {문제명} """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(...) -> ...:
    # 핵심 알고리즘 로직
    pass


def main() -> None:
    # 입력 처리
    # solve 호출
    # 출력 처리
    answer = solve(...)
    print(answer)


if __name__ == "__main__":
    main()
```

### 각 요소 설명

| 요소 | 역할 |
|------|------|
| `sys_input()` | `sys.stdin.readline().rstrip()` 래핑. 백준에서 `input()` 대신 쓰면 입력이 빨라집니다 |
| `solve()` | 순수한 알고리즘 로직만 담당. 입출력과 분리해서 테스트하기 좋습니다 |
| `main()` | 입력 파싱 → `solve()` 호출 → 결과 출력. 프로그램의 진입점입니다 |
| Type Annotation | 모든 함수에 타입 힌트를 답니다. 의도가 명확해지고 실수를 줄여줍니다 |

### 추가 규칙

- 복잡한 로직은 헬퍼 함수로 분리 (예: `bfs()`, `dfs()`)
- 출력이 개행으로 구분된 리스트면 `print(*answer, sep="\n")` 사용

## 폴더 구조

```
.
├── 0x02_basic-coding-tips/
├── 0x03_array/
├── 0x04_linked-list/
├── 0x05_stack/
├── 0x06_queue/
├── 0x07_deque/
├── 0x08_stack-bracket-matching/
├── 0x09_bfs/
├── 0x0b_recursion/
├── 0x0c_backtracking/
├── 0x0d_simulation/
├── 0x0e_sorting-I/
├── 0x0f_sorting-II/
├── 0x10_dynamic-programming/
├── 0x11_greedy/
└── README.md
```

**원본 강좌**: [바킹독의 실전 알고리즘](https://blog.encrypted.gg/category/강좌/실전%20알고리즘)  
**원본 워크북**: [basic-algo-lecture](https://github.com/encrypted-def/basic-algo-lecture/blob/master/workbook.md)
