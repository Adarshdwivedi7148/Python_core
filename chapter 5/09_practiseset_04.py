s = set()

s.add(20)
s.add(20.0)       #  1 == 1.0 same as 
s.add("20")       # length of s after these operations ?

print(s,len(s))