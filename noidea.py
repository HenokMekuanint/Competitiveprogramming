# Enter your code here. Read input from STDIN. Print output to STDOUT
_size=input()
collection=list(input().split())
seta=set(input().split())
setb=set(input().split())
happiness=0
for i in collection:
    if i in seta:
        happiness+=1
    if i in setb:
        happiness -= 1
print(happiness)

