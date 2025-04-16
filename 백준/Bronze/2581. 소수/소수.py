M = int(input())
N = int(input())
ans = []
def primenumber(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0 : 
            return False
    return True

for target in range(M,N+1):
    if primenumber(target) is True:
        ans.append(target)
        
if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])