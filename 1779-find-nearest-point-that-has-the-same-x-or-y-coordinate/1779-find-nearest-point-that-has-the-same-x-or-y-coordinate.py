class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis=float('inf')
        min_index=-1
        for p in range(len(points)):
            if (points[p][0]==x or points[p][1]==y) and  min_dis>abs(points[p][0]-x)+abs(points[p][1]-y):
                    min_dis=abs(points[p][0]-x)+abs(points[p][1]-y)
                    min_index=p
        return min_index
            
        