import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    score = int(sys_input())
    if score >= 90:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 60 and score <= 69:
        return "D"
    else:
        return "F"

def main():
    print(solve())

if __name__ == "__main__":
    main()
