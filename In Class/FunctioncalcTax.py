
def calculateTax(in_product_price,in_tax_rate):
   
    #Process
    product_total= in_product_price*(1+ in_tax_rate)
    #Output
    return product_total

def main():
    product_one_price=float(input("Enter product one price: "))
    product_one_total=calculateTax(product_one_price,0.15)
    print("The total price is ${0:.2f}.".format(product_one_total))

    product_two_price=float(input("Enter product two price: "))
    product_two_total=calculateTax(product_two_price,0.06)
    print("The total price is ${0:.2f}.".format(product_two_total))

    product_three_price=float(input("Enter product three price: "))
    product_three_total=calculateTax(product_three_price,0.15)
    print("The total price is ${0:.2f}.".format(product_three_total))

if __name__== "__main__":
    main()