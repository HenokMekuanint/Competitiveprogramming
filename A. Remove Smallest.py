def removesmall(array):
    array.sort()
    left=0
    right=1
    while right<len(array):
        if abs(arr[right]-array[left])<=1:
            if arr[right]<arr[left]:
                arr.pop(right)
            else:
                arr.pop(left)
        else:
            left+=1
            right+=1
    if len(array)<=1:
        return "YES"
    else:
        return "NO"
 
for i in range(int(input())):
    size=input()
    arr=list(map(int,input().split()))
    print(removesmall(arr))
