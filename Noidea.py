n,m = list(map(int, input().split()))
n_arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0
for i in n_arr:
    if i in a:
        happiness +=1
    elif i in b:
        happiness -=1
print(happiness)
