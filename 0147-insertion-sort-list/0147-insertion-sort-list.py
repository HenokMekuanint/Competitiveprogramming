# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=[]
        cur=head
        while cur:
            temp.append(cur.val)
            cur=cur.next
        temp.sort()
        dummy=rtn=ListNode(0)
        for num in temp:
            dummy.next=ListNode(num)
            dummy=dummy.next
        return rtn.next
        