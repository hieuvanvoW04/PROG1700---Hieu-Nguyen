

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

function

# def getValidNum(num_to_check):
#         nc=num_to_check.replace(".","")
#         while(not num_to_check.isnumeric):
#                 num_to_check=input("Not a number. Please try again.")
#                 nc=num_to_check.replace(".","")
#         else:
#                 num_to_check=int(num_to_check)

#         return(num_to_check)

# first_int=input("Give me first #")
# first_int=getValidNum(first_int)



whileloop()
