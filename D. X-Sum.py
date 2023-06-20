for i in range(int(input())):
    from collections import defaultdict
    top_left_bottom_right=defaultdict(int)
    bottom_left_top_right=defaultdict(int)
    r,c=map(int,input().split())
    ans=0
    matrix=[]
    for i in range(r):
        matrix.append(list(map(int,input().split())))
    def in_bound(row,col):
        return 0<=row<len(matrix) and 0<=col<len(matrix[row])
    for col in range(len(matrix[0])):
        itr_col=col
        for row in range(len(matrix)):
            if not in_bound(row,itr_col):
                break
            top_left_bottom_right[row-itr_col]+=matrix[row][itr_col]
            itr_col+=1
    for row in range(1,len(matrix)):
        itr_row=row
        for col in range(len(matrix[0])):
            if not in_bound(itr_row,col):
                break
            top_left_bottom_right[itr_row-col]+=matrix[itr_row][col]
            itr_row+=1
    for col in range(len(matrix[-1])):
        itr_col=col
        for row in range(len(matrix)-1,-1,-1):
            if not in_bound(row,itr_col):
                break
            bottom_left_top_right[row+itr_col]+=matrix[row][itr_col]
            itr_col+=1
    for row in range(len(matrix)-2,-1,-1):
        itr_row=row
        for col in range(len(matrix[0])):
            if not in_bound(itr_row,col):
                break
            bottom_left_top_right[itr_row+col]+=matrix[itr_row][col]
            itr_row-=1
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            ans=max(ans,top_left_bottom_right[row-col]+bottom_left_top_right[row+col]-matrix[row][col])
    print(ans)




     





