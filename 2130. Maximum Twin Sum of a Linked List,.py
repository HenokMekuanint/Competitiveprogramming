# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(head: ListNode) -> ListNode:
          prev = None
          while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
          return prev

        ans = 0
        slow = head
        fast = head

        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

        tail = reverseList(slow)

        while tail:
          ans = max(ans, head.val + tail.val)
          head = head.next
          tail = tail.next

        return ans
