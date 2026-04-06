import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    numbers = [item for item in map(int, sys_input().split())]
    numbers.sort()
    print(*numbers)
    
def main():
    solve()

if __name__ == "__main__":
    main()
