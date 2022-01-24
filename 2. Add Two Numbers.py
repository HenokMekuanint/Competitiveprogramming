# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        temp = res
        carry = 0
        
        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            
            cur_sum = a+b+carry
            carry = 0
            if cur_sum > 9:
                carry = cur_sum//10
                cur_sum = cur_sum%10
                
            res.next = ListNode(cur_sum)
            res = res.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if carry:
            res.next = ListNode(carry)
            
        return temp.next
