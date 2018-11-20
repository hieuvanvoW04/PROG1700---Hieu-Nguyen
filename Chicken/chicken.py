def main():

# Ask the user for 3 choices construct The choices list from their answers.
    choiceList=[]
    for i in range(1,4):
        choice=input("Next choice please ")
        choiceList.append(choice)
    print(choiceList)

    
# Create a text file called template.txt-> and put strTemplate in it    strTemplate= "The _1_ jumped over the _2_ to get to their _3_"
    objFile = open("template.txt")
    strTemplate = objFile.read()
# Popolate strTemplate variable by reading from template.txt 
# Do the for loop replace thing
    for i in range(0,3):
        strPH = ""
        strPH += "_"
        strPH = str(i+1)
        strPH += "_"
        print(strPH)
    strTemplate=strTemplate.replace(strPH, choiceList[i])

    print(strTemplate)

main()


# strMsg="Pick from this list: \n"
# loop_counter=1
# for color in colorList:
#     strMsg += str(loop_counter)
#     strMsg += ")"
#     strMsg += color
#     loop_counter += 1

# strMsg += "Choose(1-3)"
# choice= input(strMsg)