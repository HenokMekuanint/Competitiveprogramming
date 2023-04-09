num_of_ones=0
for i in range(int(input())):
    temp=list(map(int,input().split()))
    for num in temp:
        if num==1:
            num_of_ones+=1
print(num_of_ones//2)
