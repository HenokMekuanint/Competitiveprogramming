def composition(prog,mat):
    d=0
    if prog==mat:
        return ((prog+mat)//4)
    elif prog>mat:
        d=prog-mat
        prog-=d
        d//=2
        d=min(prog,d)
        prog-=d
        mat-=d
        d+=((prog+mat)//4)
        return d
    else:
        d=mat-prog
        mat-=d
        d//=2
        d=min(mat,d)
        mat-=d
        prog-=d
        d+=((mat+prog)//4)
        return d
    
for i in range(int(input())):
    prog,mat=map(int,input().split())
    print(composition(prog,mat))
