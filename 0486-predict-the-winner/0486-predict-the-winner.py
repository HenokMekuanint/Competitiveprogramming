class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        s={}
        def turn(l,r,player):
            if (l,r,player) in s:return s[(l,r,player)]
            if l>r:return 0
            if player:s[(l,r,player)]=max(nums[l]+turn(l+1,r,not player),nums[r]+turn(l,r-1,not player))
            else:s[(l,r,player)]=min(-nums[l]+turn(l+1,r,not player),-nums[r]+turn(l,r-1,not player))
            return s[(l,r,player)]
        return turn(0,len(nums)-1,True)>=0