import sys


def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    a, b = map(int, sys_input().split())
    return a+b, a-b, a*b, a//b, a%b

def main():
    answer = solve()
    print(*answer, sep="\n")

if __name__ == "__main__":
    main()
