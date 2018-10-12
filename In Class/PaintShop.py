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

length = float(input("\nEnter the length of the room, in feet: "))
width = float(input("Enter the width of the room, in feet: "))
height = float(input("Enter the height of the room, in feet: "))

totalArea= calcualteArea(length,width,heigh)

gallons_of_paint= calculateGallons(totalArea,square_feet_per_gallon)

def calcualteArea(length,width,heigh):
    return ((length * height * 2) + (width * height * 2))

def calculateGallons(totalArea,square_feet_per_gallon):
    return math.ceil(totalArea/square_feet_per_gallon)


print(f"\nThe total wall area of your room is "+ str(totalArea)+ " square feet.")
print(f"You need "+ str(calcualteArea)+ " gallon(s) of paint. \n\nHappy Painting!")




    