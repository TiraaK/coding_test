n, x = map(int, input().split())
A = list(map(int, input().split()))
ans = []

for i in A:
    if i < x:
        ans.append(str(i))

print(" ".join(ans))