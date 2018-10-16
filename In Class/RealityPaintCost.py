"""
Function

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

#Let's use our function in a real situation.

cost_per_sqft=0.25
len=float(input("Length? "))
wid=float(input("Width? "))

def calcPaintCost(l,w,cost):
    area=l*w
    cost=(0.25)*area
    return(cost)
cost=calcPaintCost(len,wid,cost_per_sqft)

#Params are either values or variables with values stored in them

print(f"the cost is "+str(cost))             