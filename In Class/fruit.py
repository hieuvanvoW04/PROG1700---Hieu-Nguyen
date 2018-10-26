

def fruit():

    L=['apples','peaches','grapes','oranges','bananas']
    def replace():
        K=L.replace('e','E')
        return K
    res=map(replace,L)

    print(list(res))


fruit()