"""
Hello World
Python Push
Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

def main():
    country=input("where are you from? ")
    country= country.lower()
    total= input("What are the order total: ")

    if country=="CANADA":
        province=input("Which province ")
        if province=="AB":
            total=total+total*0.05
            print(total)
        elif province=="ON"or"NB"or"NS":
            total=total+total*0.15
            print(total)
        elif province!="AB"or"ON"or"NB"or"NS":
            total=total+total*0.11
            print(total)
    else country!="CANADA":
        print(total)


if __name__== "__main__":
    main()