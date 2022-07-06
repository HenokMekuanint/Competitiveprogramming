class MyQueue(object):

    def __init__(self):
        self.array1=[]
        self.array2=[]

    def push(self, x):
        self.array1.append(x)
        
    def pop(self):
        for i in range(len(self.array1)):
            self.array2.append(self.array1.pop())
        poped=self.array2.pop()
        for i in range(len(self.array2)):
            self.array1.append(self.array2.pop())
        return poped
    
    def peek(self):
        for i in range(len(self.array1)):
            self.array2.append(self.array1.pop())
        peeked=self.array2[-1]
        for i in range(len(self.array2)):
            self.array1.append(self.array2.pop())
        return peeked
    def empty(self):
        return (len(self.array1))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
