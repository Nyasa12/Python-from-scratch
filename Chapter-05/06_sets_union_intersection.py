s1 ={2,6,8,34,67,22,90}
s2 ={1,2,3,8,22,90,35,64}

print(s1.union(s2))

print(s1.intersection(s2))

a = {1, 2, 3, 4}
b = {3, 4}
print(a.difference(b))    # {1, 2}

a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))   # {1, 2, 4, 5}

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))   # True


a = {1, 2, 3}
b = {3, 4, 5}
print(a.symmetric_difference(b))   # {1, 2, 4, 5}

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))   # True

a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))   # True

