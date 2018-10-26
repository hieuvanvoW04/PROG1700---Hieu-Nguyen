
#num_list=[]
#while loop that's alway True
    #Prompt the user to enter a number add 
    #that number to num_list print the current num_list


def whileTrue():
    
    num_list=[]

    bkeepgoing='y'

    while (bkeepgoing=='y'):
        n= int(input("Please enter a number "))
        num_list.append(n)
        print(num_list)
        bkeepgoing=input("Do you want to contunue adding to the list(y/n) ")
    
    
    maybe_num= input ("Please enter a number ")
    if(maybe_num.isnumeric()):
        num=int(maybe_num)
    else:
        print("not a number")
    while(not maybe_num.isnumeric()):
        maybe_numn= input("Please enter a number")
    num=int(maybe_num)
    
    l=len(num_list)
    s=sum(num_list)
    a=s/l
    print(l,s,a)

whileTrue()
