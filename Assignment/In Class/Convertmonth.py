"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():
# Convert a number of months to years and months.

    numberofMonths= int(input("Enter number of months: "))
    years= numberofMonths//12
    months=numberofMonths % 12
    print(numberofMonths, "months is", years, "years and", months, "months.")
  


if __name__== "__main__":
    main()