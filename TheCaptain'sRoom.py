K = int(input())
roon_num_list = map(int, input().split())
d = {}
for i in roon_num_list:
    if i not in d:
        d[i] = 0
    d[i] += 1
for key, values in d.items():
    if d[key] == 1:
        print(key)
