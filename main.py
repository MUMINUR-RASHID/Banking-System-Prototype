from user import Users
from bank import Bank
from admin import Admin


def main():
    print("Here Is Main")

    bank=Bank("MMR BANK","MYMENSINGH")

    check=True

    while check:
        print("\n1. Press 1 For Admin.")
        print("2. Press 2 for User.")
        print("3. Press Any Key For Exit")
        try:
            chose = int(input("Enter Your Choice: "))
        except ValueError:
            print("Exiting...")
            break
        if chose==1:
            check1=True

            while check1:

                print("\n1. Press 1 For Create Account.")
                print("2. Press 2 For Delete User Account.")
                print("3. Press 3 For See User List")
                print("4. Press 4 For Check Bank Total Balance.")
                print("5. Press 5 For Check Total Loan Balance.")
                print("6. Press 6 For Control Bank Loan Feature")
                print("7. Press Any Key For Exit")
                try:
                    choice = int(input("Enter Your Choice: "))
                except ValueError:
                    print("Exiting...")
                    break
                if choice==1:
                    name=input("Enter Your Name: ")  
                    email=input("Enter Your email: ") 
                    address=input("Enter Your address: ")
                    position=input("Enter Your Designation: ")
                    staf1=Admin(name,email,address,position)
                    bank.add_staf(staf1)
                    print(f"Your Account Number Is {staf1.Id_num}. Please Remember It for Further Use")

                elif choice==2:
                    try:
                        staf_ac=input("Enter Your Id: ")
                    except ValueError:
                        print("Exiting...")
                        break
                    if staf_ac in bank.stafs:
                        acc_num=input("Enter User Account Number: ")
                        bank.remove_acc(acc_num)

                    else:
                        print("You Are Not Illigible For This Operation.")

                elif choice==3:
                    staf_ac=input("Enter Your Id: ")
                    if staf_ac in bank.stafs:
                        print(f"User Account Numbers: ")
                        print(list(bank.users.keys()))

                    else:
                        print("You Are Not Illigible For This Operation.")

                elif choice==4:
                    try:
                        staf_ac=input("Enter Your Id: ")
                    except ValueError:
                        print("Exiting...")
                        break
                    if staf_ac in bank.stafs:
                        print(f"Bank Total Balance Is: {bank.add_balance} Taka")

                    else:
                        print("You Are Not Illigible For This Operation.")
                elif choice==5:
                    
                    try:
                        staf_ac=input("Enter Your Id: ")
                    except ValueError:
                        print("Exiting...")
                        break
                    if staf_ac in bank.stafs:
                        print(f"Bank Total Loan Is: {bank.add_loan} Taka")

                    else:
                        print("You Are Not Illigible For This Operation.")
                elif choice==6:
                    try:
                        staf_ac=input("Enter Your Id: ")
                    except ValueError:
                        print("Exiting...")
                        break
                    if staf_ac in bank.stafs:
                        choice=None
                        while choice is None:
                            choice=int(input("Press 1 For Loan On and 2 For Loan Off"))
                        if choice==1:
                            bank.loan_available=True
                        elif choice==2:
                            bank.loan_available=False
                        else:
                            print("Invalid Keyword")
                            choice=None

                    else:
                        print("You Are Not Illigible For This Operation.")
                else:
                    check1=False
        elif chose==2:
            check2=True

            while check2:

                print("\n1. Press 1 For Create Account.")
                print("2. Press 2 For Deposit.")
                print("3. Press 3 For Withdraw")
                print("4. Press 4 For Check Balance.")
                print("5. Press 5 For Check Transection History.")
                print("6. Press 6 For Take Loan")
                print("7. Press 7 For Transfer Balance.")
                print("8. Press Any Key For Exit")
                try:
                    choice=int(input("Enter Your Choice: "))
                except ValueError:
                    print("Exiting...")
                    break
                
                if choice==1:
                    
                    name=input("Enter Your Name: ")
                        
                    email=input("Enter Your email: ")
                        
                    address=input("Enter Your address: ")
                    acc_type=None
                    while acc_type is None:
                        try:
                            ch=int(input("Enter Your Account Type. press 1 for Savings, press 2 for Current "))
                        except ValueError:
                            print("Exiting...")
                            break
                    
                        
                        if ch==1:
                            acc_type="Savings"
                        elif ch==2:
                            acc_type="Current"
                        else:
                            print("You chose wrong keyword. Please chose again")
                            ch=None
                            
                    user1=Users(name,email,address,acc_type)
                    bank.add_user(user1)
                    print(f"Your Account Number Is {user1.ac_num}. Please Remember It for Further Use")

                elif choice==2:
                    acc_num=input("Enter Your Account Number: ")
                    amount=int(input("Enter The amount of deposit: "))
                    bank.deposit(acc_num,amount)

                elif choice==3:
                    acc_num=input("Enter Your Account Number: ")
                    amount=int(input("Enter The amount: "))
                    bank.withdraw(acc_num,amount)
                elif choice==4:
                    acc_num=input("Enter Your Account Number: ")
                    bank.check_user_balance(acc_num)
                elif choice==5:
                    acc_num=input("Enter Acount Number: ")
                    print(bank.users[acc_num].trans_history)
                elif choice==6:
                    acc_num=input("Enter Your Account Number: ")
                    amount=int(input("Enter Loan Amount: "))
                    bank.give_loan(acc_num,amount)
                elif choice==7:
                    user_acc_num=input("Enter Your Account Number: ")
                    target_acc_num=input("Enter Target Account Number: ")
                    amount=int(input("Enter Amount Of Money: "))
                    bank.transfer_balance(user_acc_num,target_acc_num,amount)
                else:
                    check2=False

        else:
            check=False








if __name__=="__main__":
    main()