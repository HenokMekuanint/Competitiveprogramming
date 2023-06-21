n=int(input())
l=list(map(int,input().split()))
for i in l:
    if(i%2!=l[0]%2):
        l.sort()
        break
print(*l)
