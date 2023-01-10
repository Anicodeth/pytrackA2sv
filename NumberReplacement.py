cin = int(input())
for _ in range(cin):
    lc = int(input())
    nums = input().split(' ')
    ls = input()

    dict = {}
    for index, n in enumerate(nums):
        l = dict.get(n, None)
        if not letter:
            dict[n] = ls[index]
        elif l != ls[index]:
            print('NO')
            break
    else:
        print('YES')
