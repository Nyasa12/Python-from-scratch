s = {5,5,5,5,6,7,3,8.9, 'nyasa'}
print(s,type(s))

s.add(354)
print(s,type(s))

s = {1, 2}
s.update([3, 4, 5])
print(s)    # {1, 2, 3, 4, 5}

s = {1, 2}
s.update([3, 4, 5])
print(s)    # {1, 2, 3, 4, 5}

s = {1, 2, 3}
s.remove(2)
print(s)    # {1, 3}

s = {1, 2, 3}
s.discard(5)
print(s)    # {1, 2, 3}

s = {10, 20, 30}
x = s.pop()
print(x)    # koi bhi random element
print(s)

s = {1, 2, 3}
s.clear()
print(s)   # set()

s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)   # {1, 2, 3}

