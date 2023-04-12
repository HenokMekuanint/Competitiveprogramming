# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[""]
        def traverse(node):
            if not node:
                return ""
            if node.left == node.right:
                return str(node.val)
            if not node.right:
                return str(node.val) + '(' + traverse(node.left) + ')'
            return str(node.val) + '(' + traverse(node.left) + ')(' + traverse(node.right) + ')'
        return traverse(root)