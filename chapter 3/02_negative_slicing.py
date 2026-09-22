name = "Cherry_Tree"


print(name[-6:-1])   # both are same as below [5:10]
print(name[5:10])

print(name[:-1])     # is same as print(name[0:-1])
print(name[:10])     # is same as print(name[0:10])

print(name[1:11])   # is same as print(name[1:11])
print(name[1:])     # [1:] is same as print(name[1:11]) but Note [1: ke baad (length - 1) hoga]

print(name[5])
print(len(name))

###########################################################################################
# Slicing with skip value

a = "amazingsarts"    # first solve [1:5] so get 'mazi' then solve [1:5:3] where 3 is slice(skip) or 3 places jump from 'm to a,a to z,z to i' 
                      # so we get 'mi' as output
print(a[1:5:3])


word = "amazing"
print(word[1:6:2])