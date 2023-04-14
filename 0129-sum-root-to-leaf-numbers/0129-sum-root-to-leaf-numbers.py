# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        nums=[]
        
        def traverse(node,num):
            if node and not node.left and not node.right:
                nums.append(num+str(node.val))
                return
        
            if node.left:traverse(node.left,num+str(node.val))
            if node.right:traverse(node.right,num+str(node.val))
            return nums
        traverse(root,"")
        return sum(map(int,nums))
                
        
    
                
        