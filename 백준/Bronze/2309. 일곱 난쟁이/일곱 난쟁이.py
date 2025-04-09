
input_list = [int(input()) for _ in range(9)]
result = []
found = False

def dfs(path, idx):
    global found, result
    if found:
        return
    if len(path) == 7:
        if sum(path) == 100:
            result = path
            found = True
        return
    for i in range(idx, 9):
        dfs(path + [input_list[i]], i+1)
        
dfs([], 0)

for res in sorted(result):
    print(res)