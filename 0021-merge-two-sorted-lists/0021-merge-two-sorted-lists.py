# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return 
        elif not list1:
            return list2
        elif not list2:
            return list1
        if list1.val>list2.val:
            head=ListNode(list2.val)
            list2=list2.next
            rtn=head
        else:
            head=ListNode(list1.val)
            rtn=head
            list1=list1.next
        while list1 and list2:
            if list1.val>list2.val:
                head.next=ListNode(list2.val)
                head=head.next
                list2=list2.next
            else:
                head.next=ListNode(list1.val)
                head=head.next
                list1=list1.next
        while list1:
            head.next=ListNode(list1.val)
            head=head.next
            list1=list1.next
        while list2:
            head.next=ListNode(list2.val)
            head=head.next
            list2=list2.next
        return rtn
            
        