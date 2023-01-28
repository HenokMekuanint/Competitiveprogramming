class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        [   1,  2   ,   3   ,   4   ,   5 ]
            l   
                                        R
        """
        skill.sort()
        left=0
        right=len(skill)-1
        temp=[]
        comp=skill[0]+skill[-1]
        while left<right:
            pair_pro=skill[right]+skill[left]
            if len(temp)>0:
                if comp==pair_pro:
                    temp.append(skill[right]*skill[left])
                    left+=1
                    right-=1
                else:
                    return -1
            else:
                temp.append(skill[right]*skill[left])
                left+=1
                right-=1
        return sum(temp)
        