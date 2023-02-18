def merge(arr1,arr2):
    ptr1=0
    ptr2=0
    ans=[]
    counter=0
    while ptr2<len(arr2) and ptr1<len(arr1):
        if arr1[ptr1]<arr2[ptr2]:
            counter+=1
            ptr1+=1
        elif arr1[ptr1]>=arr2[ptr2]:
            ans.append(counter)
            ptr2+=1
    while ptr2<len(arr2):
        ans.append(counter)
        ptr2+=1
    return ans
s1,s2=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(*merge(arr1,arr2))
