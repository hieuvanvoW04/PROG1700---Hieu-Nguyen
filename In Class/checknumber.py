
def isnumber():

    may_num=input("enter 4 number ")
    if(may_num.isnumeric()):
        num=int(may_num)
    else:
        print("no good: Not a number")


isnumber()

