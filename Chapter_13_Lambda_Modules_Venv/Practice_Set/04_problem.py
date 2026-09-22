def divisible5(n):
    if(n%5 == 0):
        return True
    return False
    
a = [1,2,34,56,6765,676795,679,9890,678,67,345,347,76]

f = list(filter(divisible5,a))
print(f)