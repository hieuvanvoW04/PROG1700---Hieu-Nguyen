"""

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

#1. Print name
#2. Input customer name
#3. Input distance delivery
#4. Input cost purchase
#5. Calculate delivery cost
#6. Calculate purchase cost
#7. Calculate total cost
#8. Print
def main():
#Input
    print("Hipster's Local Vinyl Record- Customer Invoice")
    customerName=input("\nCustomer's Name: ")
    distance=float(input("Distance for Delivery (in kilimeters): "))
    costofRecords=float(input("Cost of record purchased: "))
#Process
    deliveryCharge=int(15)
    saleTax=float(0.14)

    deliveryCost= distance*deliveryCharge
    purchaseCost=costofRecords*saleTax+costofRecords
    totalCost= deliveryCost+purchaseCost

#Output
    print("\nPurchase summary for "+customerName.title())
    print("Delivery Cost: \t${0:.2f}".format(deliveryCost)+"\nPurchase Cost: \t${0:.2f}".format(purchaseCost)+"\nTotal Cost\t: \t${0:.2f}".format(totalCost))


if __name__== "__main__":
    main()