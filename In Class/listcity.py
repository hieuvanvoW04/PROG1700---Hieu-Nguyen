
def cityworld():
    cities_in_canada=["ottowa","montreal","vancouver"]
    cities_in_us=["detroil","nyc","la"]
    cities_in_skorea=["seoul","busan","ulsan","jeju"]

    list_of_cities=[cities_in_canada,cities_in_us,cities_in_skorea]

    for clist in list_of_cities:
        print(clist)
        for city in clist:
            print(city)








cityworld()