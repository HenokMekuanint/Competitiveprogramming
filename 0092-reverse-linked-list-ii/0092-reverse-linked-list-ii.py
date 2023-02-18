# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur=head
        temp=[]
        while cur:
            temp.append(cur.val)
            cur=cur.next
        left-=1
        right-=1
        while left<right:
            temp[right],temp[left]=temp[left],temp[right]
            left+=1
            right-=1
        newhead=ListNode(temp[0])
        rtrn=newhead
        for i in range(1,len(temp)):
            newhead.next=ListNode(temp[i])
            newhead=newhead.next
        return rtrn
        
            
        