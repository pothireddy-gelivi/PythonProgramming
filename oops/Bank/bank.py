class Bank:
    bank_name="State Bank Of India"
    bank_branch="Dharmavaram"
    bank_roi=5
    def __init__(self,cname,account,balance,mobile):
        self.cname=cname
        self.account=account
        self.balance=balance
        self.mobile=mobile
    def customer_details(self):
        print(f"customer name is {self.cname}")
        print(f"customer Account number is {self.account}")
        print(f"customer Bank Balance is {self.balance}")
        print(f"customer Mobile number is {self.mobile}")
    def withdraw(self):
        amount=int(input("Enter the amount how much you want?"))
        self.balance-=amount
        print("withdraw successful")
        print(f"Available balance is {self.balance}")
    def balance_check(self):
       print(f"Available balance is {self.balance}")
    def deposite(self):
        amount=int(input("Enter the amount to deposit."))
        self.balance+=amount
        print("successfully deposited")

reddy=Bank("Gelivi pothireddy",289735766915,15000,7569118920)
kavya=Bank("Gotluru Kavya Sree",289735766916,50000,6303364884)
pavani=Bank("Gelivi pavani",289735766917,1200,9966593133)
