def tax(total):
    t = round((total * .06), 2)
    gTotal = (round(float(t + total), 2))
    print("The total cost of your items is: $" + str(total))
    print("Your tax comes up to: $" + str(t))
    print ("Your grand total comes up to: $" + str(gTotal))

purchase = 0

n = raw_input("Please input the prices of your items (enter 0 when you are done): ")
while float(n) != 0:
    purchase = float(n) + purchase
    print("Running total: $" + str(purchase))
    n = raw_input("Input another price: ")

tax(float(purchase))

