class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        
        ans = []
        dic = {
            "rowUp":[-1,0],
            "rowDown":[1,0],
            "colRight":[0,1],
            "colLeft":[0,-1],
            "upLeft":[1,-1],
            "upRight":[1,1],
            "downRight":[-1,1],
            "downLeft":[-1,-1],
        }
        def traveler(direction):
            temp = king.copy()
            while 0<= temp[0] < 8 and 0 <= temp[1] < 8:
                temp[0] += direction[0]
                temp[1] += direction[1]
                if temp in queens:
                    return temp
            return None

        for direct in dic.keys():
            if traveler(dic[direct]) != None:
                ans.append(traveler(dic[direct]))
        return ans
        