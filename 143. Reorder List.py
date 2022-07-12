# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        dummy = ListNode(0, None)
        while head2:
            tmp = head2.next
            head2.next = dummy.next
            dummy.next = head2
            head2 = tmp
        head1 = head
        head2 = dummy.next
        while head1 and head2:
            tmp = head2
            head2 = head2.next
            tmp.next = head1.next
            head1.next = tmp
            head1 = head1.next.next
