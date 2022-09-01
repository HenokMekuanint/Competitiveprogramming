        if num==1:
            return True
        rem=num%3
        if rem!=0 or num==0:
            return False
        else:
            return self.isPowerOfThree(num//3)
