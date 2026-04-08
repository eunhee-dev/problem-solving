import sys

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    numbers = [int(sys_input()) for _ in range(5)]
    numbers.sort()
    
    mean = sum(numbers)//5
    median = numbers[2]

    return [mean, median]


def main():
    print(*solve(), sep="\n")


if __name__ == "__main__":
    main()