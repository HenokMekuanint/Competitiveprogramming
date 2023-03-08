# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def sum_two_nodes(p,q):
            
            if not p: return q
            if not q: return p
            if p and q: 
                ans = TreeNode(p.val + q.val)
                ans.left = sum_two_nodes(p.left, q.left)
                ans.right = sum_two_nodes(p.right, q.right)
            return ans
        return sum_two_nodes(root1,root2)