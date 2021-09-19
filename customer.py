import details as dt
from prettytable import PrettyTable

def main_function():
    print("--------Welcome to Customer --------")
    table = dt.get_pretty_table(["1.Check details","2.Transfer money"])
    print(table)
    choice = int(input("Enter Your Choice "))
    if choice == 1:
        check_details()
    elif choice == 2:
        transfer_money()
    else:
        print("Invalid Choice!")
        exit()
    main_function()

def check_details():
    acc_no = input("Enter Account number : ")
    result = dt.get_acc_by_no(acc_no)
    if len(result) == 0:
        print("Account Details Not Found")
    else:
        x = PrettyTable()
        x.field_names = ["Account number","Name","Address","Phone number","Amount"]
        x.add_row(result)
        print(x)

def transfer_money():
    acc=input("Enter your account number : ")
    amount=input("Enter the amount to transfer : ")
    dt.remove_money(amount,acc)
    acco=input("Enter the account number to transfer money : ")
    dt.add_money(amount,acco)
    print("Amount transferred successfully ")
    main_function()