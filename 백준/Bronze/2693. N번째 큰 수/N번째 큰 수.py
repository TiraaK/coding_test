my_arr = []
N = int(input())
for _ in range(N):
    temp = list(map(int, input().split()))
    my_arr.append(temp)
for i in range(N):
    print(sorted(my_arr[i])[-3])