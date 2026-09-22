from functools import reduce

l = [111, 4,456, 565,456,85 ,567,342 , 98]

def greater(a,b):
    if(a>b):
        return a
    return b

goi = reduce(greater,l)
print(goi)
