import sys
from itertools import combinations

def sys_input():
    return sys.stdin.readline().rstrip()

def solve():
    dwarfs = [int(sys_input()) for _ in range(9)]
    dwarfs_comb = [comb for comb in combinations(dwarfs, 7) if sum(comb) == 100]
    answer = sorted(dwarfs_comb.pop())
    return answer

def main():
    print(*solve(), sep="\n")

if __name__ == "__main__":
    main()
