from collections import deque
import sys
input = sys.stdin.readline
q = deque()

for _ in range(int(input())):
    temp = input().strip()
    if "push" in temp:
        q.append(temp.split(" ")[1])
    elif "front" in temp:
        print(-1 if not q else q[0])
    elif "back" in temp:
        print(-1 if not q else q[-1])
    elif "size" in temp:
        print(len(q))
    elif "empty" in temp:
        print(1 if not q else 0)
    elif "pop" in temp:
        print(-1 if not q else q.popleft()) 
    