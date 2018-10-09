"""
Function

Name..: Hieu NGuyen, Student  
ID....: W0424530
"""
_AUTHOR_ = "Hieu Nguyen <W0424530@nscc.ca>"

def foo():
    print("hello from inside of foo")
    return __name__

if __name__== '__main__':
    print("going to call foo")
    x=foo()
    print("call foo")
    print("foo returned "+str(x))

