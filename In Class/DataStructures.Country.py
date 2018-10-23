
# countries.append("nz")
# c=countries[index]
# countries[i]= "Berlins"
# if("nz" in countries)
# countries.insert(index,"ce")
# countries.pop(index)
# r=nap(func,list)
    #print(list(r))
# countries.xvssdf??("canada")
# countries[1:3]= ["nz","bulgary"]
    #del(countries[3])
def main():

    country=input("What country should I add to my list: ")
    countries=["canada","australia","combodia","laos","china"]
  
    while (country in countries ):
        print("already in list")
        country=input("try another one")

    countries.append(country)

    print(countries)

if __name__== "__main__":
    main()  