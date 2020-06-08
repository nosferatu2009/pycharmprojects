def find_max(num):
    maxx = num[0]
    for i in num :
        if maxx<i :
            maxx = i
    return maxx