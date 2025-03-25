import sys
my_list = list(map(int, sys.stdin.readline().split()))

for m in sorted(my_list):
    print(m, end=' ')