# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

        # Recursion
        # if not head or not head.next:
        #     return head
        # node = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return node
