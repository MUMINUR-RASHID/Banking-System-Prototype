from datetime import datetime
#from user import Users
class Bank:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.users={}
        self.stafs={}
        self.__balance=0
        self.__loan=0
        self.loan_available=True

    
    def add_staf(self,staf):
        Id_no=self.set_ac_num(staf)
        staf.Id_num=Id_no
        self.stafs[Id_no]=staf


    
    def add_user(self,user):
        ac_no=self.set_ac_num(user)
        user.ac_num=ac_no
        self.users[ac_no]=user


    
    def set_ac_num(self,user):
        date=datetime.now()
        year=date.year
        month=date.month
        day=date.day
        hour=date.hour
        minite=date.minute
        second=date.second
        micro=date.microsecond
        return f"{year}-{month}{day}-{hour}{minite}{second}-{micro}"
    
    def deposit(self,acc_num,amount):
        if acc_num in self.users:
            self.users[acc_num].acc_balance=amount
            self.add_balance=amount
            date=datetime.now()
            self.users[acc_num].add_trans_history(f"Time:{date}  Diposit: {amount} Taka")
            self.check_user_balance(acc_num)
        else:
            print("Invalid Account Number.")

    @property
    def add_balance(self):
        return self.__balance
    @add_balance.setter
    def add_balance(self,amount):
        self.__balance+=amount

    
    def withdraw(self,acc_num,amount):
        if acc_num in self.users:
            if amount<=self.add_balance:
                check=self.users[acc_num].check_balance(amount)
                if check:
                    bal=amount*-1
                    self.users[acc_num].acc_balance=bal
                    self.add_balance=bal
                    self.check_user_balance(acc_num)
                    print(f"Plese Take Your {amount} Taka")
                    date=datetime.now()
                    self.users[acc_num].add_trans_history(f"Time:{date}  Withdraw: {amount} Taka")


                else:
                    print("Withdrawal amount exceeded")
            else:
                print("The Bank Is Bankrupt")

        else:
            print("Invalid Account Number.")

    def check_user_balance(self,acc_num):
        print(f"Your Current Account Balance is {self.users[acc_num].acc_balance}")

    def give_loan(self,acc_num,amount):
        if acc_num in self.users:
            if amount<=self.add_balance:
                check=self.loan_available
                if check:
                    chln=self.users[acc_num].check_loan()
                    if chln:
                        bal=-1*amount
                        self.add_balance=bal
                        self.add_loan=amount
                        self.users[acc_num].take_loan=amount
                        print(f"Plese Take Your Loan {amount} Taka")
                        date=datetime.now()
                        self.users[acc_num].add_trans_history(f"Time:{date}  Take Loan: {amount} Taka")
                    else:
                        print("You Are Not Iligible For Taking More Loan.")


                else:
                    print("Bank Not Giving Loan Now")
            else:
                print("The Bank Has Not Enough Money")

        else:
            print("Invalid Account Number.")


    def transfer_balance(self,user_acc_num,target_acc_num,amount):
        if user_acc_num in self.users:
            if target_acc_num in self.users:
                check=self.users[user_acc_num].check_balance(amount)
                if check:
                    bal=-1*amount
                    self.users[target_acc_num].acc_balance=amount
                    self.users[user_acc_num].acc_balance=bal
                    self.check_user_balance(user_acc_num)
                    date=datetime.now()
                    self.users[user_acc_num].add_trans_history(f"Time:{date}  Transfer: {amount} Taka To {target_acc_num}")
                else:
                    print("Not Enough Money In Your Account")
            else:
                print("Target Account does not exist")

        else:
            print("Invalid User Account Number")



    def remove_acc(self,acc_num):
        val=self.users.pop(acc_num,'0')
        if val=='0':
            print(f"{acc_num} Not In List")
        else:
            print(f"{acc_num} Removed From The List.")

        
    @property
    def add_loan(self):
        return self.__loan
    @add_loan.setter
    def add_loan(self,amount):
        self.__loan+=amount


   