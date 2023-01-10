class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans=[]
        if num%3==0:
            i=int(num/3)
            ans.append(i-1)
            ans.append(i)
            ans.append(i+1)
        return ans
        