"""

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

#1. Print name
#2. Input loan amount
#3. Input interest rate
#4. Input year
#5. Calculate i
#6. Calculate weekly loan payment amount

def main():
#Input

    print("Weekly Loan Payment Calculator")
    loanAmount=float(input("\nEnter the amount of loan: "))
    interestRate=float(input("Enter interest Rate (%): "))
    numberofYears=float(input("Enter the number of years: "))

#Process

    i=interestRate/5200
    weeklyPayment= (i/(1-((1+i)**(-(52*numberofYears)))))*loanAmount
    
#Output

    print("\nYour weekly payment will be: ${0:.2f}".format(weeklyPayment))
    


if __name__== "__main__":
    main()