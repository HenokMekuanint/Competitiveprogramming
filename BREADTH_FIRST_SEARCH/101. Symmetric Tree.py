# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root ==None:
            return True
        return self.MIRROR(root,root)
    def MIRROR(self,right,left):
        if left==None and right ==None:
            return True
        elif left==None or right ==None:
            return False
        else:
            return left.val==right.val and self.MIRROR(left.left,right.right) and self.MIRROR(left.right,right.left)
        