import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    year = int(sys_input())
    is_leap_year = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        is_leap_year = True
    
    print(int(is_leap_year))

def main():
    solve()

if __name__ == "__main__":
    main()
