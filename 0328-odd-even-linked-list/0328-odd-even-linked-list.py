# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return 
        
        odd_node=head
        even_node=head.next
        evenhead=head.next
        while even_node!=None and even_node.next!=None:
            odd_node.next=odd_node.next.next
            even_node.next=even_node.next.next
            
            odd_node=odd_node.next
            even_node=even_node.next
        odd_node.next=evenhead
        return head
