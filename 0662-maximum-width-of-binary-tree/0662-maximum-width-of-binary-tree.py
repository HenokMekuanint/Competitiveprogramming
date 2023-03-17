# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        min_ans,max_ans=float("inf"),float("-inf")
        dicti=defaultdict(list)
        def traverse(root,level,index):
            if not root:
                return
            if root:
                dicti[level].append(index)
                traverse(root.left,level+1,2*index)
                traverse(root.right,level+1,(2*index)+1)
        traverse(root,0,0)
        temp=list(dicti.values())
        for i in range(len(temp)-1,-1,-1):
            if len(temp[i])>1:
                if max(temp[i])-min(temp[i])>max_ans-min_ans:
                    min_ans=min(temp[i])
                    max_ans=max(temp[i])
        if max_ans==float("-inf") and min_ans==float("inf"):
            return 1
        else:
            return max_ans-min_ans+1