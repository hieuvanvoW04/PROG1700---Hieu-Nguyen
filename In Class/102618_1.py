def maybenumber():


    maybe_num= input ("Please enter a number ")
    if(maybe_num.isnumeric()):
        num=int(maybe_num)
    else:
        print("not a number")
    while(not maybe_num.isnumeric()):
        maybe_numn= input("Please enter a number")
    num=int(maybe_num)




maybenumber()