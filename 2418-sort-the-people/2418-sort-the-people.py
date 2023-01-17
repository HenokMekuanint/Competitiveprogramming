class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(names)):
            max_=i
            for j in range(i+1,len(names)):
                if heights[max_]<heights[j]:
                    max_=j
            heights[i],heights[max_]=heights[max_],heights[i]
            names[i],names[max_]=names[max_],names[i]
        return names
                
        """
     
[155,185,150]
        """