# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(map(int, input().split()))
result = []
for i in range(int(input())):
    B = set(map(int, input().split()))
    if not A.issuperset(B):
        result.append(False) 
    else:
        result.append(True)

print(bool(not(False in result)))  
