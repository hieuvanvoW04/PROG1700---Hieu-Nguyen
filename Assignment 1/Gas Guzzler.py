"""

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

#1. Print program name
#2. Input the odometer showed in Halifax: 45,978 kilometers1
#3. Input the odometer showed in Sydney: 45,067  kilometers2
#2. Input the liters the tank took: 39.7 liters1
#2. Input the Cost for the kilometers I have travelled: $56 cost_travelled
#3. Calcualte kilometers did I travel: kilometers1-kilometers2 kilo
#4. Convert Kilometers to miles: (kilometers1-kilometers2)*5/8
#4. Convert Liters to Gallons of gas: liters1*0.264
#3. Calcualte miles per gallon did I get: miles/gallons_of_gas
#3. Calcualte a kilometer did it cost me
#5. Print Result

def main():
#Input

    print("Gas Guzzler")
    kilometers1=float(input("\nEnter number of kilometers1: "))
    kilometers2=float(input("\nEnter number of kilometers2: "))    
    liters=float(input("\nEnter number of liters: "))
    cost=float(input("\nEnter the Cost: "))
 
#Process
    kilometers=kilometers1-kilometers2
    miles=kilometers*5/8
    gallons_of_gas=liters*0.24
    miles_per_gallons=miles/gallons_of_gas
    cost_per_kilometer=cost/(kilometers1-kilometers2)
    
#Output

    print(f"\nThe kilometers did I travel {kilometers}")
    print(f"The miles did I travel {miles}")
    print(f"The gallons of gas did I use {gallons_of_gas}")
    print(f"The miles miles per gallon did I get {miles_per_gallons}")
    print(f"A kilometer did it cost me ${cost_per_kilometer}")


if __name__== "__main__":
    main()