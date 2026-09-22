class Number:
    def __init__(self,n):   # store the number inside the object
        self.n = n 
    
    def __add__(self,ries):
        return self.n + ries.n    # when + is used, and two numbers
    
noi = Number(2)     # create object with value 2
goi = Number(3)     # create object with value 3

print(noi + goi)    # add the two objects