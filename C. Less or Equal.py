def checker(array,k):
    array.sort()
    if k==0:
        if array[0]>1:
            array[0]-=1
            return array[0]
        else:
            return -1
    for i in range(len(array)):
        if i+1==k:
            if i<len(array)-1 and array[i]==array[i+1]:
                return -1
            elif i<len(array)-1 and array[i]!=array[i+1]:
                return array[i+1]-1
            elif i==len(array)-1 and i+1==k:
                return array[i]
size,k=map(int,input().split())
array=list(map(int,input().split()))
print(checker(array,k))
