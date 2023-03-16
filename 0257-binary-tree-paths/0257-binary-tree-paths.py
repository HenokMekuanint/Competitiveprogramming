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
                arr.pop()
                return
            arr.append(str(root.val))
            dfs(arr,root.left)
            dfs(arr,root.right)
            arr.pop()
            
        dfs([],root)
        print(ans)
        return ans
            