"""
Hello World
Python Push
Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

def main():
    item= "ketchup"
    reg=1.80
    discount=0.27
    price=reg-reg*discount
    temp="${0:.2f} is the sale price of {1}"
    disp=temp.format(price,item)
    print(disp)

if __name__== "__main__":
    main()