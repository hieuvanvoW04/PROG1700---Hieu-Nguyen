"""
Name..
: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"


def main():
# Calculate percentage of game won
  
    name= input("Enter name of the team: ")
    gamesWon= int(input("Enter number of game won: " ))
    gamesLost=int(input("Enter number of game lost: " ))
    percentageWon= round(100*(gamesWon)/(gamesWon+gamesLost),1)
    print(name, "won", str(percentageWon)+'%', "of their game.")



if __name__== "__main__":
    main()