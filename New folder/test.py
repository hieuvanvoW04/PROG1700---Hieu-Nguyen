
def testFile():
    inp_obj=open("test.txt")
    out_obj=open("OutFile.txt","w")
    for line_str in inp_obj:
        line_str.write("\nContact\nLviza\nNascimento")
        result_str=line_str
        out_obj.write(result_str)
    print(out_obj.write())
    
    inp_obj.close()
    out_obj.close()

testFile()
