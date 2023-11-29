# Question 16(a)
# Student Name:
#This program is a simple ordering system
staff_name=input('please enter your username')
print("Welcome to the new online ordering system.\n")

total_cost=0
item_count=int(input('enter number of items'))

if item_count<1:
    print('Invalid option')
else:
    for i in range(item_count):
        price_of_item=float(input("Enter the price of item {}".format(i+1)+" : € "))
        total_cost+=price_of_item

    print('The member of staff who processed your order was: ',staff_name)
    print("You entered",item_count,"items and the total is €",total_cost)
      
    balance=int(input('What is the customers current account balance € '))
    rem_balance=balance-total_cost

    if rem_balance<0:
        print('The customer does not have enough credit in their account, they still owe: € ',total_cost-balance)
    else:
        print('Your remaining balance: € ',rem_balance)



