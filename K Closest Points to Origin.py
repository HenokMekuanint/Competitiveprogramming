def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        points.sort(key = lambda k: k[0]**2 + k[1]**2)
 
        return points[:k]
