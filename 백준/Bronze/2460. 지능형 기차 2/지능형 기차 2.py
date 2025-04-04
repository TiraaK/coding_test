num, max_n = 0, 0
for _ in range(10):
    a, b = map(int, input().split())
    num -= a
    num += b
    max_n = max(num, max_n)

print(max_n)