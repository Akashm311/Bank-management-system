import getpass
import details as dt
from prettytable import PrettyTable

def main_function():
    print("-------Welcome Banker -------")
    username = input("Enter Your Username :")
    password = getpass.getpass("Enter Your Password :")
    if username == "admin" and password == "admin":
        print("---------Login Success---------")
        after_login()
    else:
        print("Sorry! Invalid Password or User name")
        main_function()
    
    # create account
def add_acc():
    acc_name=input("Enter the Account holder name : ")
    acc_no = input("Enter the Account number : ")
    address= input ("Enter the address : ")
    phone = input("Enter the Phone number : ")
    amount= input("Enter the Amount : ")
    result = dt.get_acc_by_no(acc_no)
    if len(result) > 0:
        print("Account  is Already Present Please Try Again!")
        add_acc()
    else:
        data =  acc_no + '|' +  acc_name + '|' + address + '|' + str(phone) + '|' + str(amount) + '$'
        f= open("account.txt","a")
        f.write(data)
        f.close()
        after_login()



def modify_acc():
    acc_no = input("Enter Account number : ")
    result = dt.get_acc_by_no(acc_no)
    if len(result) == 0:
        print("Account Details Not Found")
    else:
        x = PrettyTable()
        x.field_names = ["Account number","Name","Address","Phone number","Amount"]
        x.add_row(result)
        print(x)
        data=["1.Update Name ","2.Update Address","3.Update Phone number"]
        table = dt.get_pretty_table(data)
        print(table)
        ch = int(input("Enter Choice :"))
        if ch == 1:
            Name= input("Enter New Name :")
            result[1]=Name
        elif ch == 2:
            address = input("Enter New address : ")
            result[2]= address
        elif ch == 3:
            phone = input("Enter New Phone number : ")
            result[3]=phone
        f= open("account.txt","r")
        data = f.read()
        f.close()        
        res_lst = []
        li = data.split('$')
        li.pop()
        for l in li:
            li2 = l.split('|')
            if acc_no == li2[0]:
                res_lst.append('|'.join(result))
            else:
                res_lst.append(l)
        book = '$'.join(res_lst)+'$'
        file = open("account.txt","w")
        file.write(book)
        file.close()
        after_login()

def after_login():
    data=["1.Create Account ","2.Deposit Amount","3.Withdraw Amount","4.All Account Holder list","5.Close Account","6.Modify Account"]
    table = dt.get_pretty_table(data)
    print(table)
    choice=int(input("Enter your choice : "))
    if choice == 1:
        add_acc()
    elif choice == 2:
        deposit_money()
    elif choice == 3:
            withdraw_money()
    elif choice == 4:
        display()
    elif choice ==5:
        del_acc()
    elif choice==6:
        modify_acc()
    else:
        print("Invalid choice!")
        after_login()
    # delete account
                
def del_acc():
    acc_no = input("Enter Account number : ")
    result = dt.get_acc_by_no(acc_no)
    if len(result) == 0:
        print("Account Details Not Found")
    else:
        x = PrettyTable()
        x.field_names = ["Account number","Name","Address","Phone number","Amount"]
        x.add_row(result)
        print(x)
        f= open("account.txt","r")
        data = f.read()
        f.close()
        res_lst = []
        li = data.split('$')
        li.pop()
        for l in li:
            li2 = l.split('|')
            if acc_no == li2[0]:
                continue
            else:
                res_lst.append(l)
        book = '$'.join(res_lst)+'$'
        file = open("account.txt","w")
        file.write(book)
        file.close()
        after_login()

def deposit_money():
    acc=input("Enter the account number to deposit money: " )
    res= dt.get_acc_by_no(acc)
    if len(res) == 0:
        print("Details not found")
        after_login()
    else :
        amount=input("Enter the amount to be deposited : ")
        dt.add_money(amount,acc)
    print("Amount deposited successfully")
    after_login()

def withdraw_money():
    acc=input("Enter the account number to withdraw money: " )
    res= dt.get_acc_by_no(acc)
    if len(res) == 0:
        print("Details not found")
        after_login()
    else :
        amount=input("Enter the amount to be withdrawed  : ")
        dt.remove_money(amount,acc)
    print("Amount withdrawed successfully")
    after_login()

def display():
    x = PrettyTable()
    x.field_names = ["Account number","Name","Address","Phone number","Amount"]
    f= open("account.txt","r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        x.add_row(li2)
    print(x)
    after_login()
        
            
               
    

       



