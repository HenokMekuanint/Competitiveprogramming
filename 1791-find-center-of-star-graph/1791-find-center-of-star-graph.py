class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dicti=defaultdict(int)
        for edge1,edge2 in edges:
            dicti[edge1]+=1
            dicti[edge2]+=1
        comp=max(dicti.values())
        for vertex in dicti:
            if dicti[vertex]==comp:
                return vertex
        
        