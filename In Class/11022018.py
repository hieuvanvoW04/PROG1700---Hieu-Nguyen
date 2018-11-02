

# code snippet to ask user if they
# want to continue doing something and 
# either continue or quit
#            keepFoing="y"
#            while(  keepFoing="y"      ) condition: is keep going set to "y"
#               do a bunch of stuff
#               insert anything here
#           keepGoing=input("Do you want to keep going(y/n)")


# Part1: turn a snippet of code into a function
# Part2: change a function that prints "something" to a function that returns "something"
n=48
for i in range(1,n+1):
    if(n%i==0):
        print(i)
# n=48
def printFactors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)

# storing result in a list

def getFactorList(n):
    FL=[]

    for i in range (1,n+1):
        if(n%i==0):
            FL.append(i)
    return(FL)

FL1=getFactorList(12)
FL2=getFactorList(9)
print(FL1)
print(FL2)


list1=[1,3,9]
list2=[1,2,3,4,6,12]
def commonInLists(list1,list2):
    commonList=[]
    for l in list1:
        if l in list2:
            commonList.append(l)
    return(commonList)


def max(L):
    max=L[0]
    for i in L:
        if(i>max):
            max=i
    return(max)  


def gcd(n1,n2):
    nModularFL=getFactorList(n1)
    nGreaterthanLL=getFactorList(n1)
    CL=commonInLists(nModularFL,nGreaterthanLL)
    # print(max(CL))
    return(max(CL))
