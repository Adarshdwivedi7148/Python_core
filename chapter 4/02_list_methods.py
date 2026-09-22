# list indexing

friends = ["Apple", "orange", 3 , 904.45, False, "Asshish", "Rohan"]
print(friends)

friends.append("Harry")         # append() means add strings something at the end of the list
print(friends)

#############################################################################################
# List Methods

l1 = [1, 33, 56,2, 6, 11]
l1.sort()                    #  increasing order
print(l1)

l1.reverse()                 # reverse order
print(l1)

l1.append(8)                # adds 8 at the end of the list
print(l1)

l1.insert(3,15)             # insert 15 at the place of third index(3)
print(l1)

value = l1.pop(2)
print(value)                # will delete element at index 2 and return its value
print(l1)

l1.remove(6)                # will remove 6 from the list
print(l1)