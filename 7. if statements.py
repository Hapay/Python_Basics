is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Make sure to drink a lot of water!")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day :)")
print("Enjoy you day")

#CWICZENIE 1
#Price of a house is $1M. If the buyer has good credit, they have to put 10% of their property. Otherwise they
#need to put down 20%
price = 1000000
good_credit = True
#bad_credit = True
if good_credit:
    down_payment = 0.1 * price
    print("You have to put down 10%, so $", + down_payment)
else:
    down_payment = 0.2 * price
    print("You have to put down 20%, so $", +down_payment)
