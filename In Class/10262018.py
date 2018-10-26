
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
    
    print(len(num_list))
    print(sum(num_list))

whileTrue()
