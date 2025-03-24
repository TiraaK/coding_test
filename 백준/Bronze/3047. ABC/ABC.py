orig_list = list(map(int, input().split()))
sort_list = sorted(orig_list)
target_list = list(input())

my_dict = dict(zip(['A', 'B', 'C'], sort_list))

for i in range(len(target_list)):
    print(my_dict[target_list[i]], end=' ')