from prettytable import PrettyTable
import banker as ba


def get_acc_by_no(acc_no):
    f = open("account.txt","r")
    data = f.read()
    f.close()
    li = data.split('$')
    li.pop()
    for l in li:
        li2 = l.split('|')
        if acc_no == li2[0]:
            return li2
    return []


def get_pretty_table(li):
    table = PrettyTable()
    table.field_names = ["Enter Your Choice"]
    for i in li:
        table.add_row([i])
    return table

def add_money(amount,acc):
    f=open("account.txt","r")
    data =f.read()
    f.close()
    resl=[]
    li= data.split('$')
    li.pop()
    for l in li:
        li1 = l.split('|')
        if li1[0] == acc:
            li1[4] = str(int(li1[4])+int(amount))
            resl.append('|'.join(li1))
        else:
            resl.append(l)
    result='$'.join(resl)+'$'
    f = open("account.txt","w")
    f.write(result)
    f.close()
    

def remove_money(amount,acc):
    
    f=open("account.txt","r")
    data =f.read()
    f.close()
    resl=[]
    li= data.split('$')
    li.pop()
    for l in li:
        li1 = l.split('|')
        if int(li1[4])< int(amount):
            print("In sufficient balance! ") 
            resl.append('|'.join(li1))
        elif li1[0] == acc:
            li1[4] = str(int(li1[4])-int(amount))
            resl.append('|'.join(li1))
        else:
            resl.append(l)
    result='$'.join(resl)+'$'
    f = open("account.txt","w")
    f.write(result)
    f.close()
   
