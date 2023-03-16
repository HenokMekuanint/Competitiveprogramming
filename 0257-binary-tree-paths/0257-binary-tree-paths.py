# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans=[]
        def dfs(arr,root):
            if not root:
                return
            if not root.left and not root.right:
                arr.append(str(root.val))
                ans.append("->".join(arr))
                return
            
            dfs(arr + [str(root.val)],root.left)
            dfs(arr+[str(root.val)],root.right)
            # return ans
            
        dfs([],root)
        print(ans)
        return ans
            