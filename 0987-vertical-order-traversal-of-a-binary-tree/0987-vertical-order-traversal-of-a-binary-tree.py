# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        dictionary=defaultdict(list)
        def traverse(root,mov,level):
            if not root:
                return
            else:
                dictionary[mov].append((level,root.val))
                traverse(root.left,mov-1,level+1)
                traverse(root.right,mov+1,level+1)
        traverse(root,0,0)
        
        
        dictionary=dict(sorted(dictionary.items(),key=lambda x:x[0]))
        for key in dictionary:
            dictionary[key]=sorted(dictionary[key])
        for key in dictionary:
            temp=[]
            for pair in dictionary[key]:
                temp.append(pair[1])
            ans.append(temp)
                
        return ans
                
        