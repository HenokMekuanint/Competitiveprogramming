    if num==1:
        return True
    rem=num%4
    if rem!=0 or num==0:
        return False
    else:
        return isPowerOfFour(num//4)
