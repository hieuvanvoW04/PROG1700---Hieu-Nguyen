"""
Function

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


square_feet_per_gallon = 150

print("Welcome to the Paint Shop!")
print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

def gallons_of_paint(x,y,z):
    return ((x*z*2)+(y*z*2))/150

gallonsPaint= gallons_of_paint(5,4,3)

print(f"You need (gallonsPaint)")




    