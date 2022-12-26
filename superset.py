# Enter your code here. Read input from STDIN. Print output to STDOUT
seta=set(input().split())
is_super=True
for i in range(int(input())):
    if seta.issuperset(set(input().split())):
        continue
    else:
        is_super=False
print(is_super)
