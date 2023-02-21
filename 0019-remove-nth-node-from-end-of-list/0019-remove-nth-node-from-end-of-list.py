# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        cur=head
        while cur:
            count+=1
            cur=cur.next
        rem_nd=count-n
        if rem_nd==0:
            return head.next
        cur2=head
        rtn=cur2
        ctr2=1
        while cur2:
            
            if ctr2==rem_nd:
                cur2.next=cur2.next.next
                return rtn
            else:
                cur2=cur2.next
                ctr2+=1
            
            
        
        