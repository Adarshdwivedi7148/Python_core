####################### Note - 'Tuples are immutable'  ####################################
# They can change in the exitings elements


di = (1,45,3345,5677,False,"Messi","Ronaldo")
print(di)

no = di.count(3345)     # Return the number of times a specified value appears in the tuple
print(no)

val = di.index("Messi")  # To check the index where "Messi" is in 5th index
print(val)

fig = len(di)           # To check the length what we write
print(fig)

print(45 in di)           # check if an item exists in a tuple using the "in" keyword
print(4535 in di)         # true or false mey check kartaa hai

repeated = di * 3         # Tuples can be repeated using the '*' operator
print(repeated)