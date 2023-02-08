# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=None
        cur=head
        while cur:
            ornext=cur.next
            cur.next=dummy
            dummy=cur
            cur=ornext
        return dummy