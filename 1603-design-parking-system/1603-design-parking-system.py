class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.biglot=big
        self.mediumlot=medium
        self.smalllot=small
    def addCar(self, carType: int) -> bool:
        if carType==1 and self.biglot>0:
            self.biglot-=1
            return True
        elif carType==2 and self.mediumlot>0:
            self.mediumlot-=1
            return True
            
        elif carType==3 and self.smalllot>0:
            self.smalllot-=1
            return True
        else:
            return False
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)