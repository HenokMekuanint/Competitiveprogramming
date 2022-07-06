def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        newarray=[]
        newarray=s.split()
        a=""
        newarray2=[]
        dict={}
        for i in newarray:
            for j in i:
                newarray2.append(j)
        for i in newarray2:
            if i!='1' and i!='2' and i!='3' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9':
                a+=i
            else:
                dict[int(i)]=a
                a=""
        b=""
        for i in range(1,len(dict)+1):
            if i !=len(dict):
                b+=str(dict.get(i))+" "
            else:
                b+=str(dict.get(i))
        return b
