# def prime_sieve(n: int) -> list[bool]:
#     is_prime: list[bool] = [True for _ in range(n + 1)]
#     is_prime[0] = is_prime[1] = False
#     i = 2
#     while i * i <= n:
#         if is_prime[i]:
#             j = i * i
#             while j <= n:
#                 is_prime[j] = False
#                 j += i
#         i += 1
#     return [i for i in range(2, n + 1) if is_prime[i]]
# a={"a"}
# b={"b"}
# print(prime_sieve(5))
# print(a.intersection(b))
iter=int(input())
matrix=[]
source=[]
sink=[]
for i in range(iter):
    temp=list(map(int,input().split()))
    matrix.append(temp)
for i in range(len(matrix)):
    row_sum=0
    for j in range(len(matrix[i])):
        row_sum+=matrix[i][j]
        if row_sum>0:
            break
    if row_sum==0:
        sink.append(i+1)
for j in range(len(matrix[0])):
    cur_sum=0
    for i in range(len(matrix)):
        cur_sum+=matrix[i][j]
        if cur_sum>0:
            break
    if cur_sum==0:
        source.append(j+1)
print(len(source),*source)
print(len(sink),*sink)



    


