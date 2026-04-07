import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    numbers = [int(sys_input()) for _ in range(7)]
    odds = [n for n in numbers if n % 2 == 1]

    if not odds:
        return [-1]
    return [sum(odds), min(odds)]

def main():
    print(*solve(), sep="\n")

if __name__ == "__main__":
    main()
