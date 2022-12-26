# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
s1=set(input().split())
m=input()
s2=set(input().split())

print(len(s1.union(s2)))
