"""
Function

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

#Let's use our function in a real situation.

cost_per_sqft=0.25
len=input("Length?")
wid=input("Width?")
cost=calcPaintCost(len,wid,cost_per_sqft)

#Params are either values or variables with values stored in them

print(f"cost is {cost}")