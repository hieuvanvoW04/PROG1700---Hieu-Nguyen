"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main(): 
 
 # input 
    grade = input("Please enter a letter grade: ")
    grade = grade.upper()
    modifier = input("Please enter a modifier(+,- or nothing): ")

    # process

    if grade == "A":
        value = 4
    elif grade == "B":
        value = 3
    elif grade == "C":
        value = 2   
    elif grade == "D":
        value = 1          
    elif grade == "F":
        value = 0  
    else:
        value = 0    # Meaningless assingment, to prevent error
                     # If grade is not A,B,C,D,F / value dosen't need 

    modifyingnumber = 0.3
    
    if modifier == "+":
        if grade != "A" and grade != "F":
            totalvalue = value + modifyingnumber
        else:
            totalvalue = value    
    elif modifier == "-":
        if grade != "F":
            totalvalue = value - modifyingnumber
        else: 
            totalvalue = value
    else:
        totalvalue = value        

    # output
    if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "F":
        display = "The numeric value is: {:.1f}". format(totalvalue)
        print(display)         
    else:
        print("You entered an invalid letter grade.")   


if __name__== "__main__":
    main()