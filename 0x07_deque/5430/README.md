# 5430번. AC

## 문제
https://www.acmicpc.net/problem/5430

---

## Key Points

1. list를 매번 뒤집는 것은 비효율적이니 reversed_flag를 설정하면 효율적이다.

    - reversed_flag가 True이면 뒤에서 pop()을 하면 같은 효과를 얻음

    - 마지막에 출력할 때만 뒤집어주면 됨

2. error_flag를 통해 error를 출력해야 할 경우를 핸들링 해준다.

3. "".split(",") 는 []가 아닌 [""]이다.

    - 테스트케이스와 같이 빈 배열 문자열("[]")이 input으로 들어오는 경우를 신경써주어야 함

    - eval()을 쓰면 편하지만... 안쓰는 것을 권장...
