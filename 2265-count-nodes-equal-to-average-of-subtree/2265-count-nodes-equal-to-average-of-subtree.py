# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans=[0]       
        def traverse(root):
            if not root:
                return 0,0
            left_sum,left_nodes=traverse(root.left)
            right_sum,right_nodes=traverse(root.right)
            cur_sum=root.val+left_sum+right_sum
            no_of_nodes=left_nodes+right_nodes+1
            if (cur_sum//(no_of_nodes))==root.val:
                ans[0]+=1
            return cur_sum,no_of_nodes
        traverse(root)
        return ans[0]
                
        
        