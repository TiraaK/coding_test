word = input().strip()
ans = ""
for c in word:
    if c.islower():
        ans += c.upper()
    elif c.isupper():
        ans += c.lower()
print(ans)