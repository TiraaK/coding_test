import sys
input = sys.stdin.readline

stack = [] 
for _ in range(int(input())): 
    temp = input().strip()
    if "push" in temp:
        stack.append(temp.split(" ")[1])
    elif "top" in temp:
        print(-1 if not stack else stack[-1])
    elif "size" in temp:
        print(len(stack))
    elif "empty" in temp:
        print(1 if not stack else 0)
    elif "pop" in temp:
        print(-1 if not stack else stack.pop())
