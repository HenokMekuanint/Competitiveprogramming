# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp=[]
        cur=head
        i=0
        while cur:
            temp.append((cur.val,i))
            cur=cur.next
            i+=1
        ans=[0 for i in range(len(temp))]
        
        stack=[]
        for i in range(len(temp)):
            while stack and stack[-1][0]<temp[i][0]:
                popped=stack.pop()
                ans[popped[1]]=temp[i][0]
            else:
                stack.append(temp[i])
        return ans
                
            
        