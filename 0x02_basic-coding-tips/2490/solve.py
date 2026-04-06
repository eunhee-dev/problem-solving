import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve(yuts):
    return ["DCBAE"[sum(yut)] for yut in yuts]

def main():
    yuts = [list(map(int, sys_input().split())) for _ in range(3)]
    answer = solve(yuts)
    print(*answer, sep="\n")

if __name__ == "__main__":
    main()
