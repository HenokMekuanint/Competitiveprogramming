class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False 
        array1=[0 for i in range(26)]
        for i in range(len(s1)):
            array1[ord(s1[i])-97]+=1   
        array2=[0 for i in range(26)]
        for i in range(len(s1)):
            array2[ord(s2[i])-97]+=1
        left,right=0,len(s1)-1
        if array1==array2: return True
        while array1!=array2 and right<len(s2)-1:
            if array1==array2:
                return True
            else:
                if array2[ord(s2[left])-97]>0:
                    array2[ord(s2[left])-97]-=1
                    left+=1
                else:
                    array2[ord(s2[left])-97]=0
                    left+=1
                right+=1
                array2[ord(s2[right])-97]+=1
        return True if array1==array2 else False
        
