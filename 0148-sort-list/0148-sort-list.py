# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        temp=[]
        cur=head
        while cur:
            temp.append(cur.val)
            cur=cur.next
        temp.sort()
        hd=rtn=ListNode(temp[0])
        for i in range(1,len(temp)):
            hd.next=ListNode(temp[i])
            hd=hd.next
        return rtn
        