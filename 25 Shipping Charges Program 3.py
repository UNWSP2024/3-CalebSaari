def weight_conversion(weight):
    # Calculate the shipping charge.
    shippingCost = 0.0
    ######################
    if weight <= 2:
        shippingCost = weight * 1.50
    if weight > 2 and weight <= 6:
        shippingCost = weight * 3.00
    if weight > 6 and weight <= 10:
        shippingCost = weight * 4.00
    elif weight > 10:
        shippingCost = weight * 4.75
    ######################

    return shippingCost


if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print('Shipping charge: $', format(shippingCost, '.2f'))

#Caleb Saari 2/6/25 Shipping Charges