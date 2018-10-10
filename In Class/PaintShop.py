"""
Function

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


import math

square_feet_per_gallon = 150

print("Welcome to the Paint Shop!")
print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

x=float(input("\nEnter the length of the room, in feet: "))
y=float(input("Enter the width of the room, in feet: "))
z=float(input("Enter the height of the room, in feet: "))

def CalculatetotalArea(x,y,z):
    
    return (x*z*2)+(y*z*2)

totalArea= CalculatetotalArea(x,y,z)

def gallons_of_paint():

    gallons_of_paint= math.ceil(totalArea/square_feet_per_gallon)

print(f"The total wall area of your room is (totalArea)")
print(f"You need (gallons_of_paint)")




    