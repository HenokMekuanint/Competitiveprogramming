def merge(arr1,arr2):
    ptr1=0
    ptr2=0
    ans=[]
    while ptr1<len(arr1) and ptr2<len(arr2):
        if arr1[ptr1]>arr2[ptr2]:
            ans.append(arr2[ptr2])
            ptr2+=1
        else:
            ans.append(arr1[ptr1])
            ptr1+=1
    while ptr1<len(arr1):
            ans.append(arr1[ptr1])
            ptr1+=1
    while ptr2<len(arr2):
            ans.append(arr2[ptr2])
            ptr2+=1
    return ans
s1,s2=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
print(*merge(arr1,arr2))
        
        
        
