# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        memo={}
        def dp(node,Id):
            if not node:
                return 0
            
            if (node.val,Id) in memo:
                return memo[(node.val,Id)]
            else:
                if node.left:
                    left_of_left=dp(node.left.left,4*Id+3)
                    right_of_left=dp(node.left.right,4*Id+4)
                else:
                    left_of_left=0
                    right_of_left=0
                if node.right:
                    left_of_right=dp(node.right.left,4*Id+5)
                    right_of_right=dp(node.right.right,4*Id+6)
                else:
                    left_of_right=0
                    right_of_right=0
                if node:
                    memo[(node.val,Id)]=max(dp(node.left,2*Id+1)+dp(node.right,2*Id+2),node.val+left_of_left+right_of_left+left_of_right+right_of_right)
            
            return memo[(node.val,Id)]
        return max(dp(root,0),dp(root.left,1)+dp(root.right,2))
        