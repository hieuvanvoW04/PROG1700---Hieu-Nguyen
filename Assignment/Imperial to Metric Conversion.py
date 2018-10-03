"""

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

#1. Print program name
#2. Input tons, stones, pounds and ounces amount
#3. Convert amount into kilos
#4. Convert rest amount to grams
#5. Print Result

def main():
#Input

    print("Imperial to Metric Conversion")
    tons=float(input("\nEnter number of tons: "))
    Stones=float(input("Enter number of stone: "))
    ounces=float(input("Enter number of ounces: "))

#Process

    totalOunces=tons*35840+Stones*224+pounds*16+ounces
    totalKilos=totalOunces/35.274
    metricTons=int(totalKilos/1000)
    kilo=int(totalKilos-metricTons*1000)
    gram=float()
    
#Output

    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment))
    


if __name__== "__main__":
    main()