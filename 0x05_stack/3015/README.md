# 3015번. 오아시스 재결합

## 문제
https://www.acmicpc.net/problem/3015

---

## Key Points

1. 자신보다 [오큰수](../17298/)까지 볼 수 있다.

2. 키가 같은 경우를 처리해주기 위해 stack에 count를 같이 저장한다. (height, count)
    - height를 하나로 압축해서 넣는 효과 (중복 문제 해결)
    - 오큰수 문제와 같아짐
