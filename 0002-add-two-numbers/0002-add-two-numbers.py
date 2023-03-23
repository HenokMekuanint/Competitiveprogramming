# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=[]
        temp2=[]
        cur=l1
        cur2=l2
        while cur:
            temp1.append(str(cur.val))
            cur=cur.next
        while cur2:
            temp2.append(str(cur2.val))
            cur2=cur2.next
        temp1.reverse()
        temp2.reverse()
        
        added="".join(reversed(list(str(int("".join(temp1))+int("".join(temp2))))))
        dummy=rtn=ListNode(0)
        
        for i in range(len(added)):
            dummy.next=ListNode(int(added[i]))
            dummy=dummy.next
        return rtn.next
        
        
        
        
            
        