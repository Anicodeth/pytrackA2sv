n,m = list(map(int, input().split()))
a = [input() for i in range(n)]
b = [input() for j in range(m)]
ls = [(x,y) for x,y in enumerate(a)]

for i in b:
    new = []
    for s in ls:
        if s[1] == i:
            new.append(str(s[0]+1))
    if new:
        print(" ".join(new))
    else:
        print(-1)
