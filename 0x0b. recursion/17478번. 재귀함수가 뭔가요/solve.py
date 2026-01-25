""" solve.py for 17478번. 재귀함수가 뭔가요? """

import sys


def sys_input():
    return sys.stdin.readline().rstrip()


def chat_recursive(n: int, depth: int) -> list[str]:
    prefix = "____" * depth
    chat_res = [prefix + "\"재귀함수가 뭔가요?\""]
    if depth == n:
        chat_res.append(prefix + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
    else:
        chat_res.append(prefix + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
        chat_res.append(prefix + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        chat_res.append(prefix + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
        chat_res.extend(chat_recursive(n, depth+1))
    chat_res.append(prefix + "라고 답변하였지.")
    return chat_res


def solve(n: int) -> str:
    chat_res = ["어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다."]
    chat_res.extend(chat_recursive(n, 0))
    return "\n".join(chat_res)


def main() -> None:
    n = int(sys_input())

    answer: str = solve(n)
    print(answer)


if __name__ == "__main__":
    main()
