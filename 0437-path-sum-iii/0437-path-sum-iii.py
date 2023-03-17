# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        dicti=defaultdict(int)
        dicti[0]=1
        cur_sum=0
        count=[0]
        def traverse(root,cur_sum):
            if not root:
                return
            cur_sum+=root.val
            
            if dicti[cur_sum-targetSum]>0:
                count[0]+=(dicti[cur_sum-targetSum])
            dicti[cur_sum]+=1

            traverse(root.left,cur_sum)
            traverse(root.right,cur_sum)
            dicti[cur_sum]-=1
            
        traverse(root,0)
        return count[0]
        