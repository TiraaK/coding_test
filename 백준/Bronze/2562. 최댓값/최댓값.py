max = 0
max_pos = 0
for i in range(1, 10):
    cur = int(input())
    if max < cur:
        max_pos = i
        max = cur      
print(max)
print(max_pos)