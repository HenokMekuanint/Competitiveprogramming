# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def BST(arr):
            if not arr:
                return None
            if len(arr) == 1:
                return TreeNode(arr[0])
            root_val = arr[0]
            root = TreeNode(root_val)
            right_index = len(arr)
            for i in range(1, len(arr)):
                if arr[i] > root_val:
                    right_index = i
                    break
            root.left = BST(arr[1:right_index])
            root.right = BST(arr[right_index:])
            return root
        return BST(preorder)
            
                
                
                
        