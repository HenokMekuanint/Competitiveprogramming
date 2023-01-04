def tshirt(sizes):
    # from collections import defaultdict
    size1=sizes[0]
    size2=sizes[1]
    dicti={"L":4,"M":3,"S":2,"1":0}
    if dicti[size1[-1]]>dicti[size2[-1]]:
        return ">"
    elif dicti[size1[-1]]<dicti[size2[-1]]:
        return "<"
    elif size1[-1]==size2[-1]=="S":
        if len(size1)>len(size2):
            return "<"
        elif len(size1)<len(size2):
            return ">"
        else:
            return "="
    elif size1[-1]==size2[-1]=="L":
        if len(size1)>len(size2):
            return ">"
        elif len(size1)<len(size2):
            return "<"
        else:
            return "="
    elif size1[-1]==size2[-1]=="M":
        return "="
for i in range(int(input())):
    sizes=list(input().split())
    print(tshirt(sizes))
