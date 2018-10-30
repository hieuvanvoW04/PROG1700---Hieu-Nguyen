
def Modular():


    def getValidNum(num_to_check):
            nc=num_to_check.replace(".","")
            while(not num_to_check.isnumeric):
                    num_to_check=input("Not a number. Please try again.")
                    nc=num_to_check.replace(".","")
            else:
                    num_to_check=int(num_to_check)

            return(num_to_check)

# 1.set n=number to test
# 2.try dividing n by all number less than n
# print the number that divide evenly(have )
    n=182
    for d in range(1,n+1):
       if(n%d==0):
           print(d)
           factor.append(d) 
Modular()