# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        rtn_left=leftside=ListNode(0)
        rtn_right=rightside=ListNode(0)
        cur=head
        while cur:
            if cur.val<x:
                leftside.next=ListNode(cur.val)
                leftside=leftside.next
            else:
                rightside.next=ListNode(cur.val)
                rightside=rightside.next
            cur=cur.next
        leftside.next=rtn_right.next
        return rtn_left.next
                
                
        
        