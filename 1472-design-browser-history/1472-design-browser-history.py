class ListNode:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.prev=prev
        self.next=next
class BrowserHistory:

    def __init__(self, homepage: str):
        self.current_page=ListNode(homepage)
    def visit(self, url: str) -> None:
        new_page=ListNode(url)
        new_page.prev=self.current_page
        self.current_page.next=new_page
        self.current_page=new_page
       
    def back(self, steps: int) -> str:
        # print(self.current_page.val)
        while steps>0 and self.current_page.prev:
            self.current_page=self.current_page.prev
            steps-=1
        return self.current_page.val
    def forward(self, steps: int) -> str:
        while steps>0 and self.current_page.next:
            self.current_page=self.current_page.next
            steps-=1
        return self.current_page.val
    
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)