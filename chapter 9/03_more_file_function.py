f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines))

lines = f.readline()
while(lines != ""):
    print(lines)
    lines = f.readline()
f.close()



