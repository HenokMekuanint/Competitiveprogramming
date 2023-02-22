# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size=0
        cur=head
        if not head:
            return
        while cur:
            cur=cur.next
            size+=1
        if size==1:
            return head
        if k>size:
            k=k%size
        for i in range(k):
            cur=head
            while cur:
                if not cur.next.next:
                    lastnode=cur.next
                    cur.next=None
                    lastnode.next=head
                    head=lastnode
                    break
                cur=cur.next
        return head
                
            
        
            
        