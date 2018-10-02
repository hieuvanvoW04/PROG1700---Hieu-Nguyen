"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():

# Input

    paymentRate=float(input("what is your hourly payment?:"))
    totalHour=int(input("How many hour did you work?: "))

# Process
    if totalHour>40:
        totalPayment=paymentRate*(40)+paymentRate*(totalHour-40)*1.5
    else:
        totalPayment=totalHour*paymentRate
# Output
    print("Congratulation you have earned ${0:.2f}".format(totalPayment))

if __name__== "__main__":
    main()
