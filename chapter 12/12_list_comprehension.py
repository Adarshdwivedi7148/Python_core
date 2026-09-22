myList = [1,2,3,4,5,6,7]

# method 1 (best)
squareList = [item * item for item in myList]
print(squareList)

# method 2
squareList = []
for item in myList:
    squareList.append(item * item)

print(squareList)