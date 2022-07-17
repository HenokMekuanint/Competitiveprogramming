# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = {}

        dummy = ListNode(0)
        dummy.next = head
        
        
        while head != None:
            counter[head.val] = counter.get(head.val, 0) + 1            
            head = head.next
                        
        head = dummy.next
        prev = dummy
                
        while head != None:
            if counter[head.val] > 1:
                prev.next = head.next
            else:
                prev = head
            head = head.next
            
        return dummy.next
