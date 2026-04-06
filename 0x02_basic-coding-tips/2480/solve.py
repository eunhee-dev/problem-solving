import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    a, b, c  = map(int, sys_input().split())
    if a == b == c:
        return 10000 + a * 1000
    elif a in (b, c):
        return 1000 + a * 100
    elif b in (a, c):
        return 1000 + b * 100
    else:
        return max(a, b, c) * 100

def main():
    print(solve())

if __name__ == "__main__":
    main()
