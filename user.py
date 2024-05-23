class Users:
    def __init__(self, name, email, address, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.ac_type = acc_type
        self.__ac_num = None
        self.__acc_balance = 0
        self.__take_loan = 2
        self.trans_history=[]
        self.loan_balance=0

    @property
    def ac_num(self):
        return self.__ac_num
    
    @ac_num.setter
    def ac_num(self, value):
        self.__ac_num = value

    @property
    def acc_balance(self):
        return self.__acc_balance
    
    @acc_balance.setter
    def acc_balance(self, value):
        self.__acc_balance += value




    
    @property
    def take_loan(self):
        return self.__take_loan

    @take_loan.setter
    def take_loan(self, amount):
        if self.__take_loan > 0:
            self.__take_loan -= 1
            self.loan_balance += amount
            return True
        else:
            print("Sorry! You can't Take Loan")
            return False

    def check_balance(self, amount):
        return self.__acc_balance >= amount

    def add_balance(self, amount):
        self.__acc_balance += amount

    def add_trans_history(self,description):
        self.trans_history.append(description)

    def check_loan(self):
        return self.__take_loan>0
