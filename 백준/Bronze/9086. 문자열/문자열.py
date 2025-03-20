for _ in range(int(input())):
    ans = ''
    word = input().strip()
    ans += word[0]
    ans += word[-1]
    print(ans)