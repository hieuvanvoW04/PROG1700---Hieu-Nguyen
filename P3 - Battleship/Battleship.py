
def main():

    objFile = open("map.txt")
    targetGrid = []

    for row in objFile:
        row = row.replace("\n","")
        rowAsList = row.split(",")
        targetGrid.append(rowAsList)

        # z=[0,0,0,...]
        # hitGrid=[z,z,z,z...]
        # InGrid[1][1]=1
    # TOTAL_SHIP_POSITIONS=7
    # SHIP_POSITIONS_LEFT=TOTAL_SHIP_POSITIONS
    # while(num_of_turns<30):
    #     loop herre untill shot is new location
    #     xy=getgotshotfromuser()

    #     if(washit(xy)):
    #             shotFired[x][y]=1
    #             print("you gor a hit")
    #             SHIP_POSITIONS_LEFT=1
    #     else(notwashit(xy)):
    #             shotFired[x][y]=-1
    #             print("you missed")
    #     if(SHIP_POSITIONS_LEFT=0)
    #             print("end game")

    # row = input("what row")
    # col = input("what col")
    # listCoords=cor.split(",")

    # print(listCoords[0])
    # print(listCoords[1])

    # if(1):
    #     print("hit")
    # else
    #     print("you missed")

    print(targetGrid)
















main()