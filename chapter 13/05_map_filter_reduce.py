from functools import reduce

# Map Example
l = [1,2,3,4,5] 

square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))

# Filter Example
def even(n):
    if(n%2 == 0):
       return True
       return False
    
onlyEven = filter(even,l)  
print(list(onlyEven))

# Reduce Example 
def sum(a,b):    # add numbers
    return a+b

addNum = reduce(sum,l)
print(addNum)

# Reduce Example
mul = lambda x,y: x*y   # multiple numbers

mulPle = reduce(mul,l)
print(mulPle)
