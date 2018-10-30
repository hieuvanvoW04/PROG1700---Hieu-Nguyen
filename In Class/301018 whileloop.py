

def whileloop():

    input_is_valid=False
    while(not input_is_valid):
# Ask for input
        maybe_num=input("Please enter 4 number ")
        # kk=maybe_num.replace(".","")
        # kk.isnumeric
        # try float
        # not float
# Check is it valid
        if(maybe_num.isnumeric()):
# Set input_is_valid
            input_is_valid=True
            
    else:
        num=int(maybe_num)
        print(num)








whileloop()
