def fibbo(a, b, cnt, tg):
    if cnt == tg:
        return a
    return fibbo(b, a+b, cnt+1, tg)
print(fibbo(0,1,0, int(input())))