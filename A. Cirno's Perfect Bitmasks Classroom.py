t = int(input())
for _ in range(t):
    x = int(input())

    if x ==1:
        print(3)
        continue

    i = 0
    y = 0
    while y<=0:
        y = x & (1<<i)
        i +=1

    if (y ^ x) == 0:
        print(y+1)
    else:
        print(y)
