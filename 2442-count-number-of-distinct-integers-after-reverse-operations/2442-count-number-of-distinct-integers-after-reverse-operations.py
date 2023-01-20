class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        rev=[]
        for num in nums:
            temp=list(str(num))
            temp.reverse()
            temp="".join(temp)
            rev.append(int(temp.lstrip("0")))
        nums.extend(rev)
        ans=set()
        for num in nums:
           ans.add(num)
        return len(list(ans))
            
        