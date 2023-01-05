class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
        [5,4,0,2]
        
        [[1,1],[3,1],[3,3],[5,1]]
        total=6
        [5,4,0,2]
        """
        total=0
        res=[]
        for num in nums:
            if num%2==0:
                total+=num
        for query in queries:
            value=query[0]
            index=query[1]
            if (nums[index]%2==0 and value%2==0):
                nums[index]+=value
                total+=value
            elif ( nums[index]%2!=0 and value %2 !=0):
                print(nums[index],value)
                nums[index]+=value
                total+=nums[index]
            else:
                if nums[index]%2==0:
                    total-=nums[index]
                    nums[index]+=value
                else:
                    nums[index]+=value
            res.append(total)
        return res
            
            
        