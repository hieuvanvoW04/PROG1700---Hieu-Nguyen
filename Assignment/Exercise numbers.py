"""
Hello World
Python Push
Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

def main():
    deposit=input("Deposit:")
    deposit=float(deposit)
    if deposit>=100:
        print("toaster")
    else:
        print("mug")
print(":)")

if __name__== "__main__":
    main()