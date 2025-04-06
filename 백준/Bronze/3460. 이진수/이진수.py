def dfs(n, mylist):
    if n == 0: 
        return mylist
    mylist.append(n % 2)
    return dfs(n // 2, mylist)

T = int(input())
for _ in range(T):
    n = int(input()) 
    ans = dfs(n, [])

    for i in range(len(ans)):
        if ans[i] == 1:
            print(i, end=' ')
    print() 