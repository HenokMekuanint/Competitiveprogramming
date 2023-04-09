class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        start=set()
        for neigh1,neigh2 in edges:
            start.add(neigh1)
        for  neigh1,neigh2 in edges:
            if neigh2 in start:
                start.remove(neigh2)
        return list(start)
        
        
                
            
        
        