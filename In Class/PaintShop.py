"""
Function

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


square_feet_per_gallon = 150

print("Welcome to the Paint Shop!")
print("This program will help you calculate how many cans of paint you need to buy, based on the dimensions of your room.")

length = float(input("\nEnter the length of the room, in feet: "))
width = float(input("Enter the width of the room, in feet: "))
height = float(input("Enter the height of the room, in feet: "))


def gallons_of_paint(length,width,height):
    return ((length*height*2)+(width*height*2))/150

gallonsPaint= gallons_of_paint(length,width,height)

print(f"You need (gallonsPaint)")




    