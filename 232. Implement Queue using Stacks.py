class MyQueue(object):

    def __init__(self):
        self.array1=[]
        self.array2=[]

    def push(self, x):
        self.array1.append(x)
        
    def pop(self):
        popped=self.peek()
        return self.array2.pop()
    
    def peek(self):
        if not self.array2:
            while self.array1:
                self.array2.append(self.array1.pop())
        return self.array2[-1]  
    def empty(self):
        return not self.array1 and not self.array2
