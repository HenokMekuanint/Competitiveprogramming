# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        dummy=ListNode(-1)
        rtn=dummy
        cur=head
        dicti=defaultdict(int)
        while cur:
            dicti[cur.val]+=1
            cur=cur.next
        for num in dicti:
            if dicti[num]>1:
                continue
            else:
                dummy.next=ListNode(num)
                dummy=dummy.next
        return rtn.next
                