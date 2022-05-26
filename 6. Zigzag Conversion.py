def convert(s,numsrows):
    if numsrows==1: return s
    res=""
    for r in range(numsrows):
        increment=2*(numsrows-1)
        for i in range(r,len(s),increment):
            res+=s[i]
            if(r>0 and r<numsrows-1 and i+ increment-2*r<len(s)):
                res+=s[i+ increment-2*r]
    return res
print(convert("PAYPALISHIRING",4))