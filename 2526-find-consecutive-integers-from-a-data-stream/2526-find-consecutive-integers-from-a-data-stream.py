class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.counter=0
    def consec(self, num: int) -> bool:
        if num==self.value:
            self.counter+=1
        elif num!=self.value:
            self.counter=0
            
        if self.counter>=self.k:
            return True
        return False
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)