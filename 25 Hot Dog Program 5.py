def price_conversion(price):

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