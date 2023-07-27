class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def find_count(count):
            if count == 0 or count==1:
                return 1
            if count==2:
                return 2

            ans = 0
            for left in range(count):    
                ans+= find_count(left) * find_count(count-1-left)


            return ans
        
        return find_count(n)
        