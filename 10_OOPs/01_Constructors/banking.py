import random
class banking:
    def __init__(self,location,balance):
        #self.name=input("Enter Name: ")
        self.bankname = "SBI"
        self.location = location
        self.balance = balance
        self.email = input("Enter User Name: ")
        self.password = input("Enter Password: ")
        self.otp = random.randrange(1111,9999)


    def withdraw(self):
        self.amount = int(input("Enter Withdraw Amount: "))
        print(self.amount, "Debited from your account")
        self.balance = self.balance - self.amount
        print("Remaining Balance is : ", self.balance)

    def deposit(self):
        self.amount = int(input("Enter deposit Amount: "))
        print(self.amount,"Credited from your account")
        self.balance = self.balance + self.amount
        print("Remaining Balance is : ", self.balance)

    def otpgen(self):
        print("OTP of you transaction is",self.otp)

    def authenticate(self):
        otp=int(input("Enter OTP: "))
        if self.email == "pravink@sbi.com" and self.password == "abc123" and otp==self.otp:

            s1.withdraw()
            s1.deposit()
        else:
            print("please enter correct user name or password or OTP")


s1 = banking("Thane",100000)
s1.otpgen()
s1.authenticate()





