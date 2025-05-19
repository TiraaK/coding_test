n, k = map(int, input().split(" "))
mylist = list(range(1, n+1))
index = 0
answer = []
 
while mylist: 
    index = (index + k - 1) % len(mylist)
    answer.append(mylist.pop(index))

print("<" + ", ".join(map(str, answer)) + ">")
