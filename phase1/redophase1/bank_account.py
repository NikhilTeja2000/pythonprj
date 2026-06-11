"""
1. Create an account
2. Deposit money
3. Withdraw money
4. Check balance
5. Prevent overdraft

"""
from datetime import datetime
print(datetime.now())

class BankAccount:

    bank_name="ABE bank"



    def __init__(self,accountname, accountnumber,balance):
        self.accountname=accountname
        self._accountnumber=accountnumber
        self._balance=balance
        self._transcations=[]

    def get_balance(self):
        return self._balance

    def get_transactions(self):
        return self._transcations
    #def update_balance(self):


    def get_account_details(self):
        return [self.accountname,self._accountnumber,self.get_balance()]

    def deposit_money(self,amount):
        self._balance=self.get_balance() + amount
        transaction={
            "time": datetime.now(),
            "type": "deposit",
            "amount": amount,
            "status": "valid"
        }
        self._transcations.append(transaction)
        return f'the current balance is: {self.get_balance()}'

    def withdraw_money(self,amount):

        if amount<=self.get_balance():

            self._balance= self.get_balance()-amount
            transaction={
                "time": datetime.now(),
                "type": "deposit",
                "amount": amount,
                "status": "valid"
            }
            self._transcations.append(transaction)
        else:
            transaction={
                "time": datetime.now(),
                "type": "deposit",
                "amount": amount,
                "status": "invalid"
            }
            self._transcations.append(transaction)

            return "Amount is less than the current balance"
        return f"the current balance is: {self.get_balance()}"


    @staticmethod
    def sort_values(values,type):
        l=[]
        for a in values:

            if a['status']==type:
                l.append(a)
            
            else:
                pass
        return l

    def transaction_history(self,type):
        value = self.sort_values(self.get_transactions(),type)
        return value

    @classmethod
    def change_bank_name(cls,value):
        cls.bank_name=value
        return cls.bank_name

if __name__ == "__main__":
    obw=BankAccount("nikhil",345,100)
    print(obw.get_balance())

    print( obw.withdraw_money(30))
    print(obw.get_transactions())
    print(obw.deposit_money(200))
    print(obw.withdraw_money(400))
    print(obw.withdraw_money(100))
    print(obw.get_transactions())
    print("++++")
    print(obw.transaction_history("qvalid"))
    print("end")





