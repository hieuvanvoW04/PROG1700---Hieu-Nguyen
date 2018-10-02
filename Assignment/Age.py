"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():
    age= input("Age?")
    isvalid= checkID()
    if age>=19 and isvalid==True:
        print("Approved")
        approve= True
    else:
        print("Not Approved")
        approve= False
print("Approved:"+ approve)

    
if __name__== "__main__":
    main()