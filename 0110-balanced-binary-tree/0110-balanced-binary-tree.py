# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans=True
        def traverse(node):
            nonlocal ans
            if not node:
                return 1
            
            left_rtn=traverse(node.left)
            right_rtn=traverse(node.right)
            if abs(right_rtn-left_rtn)>1:
                ans=False
            return max(left_rtn+1,right_rtn+1)
        traverse(root)
        return ans
                
            
            
            
            