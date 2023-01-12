class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        counter=0
        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if strs[j-1][i]>strs[j][i]:
                    counter+=1
                    break
        return counter
        
        