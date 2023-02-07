class ListNode:
    
    def __init__(self, x):
        
        self.val=x
        self.next=None
class MyLinkedList:
    def __init__(self):
        self.length=0
        self.dummy=ListNode(0)
    def get(self, index: int) -> int:
        if index<0 or index>=self.length:
            return -1
        cur=self.dummy.next
        for i in range(index):
            cur=cur.next
        return cur.val
    def addAtHead(self, val: int) -> None:
        oldhead=self.dummy.next
        self.dummy.next=ListNode(val)
        self.dummy.next.next = oldhead
        self.length+=1
    def addAtTail(self, val: int) -> None:
        cur=self.dummy
        while cur.next:
            cur=cur.next
        cur.next=ListNode(val)
        self.length+=1
    def addAtIndex(self, index: int, val: int) -> None:
        if index<0 or index>self.length:
            return 
        cur=self.dummy
        for i in range(index):
            cur=cur.next
        rem=cur.next
        cur.next=ListNode(val)
        cur.next.next=rem
        self.length+=1
    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.length:
            return 
        cur=self.dummy
        for i in range(index):
            cur=cur.next
        cur.next=cur.next.next
        self.length-=1
        
