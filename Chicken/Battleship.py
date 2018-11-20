
objFile = open("odd.csv")
dictTeams={}
for line in objFile:
    line=line.replace("\n","")
    listLineContent = line.split(",")
    teamName = listLineContent[0]
    teamMembers = listLineContent[1:]
    dictTeams[teamName] = teamMembers
    for team in dictTeams:
        print(team)
        for person in dictTeams[team]:
            print("  " + person)

objFile.close()
