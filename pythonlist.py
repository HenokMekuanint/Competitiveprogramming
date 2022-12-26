if __name__ == '__main__':
    ans=[]
    for i in range(int(input())):
        comm=list(input().split())
        if comm[0]=="insert":
            ans.insert(int(comm[1]),int(comm[2]))
        elif comm[0]=="append":
            ans.append(int(comm[1]))
        elif comm[0]=="remove":
            ans.remove(int(comm[1]))
        elif comm[0]=="print":
            print(ans)
        elif comm[0]=="pop":
            ans.pop()
        elif comm[0]=="reverse":
            ans.reverse()
        elif comm[0]=="sort":
            ans.sort()
