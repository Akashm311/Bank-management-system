import banker as ba
import customer as ca
import details as dt


def main_function():
    print("--------Welcome to Bank --------")
    table = dt.get_pretty_table(["1.Banker","2.Customer"])
    print(table)
    choice = int(input("Enter Your Choice "))
    if choice == 1:
        ba.main_function()
    elif choice == 2:
        ca.main_function()
    else:
        print("Invalid Choice!")
        exit()
if __name__=="__main__":
    main_function()