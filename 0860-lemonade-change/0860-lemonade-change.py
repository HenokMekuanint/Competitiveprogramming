class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        no_of_ten=0
        no_of_20=0
        no_of_five=0
        for i in range(len(bills)):
            if bills[i]==5:
                no_of_five+=1
            if bills[i]==10:
                if not no_of_five:
                    return False
                else:
                    no_of_ten+=1
                    no_of_five-=1
            elif bills[i]==20:
                if no_of_ten>0 and no_of_five>0:
                    no_of_ten-=1
                    no_of_five-=1
                    no_of_20+=1
                elif no_of_five>=3:
                    no_of_five-=3
                else:
                    return False
        return True
        