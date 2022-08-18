class MyStack:

    def __init__(self):
        self.array1=[]
        self.array2=[]
    def push(self, x: int) -> None:
        self.array1.append(x)

    def pop(self) -> int:
        for i in range(0,len(self.array1)):
            self.array2.append(self.array1.pop())
        popped=self.array2.pop(0)
        
        for i in range(0,len(self.array2)):
            self.array1.append(self.array2.pop())
        return popped
            
    def top(self) -> int:
        for i in range(0,len(self.array1)):
            self.array2.append(self.array1.pop())
        top=self.array2[0]
        
        for i in range(0,len(self.array2)):
            self.array1.append(self.array2.pop())
        return top

    def empty(self) -> bool:
        return len(self.array1)==0
