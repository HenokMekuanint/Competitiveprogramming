# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        def comp_and_build(list1: Optional[ListNode],list2:Optional[ListNode],dummy):
            if list1 and list2:
                if list1.val>=list2.val:
                    dummy.next=ListNode(list2.val)
                    dummy=dummy.next
                    list2=list2.next
                    comp_and_build(list1,list2,dummy)
                else:
                    dummy.next=ListNode(list1.val)
                    dummy=dummy.next
                    list1=list1.next
                    comp_and_build(list1,list2,dummy)
            elif list1:
                dummy.next=ListNode(list1.val)
                dummy=dummy.next
                list1=list1.next
                comp_and_build(list1,list2,dummy)
            elif list2:
                dummy.next=ListNode(list2.val)
                dummy=dummy.next
                list2=list2.next
                comp_and_build(list1,list2,dummy)
            elif not list1 and not list2:
                return None
        
                    
        comp_and_build(list1,list2,dummy)
        return dummy.next
                    
            
            
        