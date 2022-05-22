
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Length = 0
        l2Length = 0
        
        current = l1
        while current:
            l1Length += 1
            current = current.next
        
        current = l2
        while current:
            l2Length += 1
            current = current.next

        if l1Length >= l2Length:  
            head1 = l1
            head2 = l2
        else:
            head2 = l1 
            head1 = l2

        
        rem = 0
        while head1:
            if rem:
                head1.val += rem
                rem = 0
            if head2:
                head1.val = head1.val + head2.val
            if head1.val >= 10:
                temp = str(head1.val)
                rem = int(temp[0])
                head1.val = int(temp[1])
            if rem and head1.next == None:
                head1.next = ListNode(rem)
                rem = 0
            
            head1 = head1.next
            
            if head2:
                head2 = head2.next
            
        if l1Length >= l2Length: 
            return l1
        else:
            return l2

        
            
