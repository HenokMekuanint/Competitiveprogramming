# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        
        def traverse(node):
            if  node and not node.left and not node.right:
                return 1
            lft=rtn=float("inf")
            if node and node.left:
                lft=traverse(node.left)
            if node and node.right:
                rtn=traverse(node.right)
            if lft==rtn==float("inf"):
                return 0
      
          
            return min(lft,rtn)+1
        return traverse(root)
            