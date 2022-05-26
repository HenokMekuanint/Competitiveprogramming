# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        dummy_head = ListNode(0)
        curr = dummy_head

        i = l1
        j = l2

        while i and j:
            i_val = i.val
            j_val = j.val

            if i_val < j_val:
                curr.next = ListNode(i_val)
                i = i.next
            else:
                curr.next = ListNode(j_val)
                j = j.next
            curr = curr.next
        if i:
            curr.next = i
        if j:
            curr.next = j

        return dummy_head.next
