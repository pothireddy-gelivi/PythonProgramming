class IncorrectPinError(BaseException):
    def __init__(self,msg):
        self.msg=msg

class InsufficientBalanceError(BaseException):
    def __init__(self,msg):
        self.msg=msg

class Bank:
    bank_name="sbi"
    def __init__(self,cn,cb,cp):
        self.cname=cn
        self.cbalance=cb
        self.cpin=cp
    
    def Withdraw(self):
        pin=int(input("Enter your pin number"))
        if self.cpin!=pin:
            raise IncorrectPinError("sorry you enter wrong pin")
        else:
            amount=int(input("enter the amount"))
            if amount>self.cbalance:
                raise InsufficientBalanceError("you dont have that much of amount")
            else:
                self.cbalance-=amount
                print("withdraw succesful")
                print("Available balance is",self.cbalance)
reddy=Bank("pothireddy",12000,143)
print("Bank welcomes you")
try:
    reddy.Withdraw()
except IncorrectPinError as IPE:
    print(IPE)
except InsufficientBalanceError as IBE:
    print(IBE)
print("thank you for banking")

