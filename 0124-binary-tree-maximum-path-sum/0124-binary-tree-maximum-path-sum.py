# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans=[float("-inf")]
        
        def traverse(node):
            ans[0]=max(ans[0],node.val)
            
            if node and not node.left and not node.right:
                return node.val
            if node.left:
                left_sum=traverse(node.left)
            else:
                left_sum=0
            if node.right:
                right_sum=traverse(node.right)
            else:
                right_sum=0
            ans[0]=max(ans[0],node.val+left_sum+right_sum)
            if node.val<node.val+left_sum and left_sum>right_sum:
                ans[0]=max(ans[0],node.val+left_sum)
                return node.val+left_sum
            elif node.val<node.val+right_sum and left_sum<right_sum:
                ans[0]=max(ans[0],node.val+right_sum)
                return node.val+right_sum
            else:
                ans[0]=max(ans[0],node.val)
                return node.val
        traverse(root)
        return ans[0]
        
        