class demo :
    a = 6

o = demo()
print(o.a)
# print class attribute becoz instance attribute is not present

o.a = 0
print(o.a)
# print the instance attriute
print(demo.a)