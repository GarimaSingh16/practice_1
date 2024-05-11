d={}
def add():
        a=input("\t Enter product : ")
        b=int(input("\t Enter expenditure : "))
        if a in d.keys():
                x=input("===== ITEM ALREADY EXISTS ===== \n1. Add its expense \n2. Don't add it\n  Enter your choice : ")
                if x=='1':
                        d[a]=d[a]+b
                        print("\t---- Expense added successfully ----")
                elif x=='2':
                        print("\t---- Expense is not added ----")
                else:
                        print("\t---- Invalid choice ----")
        else:
                d[a]=b
                print("\t---- Item added successfully ----")
def remove():
        if d=={}:
                print("\t==== No item exists ====")
        else:
                a=input("\t Enter product : ")
                if a in d.keys():
                        del(d[a])
                        print("\t---- removed successfully----")
                else:
                        print("\t---- Item does not exist ----")
def change():
        if d=={}:
                print("\t==== No item exists ====")
        else:
                a=input("\t Enter product : ")
                b=int(input("\t Enter new expenditure : "))
                if a in d.keys():
                        d[a]=b
                        print("\t---- Expense changed successfully ----")
                else:
                        print("\t---- Item does not exist ----")

def edit():
        while True:
            x=input("1. Add \n2. Remove \n3. Change \n Any key to stop : \n  Enter your choice : " )
            if x=='1':
                add()
            elif x=='2':
                remove()
            elif x=='3':
                change()
            else:
                    break
        
def show():
    t_exp=0
    if d=={}:
        print("===== NO ITEM IS ADDED =====")
    else:
        for i in d.items():
            print(f"\t======= ITEMS ====== \n\t    {i[0]}  :  {i[1]}")
            t_exp+=d[i[0]]  
        print("\t==== TOTAL EXPENSES====  \n\t\t ",t_exp) 

while(True):
        y=(input("1. Add , Remove or Change \n2. Show items \n3. Stop :\n  Enter your choice :  "))
        if y=='1':
            edit()
        elif y=='2':
            show()
        elif y=='3':
            break
        else:
            print("\t---- Invalid choice ----")
