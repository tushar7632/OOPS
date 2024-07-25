
class Account:
        def _init_(self, balance,acc):
                self.balance = balance
                self.account_no = acc
                
                # debit method
                def debit(self, amount):
                        self.balance -= amount
                        print("Rs.", amount, "was debited")
                        print("total balance = ", self.get_balance())
                        
                        def credit(self, credit):
                                self.balance += amount
                        print("Rs.", amount, "was credited")
                        print("total balance = ", self.get_balance())
        def get__balance(self):
                return self.balance
                        
acc1 = Account(5000, 1000)
# acc1.debit(1000)
# acc1.credit(500)
