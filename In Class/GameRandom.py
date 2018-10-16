"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"



import random

def main():

    number_to_guess= random.randint(1,10)

    current_guess=-1

    while(number_to_guess != current_guess):
        current_guess=int(input("Guess again(1-10): "))

        if current_guess<number_to_guess and current_guess > 1:
            print("Your guess is too low.")

        if current_guess< 1 and current_guess> 10:
            print("Not a good guess.")
            
    print("you got it")


main()