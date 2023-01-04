def replacement(arr1,str1):
    for i in range(len(str1)):
        being_replaced=arr1[i]
        for j in range(i,len(arr1)):
            if arr1[j].isdigit() and being_replaced==arr1[j]:
                arr1[j]=str1[i]
    ans="".join(arr1)
    if ans==str1:
        return "YES"
    else:
        return "NO"
for i in range(int(input())):
    _=input()
    arr=list(input().split())
    stri=input()
    print(replacement(arr,stri))
