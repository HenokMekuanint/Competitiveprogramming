# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        cur=head
        rtn=head
        while cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return rtn
        