# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=set()
        cur=head
        while cur:
            if id(cur) not in temp:
                temp.add(id(cur))
            elif id(cur) in temp:
                return cur
            cur=cur.next
        return None
         