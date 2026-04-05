# 바킹독 실전 알고리즘 강좌 - Python 풀이 🐍

## 📂 폴더 구조

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

## 🎯 구조화된 풀이를 위한 전략

모든 풀이는 이런 구조를 따릅니다:

```python

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
