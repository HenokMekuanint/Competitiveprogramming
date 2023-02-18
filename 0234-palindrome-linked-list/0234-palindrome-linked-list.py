# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        org=head
        rev=head
        prev=None
        copy=ListNode(head.val)
        clone=copy
        while head.next:
            head=head.next
            copy.next=ListNode(head.val)
            copy=copy.next
        while rev:
            or_nxt=rev.next
            rev.next=prev
            prev=rev
            rev=or_nxt
        while prev and clone:
            if prev.val==clone.val:
                prev=prev.next
                clone=clone.next
            else:
                return False
        return True
                
            
        