import sys
s = list(sys.stdin.readline().strip())

v_list = [0 for _ in range(26)]
k_list = [chr(i) for i in range(65+32, 65+32+26)]


map_dict = dict(zip(k_list, v_list))

for ch in s:
    if ch in map_dict:
        map_dict[ch] += 1

for ans in map_dict.values():
    print(ans, end=' ')
