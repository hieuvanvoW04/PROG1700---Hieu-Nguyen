
def HighestCommonDivisor():

   
    def getHighestCommonDivisor(x,y):
        while y!=0:
            (x,y)=(y, x % y)
        return x
    
    def getValidNum1(num1_to_check):
            nc1=num1_to_check.replace(".","")
            while(not num1_to_check.isnumeric):
                    num1_to_check=input("ERROR!. Enter a valid first number.")
                    nc1=num1_to_check.replace(".","")
            else:
                    num1_to_check=int(num1_to_check)

            return(num1_to_check)
    
    def getValidNum2(num2_to_check):
            nc2=num2_to_check.replace(".","")
            while(not num2_to_check.isnumeric):
                    num2_to_check=input("ERROR!. Enter a valid second number.")
                    nc2=num2_to_check.replace(".","")
            else:
                    num2_to_check=int(num2_to_check)

            return(num2_to_check)

    bkeepgoing='y'
    while (bkeepgoing=='y'):
        first_int=input("Enter the first number ")
        first_int=getValidNum1(first_int)
        second_int=input("Enter the second number ")
        second_int=getValidNum2(second_int)
    
        CommonDvisor= getHighestCommonDivisor(first_int,second_int)

        print(f"The Highest Common Divisor of {first_int} and {second_int} is: {CommonDvisor} ")
        bkeepgoing=input("Would you like to try again? (y/n) ")
    else:
        print("Thank you for using the HCD program.")
        


HighestCommonDivisor()