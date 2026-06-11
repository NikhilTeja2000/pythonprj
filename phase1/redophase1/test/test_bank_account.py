import unittest
from phase1.redophase1.bank_account import BankAccount

class MyTestCase(unittest.TestCase):

    def test_deposit_money(self):
        #arragne
        value=BankAccount("rani",232,200)
        #act
        result=value.deposit_money(30)
        #assert
        self.assertEqual(result, f'the current balance is: 230')

    def test_withdraw_money(self):
        #arragne
        value=BankAccount("mike",232,200)
        #act
        result=value.withdraw_money(100)
        #assert
        self.assertEqual(result,f'the current balance is: 100')

    def test_withdraw_moremoney(self):
        #arragne
        value=BankAccount("akhil",232,200)
        #act
        result=value.withdraw_money(300)
        #assert
        self.assertEqual(result,f'Amount is less than the current balance')




if __name__ == '__main__':
    unittest.main()
