from collections import defaultdict
d=defaultdict(list)
iter1,iter2=input().split()
groupb=[]
for i in range(1,int(iter1)+1):
    d[input()].append(str(i))
for j in range(int(iter2)):
    groupb.append(input())
for i in range(len(groupb)):
    if groupb[i] in d:
        print(" ".join(d[groupb[i]]))
    else:
        print(str(-1))
