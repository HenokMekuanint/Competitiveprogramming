from collections import defaultdict
dicti=defaultdict(list)
no_of_nodes=int(input())
for i in range(int(input())):
    temp=list(map(int,input().split()))
    if temp[0]==1:
        dicti[temp[1]].append(temp[2])
        dicti[temp[2]].append(temp[1])

    elif temp[1] in dicti:
        print(*dicti[temp[1]])
