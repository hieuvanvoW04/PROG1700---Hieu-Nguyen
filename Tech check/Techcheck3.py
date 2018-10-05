"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():
    print("Valid letter grades that can be enter: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol")
    print("Calculate grade point value cannot exceed 4.0")
# Input possible grade are A, B, C, D
    Grade= input("Please enter a letter grade : ")
# Input modifiers plus (+), (-) or nothing
    Mod= input("Please enter a modifier (+, - or nothing): ")
# Process
    total=0
    if Grade=="A" and Mod=="+":
        total=total+4.0
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "A" and Mod=="":
        total = total + 4.0
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "A" and Mode=="-":
        total = total + 3.7
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "B" and Mode=="+":
        total = total + 3.3
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "B" and Mode=="":
        total = total + 3.0
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "B" and Mode=="-":
        total = total + 2.7
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "C" and Mode=="+":
        total = total + 2.3
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "C" and Mode=="":
        total = total + 2.0
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "C" and Mode=="-":
        total = total + 1.7
        print("The numeric value is {0:.1f}".format(total))
    elif Grade == "D":
         total = total + 1.0
         print("The numeric value is {0:.1f}".format(total))
    elif Grade=="F":
         total= total
         print("The numeric value is {0:.1f}".format(total))
    else:
         print("You enter an invalid letter grade.")


    
   

if __name__== "__main__":
    main()
