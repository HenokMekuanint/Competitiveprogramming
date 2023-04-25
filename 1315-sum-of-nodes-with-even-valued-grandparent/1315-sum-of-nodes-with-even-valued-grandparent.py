# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        dicti=defaultdict(list)
        ans=[0]
        def traverse(node):
            if not node:
                return
            if node.val%2==0:
                if node.left:
                    if node.left.left:
                        ans[0]+=node.left.left.val
                    if node.left.right:
                        ans[0]+=node.left.right.val
                if node.right:
                    if node.right.left:
                        ans[0]+=node.right.left.val
                    if node.right.right:
                        ans[0]+=node.right.right.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return ans[0]
            
                
        