# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head
        # Dummy node before headNode
        dummy = ListNode(-1)
        # Point the next of this dummy node to the current headNode
        dummy.next = head
        # Node to keep track of the previous node
        previous = dummy
        # Variable to keep count of the nodes in the linked list
        count = 0
        # Reference to the headNode which will be used to traverse
        current = head
        # Loop for all the nodes in the list
        while current is not None:
            count += 1
            if count % k == 0:
                previous = self.reverseList(previous, current.next)
                current = previous.next
            else:
                current = current.next
        return dummy.next

    def reverseList(self,start, end):
        previous = start.next
        current = previous.next
        while current is not end:
            nextNode = current.next
            current.next = start.next
            start.next = current
            current = nextNode
        previous.next = end
        return previous
