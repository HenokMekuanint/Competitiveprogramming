class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        array_ofs=[]
        array_oft=[]
        for i in range(len(t)):
            array_oft.append(t[i])
        for i in range(len(s)):
            array_ofs.append(s[i])
        array_ofs.sort()
        array_oft.sort()
        for i in range(len(array_oft)):
            if array_oft[i] in array_ofs:
                array_ofs.remove(array_oft[i])
            else:
                return array_oft[i]
