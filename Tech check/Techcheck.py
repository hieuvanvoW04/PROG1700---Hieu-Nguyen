"""
Hello World
Python Push
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():

# Input

    OriginalBill = float( input( "Please enter the original bill: " ) )


# Process
    tip = 0.2 * OriginalBill
    tax = 0.15 * OriginalBill
    Totalamount = OriginalBill + tip + tax

# Output
    print( "OriginalBill: $"+format( OriginalBill, ",.2f"), "tip: $"+format( tip, ",.2f"),"tax: $"+format( tax, ",.2f"), \
    "Totalamount: $" + format( Totalamount, ",.2f"), sep = "\n")


if __name__== "__main__":
    main()
