#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
       return self.merge_sort(head)
            
    def find_middle(self, head):
        if not head or not head.next:
            return head
        
        fast = head.next
        slow = head
        
        while fast.next and fast.next.next:
            slow = slow.next            
            fast = fast.next.next            
            
        return slow
        
        
    def merge(self, l1, l2):       
        dummy = ListNode(0)
        l3 = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                l3.next = l1
                l1 = l1.next
            else:
                l3.next = l2
                l2 = l2.next
            
            l3 = l3.next
            
        if l1:
            l3.next = l1
        
        if l2:
            l3.next = l2
        
        return dummy.next
    
    
    def merge_sort(self, head):
        if not head or not head.next:
            return head
        
        middle = self.find_middle(head)

        right = self.merge_sort(middle.next)
        
        middle.next = None
        left = self.merge_sort(head)        
        
        return self.merge(left, right)
