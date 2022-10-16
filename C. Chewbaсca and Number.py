x = list(input())
for i in range(len(x)):
    if (i == 0 and '5' <= x[0] <= '8') or (i != 0 and '5' <= x[i] <= '9'):
        x[i] = str(9-int(x[i]))
    print(x[i], end = '')
