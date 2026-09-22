s1 = { 2, 45, 56, 67, 78, 45, 67, 79}
s2 = { 48, 67, 79, 49, 89, 45, 1}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1.difference(s2))

print({48,67}.issubset(s2))
print(s1.issuperset({67,45}))