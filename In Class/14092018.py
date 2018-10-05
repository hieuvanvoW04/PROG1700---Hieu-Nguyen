"""
Hello World
Python Push
Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

import math

def main():

    #Input
    length=20
    width=10
    height=10

    #Process
    
    wall1= length*height*2
    wall2= width*height*2
    sqft= wall1+wall2
    gallon= sqft/150
    gallon== math.ceil(gallon)

    #Output
    displayGallon=str(gallon)
    displayGallon="You will need "<str(gallon)>" gallon"
    print(displayGallon)
    


if __name__== "__main__":
    main()
