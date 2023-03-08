# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if q.val!=p.val:
                return False
            return same(p.left,q.left) and same(p.right,q.right)
        return same(p,q)
        