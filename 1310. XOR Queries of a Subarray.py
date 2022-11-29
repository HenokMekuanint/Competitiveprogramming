class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        
        prefixor=[0 for i in range(len(arr)+1)]
        curxor=0
        for i in range(len(arr)):
            curxor=curxor ^  arr[i]
            prefixor[i+1]=curxor
        result=[0 for i in range(len(queries))]
        for index,pair in enumerate (queries):
            left=pair[0]
            right=pair[1]
            result[index]=prefixor[left]^prefixor[right+1]
        return result
            
            
        
        
        
        
