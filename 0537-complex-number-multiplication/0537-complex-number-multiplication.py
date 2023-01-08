class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        arr1=num1.split("+")
        arr2=num2.split("+")
        arr1[1]=arr1[1][:-1]
        arr2[1]=arr2[1][:-1]
        arr1[0],arr1[1]=int(arr1[0]),int(arr1[1])
        arr2[0],arr2[1]=int(arr2[0]),int(arr2[1])
        first_cof=str((arr1[0]*arr2[0])+(-1*(arr1[1]*arr2[1])))
        second_cof=str((arr1[0]*arr2[1])+((arr1[1]*arr2[0])))+"i"
        return first_cof+"+"+second_cof
