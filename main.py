#CSE1021 VITyarthi Flipped course Project
# ATM Managemet System
#Source code
usernames = ["Raj", "Kritika", "Nidish"]

username1="Raj"
PIN1=121007
balance1=150000

username2="Anmol"
PIN2=123456
balance2=120000

username3="Nidish"
PIN3=141926
balance3=900000

Username=input("Enter username: ") #taking input

usernames = ["Raj", "Kritika", "Nidish"]
pin=[121007,123456,141926]

if Username not in usernames:
    print("Invalid Username")
    exit()
PIN=int(input("Enter PIN:"))

if PIN not in pin:
    print("invalid pin")
    exit()
    
if Username==username1:  #shifting into diffrent user
    PIN=PIN1
    balance=balance1
elif Username==username2:
    PIN=PIN2
    balance=balance2

elif Username==username3:
    PIN=PIN3
    balance=balance3

else:
    print("invalid PIN or Username")

print('********ATM MENU********')  #creating menu
print('select 1 to check balance')
print('select 2 to withdraw money')
print('select 3 to Deposite money')
print('select 4 to change PIN')
print('select 5 to EXIT')

ch=0

while ch != 5:

    ch=int(input('enter choice:'))
    
    if ch==1:                                     #balance showing
        print('Current balance:',balance)
    
    elif ch==2:                                            #taking out money
        wm=float(input('Enter amount to withdraw: '))
        nb=balance-wm                                     
        if nb>0:                                            # verify input
            print("money succesfuly withdrawed",wm)
            print('Remaining balance',nb)
        else:
            print('Insufficent Balance')
    
    elif ch==3:                                            #money added
        dp=float(input('Enter amount to deposite:'))
        if dp>0:                                            #verify input
            nb1=balance+dp
            print(dp,'money succesfully deposited')
            print('New balance',nb1)
        else:
            print('invalid input')
    
    elif ch==4:                                            #change pin
        new_PIN=int(input("Enter new PIN: "))
        PIN=new_PIN
        print("PIN is succesfully changed")
    
    elif ch==5:                                            #ending program
        print("Thanks for using machine")
        exit()
    else:
        print('invalid choice')


    

