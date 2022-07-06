newarray=[]
    for i in path:
        if i=='d' or i=="D":
            newarray.append(-1)
        elif i=='U' or i=='u':
            newarray.append(1)
    count=0
    count2=0
    for i in newarray:
        count+=i
        if count==0 and i==1:
            count2=count2+1
    return count2
