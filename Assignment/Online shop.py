"""

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

def main():
    country=input("where are you from? ")
    total=float(input("What are the order total: "))

    if country.lower()=="canada":
        province=input("Which province? (use Province Code) ")
        if province=="AB":
            total=total*1.05
        elif province=="ON"or province=="NB"or province=="NS":
            total=total*1.15
        else:
            total=total*1.11

    print("Your total bill is ${0:.2f}".format(total))

if __name__== "__main__":
    main()