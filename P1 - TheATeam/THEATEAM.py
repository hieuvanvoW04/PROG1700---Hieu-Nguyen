def THEATEAM():
# 1. Read contents of ateam file and print it to the screen
    objFile=open("ateam_Original.txt")
    objOutFile=open("out.txt","w")

    strContents=objFile.read()
    print(strContents)
    line_number=1
    line_counter=1
# 2. Read each lie of atem.t ad print it along with its length
    for line in objFile:
        strMsg="length"
        strMsg+=str(len(line))
        strMsg+=")_:_"
        strMsg+=line
        print(len(line_number))
        print(line,end="")
        if(line_counter==1):
            objOutFile.write(line)
            line_counter+=1
        objOutFile.write(line)
    objFile.close()
    objOutFile.close()







THEATEAM()