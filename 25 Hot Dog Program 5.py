# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. def price_conversion(price):

    hotdogCost = 0.0

    if typeDog == "Hot Dog":
        hotdogCost = 3.50

    if typeDog == "Chili Dog":
        hotdogCost = 4.50

    if cheeseTopping == "Yes":
        hotdogCost = hotdogCost + 0.50

    if pepperTopping == "Yes":
        hotdogCost = hotdogCost + 0.75

    if onionTopping == "Yes":
        hotdogCost = hotdogCost + 1

    return hotdogCost



if __name__ == '__main__':

    price = 0.00
    hotdogCost = 0.0

    typeDog = str(input('Would you like a Hot Dog or a Chili Dog?: '))
    cheeseTopping = str(input("Would you like Cheese?:"))
    pepperTopping = str(input("Would you like Peppers?:"))
    onionTopping = str(input("Would you like Grilled Onions?:"))

    Total = price_conversion(price)
    Tax = Total * 0.07
    GrandTotal = Tax + Total
    print('Total: $', format(Total, '.2f'))
    print('Tax: $', format(Tax,  '.2f'))
    print('GrandTotal: $', format(GrandTotal,  '.2f'))

#Caleb Saari 2/6/25 Hot Dog
