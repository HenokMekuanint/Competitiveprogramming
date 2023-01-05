class Bank:

    def __init__(self, balance: List[int]):
        self.dicti={}
        for i in range(1,len(balance)+1):
            self.dicti[i]=balance[i-1]
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 in self.dicti and account2 in self.dicti and self.dicti[account1]>=money:
            self.dicti[account1]-=money
            self.dicti[account2]+=money
            return True
        return False
    def deposit(self, account: int, money: int) -> bool:
        if account in self.dicti:
            self.dicti[account]+=money
            return True
        return False
    def withdraw(self, account: int, money: int) -> bool:
        if account in self.dicti and self.dicti[account]>=money:
            self.dicti[account]-=money
            return True
        return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)