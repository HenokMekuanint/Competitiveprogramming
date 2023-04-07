from collections import defaultdict
dicti=defaultdict(list)
for row in range(int(input())):
    temp=list(map(int,input().split()))
    for col in range(len(temp)):
        if temp[col]==1:
            dicti[row+1].append(col+1)
for key in dicti:
    print(len(dicti[key]),*(dicti[key]))
