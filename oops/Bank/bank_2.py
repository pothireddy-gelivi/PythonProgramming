class Bank_v1:
    bank_name="sbi"
    bank_branch="kazikisthan"
    bank_roi=5
    def __init__(self,cn,ca,cb):
        self.cname=cn
        self.caccount=ca
        self.cbalance=cb
    
    
    def customer_details(self):
        print(f"customer name is {self.cname}")
        print(f"customer account number is {self.caccount}")
        print(f"customer available balance is {self.cbalance}")

    @classmethod
    def bank_details(cls):
        print(f"bank name is {cls.bank_name}")
        print(f"bank branch is {cls.bank_branch}")
        print(f"bank roi is {cls.bank_roi}")

    @staticmethod
    def get_int_value():
        int_value=int(input())
        return int_value
    
    def withdraw(self):
        print("enter the withdraw amount")
        amount=self.get_int_value()
        if amount<= self.cbalance:
            self.cbalance-=amount
            print("withdraw successful")
        else:
            print("insufficient balance")


    @classmethod
    def modify_roi(cls):
        print("enter the new rate of interest: ")
        newroi=cls.get_int_value()
        cls.bank_roi=newroi
        print("Rate of Interest successfully modified")
    
kavya=Bank_v1("kavya",123456789,15000)
pavani=Bank_v1("pavani",1234567890,1290)
reddy=Bank_v1("pothireddy",289735766915,1300)

# kavya.withdraw()
# kavya.customer_details()

class Bank_v2(Bank_v1):
    bank_branch="bangalore"
    bank_ifse=1234
    def __init__(self,cn,ca,cb,cp,cm):
       super().__init__(cn,ca,cb)
       self.cpin=cp
       self.cmobile=cm

    def customer_details(self):
        super().customer_details()
        print(f"customer mobile number is {self.cmobile}")
    
    def withdraw(self):
        print("enter your password")
        pin=self.get_int_value()
        if pin==self.cpin:
            super().withdraw()
        else:
            print("Incorrect password.")
    

    def deposite(self):
        print("enter the deposited amount:")
        amount=self.get_int_value()
        self.cbalance+=amount
        print("your amount is successfully deposited")


kavya_sree=Bank_v2("kavya",289735766915,50000,6303,6303364884)


kavya_sree.withdraw()
kavya_sree.customer_details()
# kavya.withdraw()
# kavya.customer_details()

# kavya_sree.deposite()
# kavya_sree.customer_details()