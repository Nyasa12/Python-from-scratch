b = ("shivam", "roham ",45, 23 , 4567 , 2)

print(type(b))

a= (1,) #tuple with single element
print(type(a))


#1 
no = b.count(45) #counts occurence of 45 in tuple b
print(no)

#2
c = b.index(23) #returns index of first occurence of 23
print(c)

#3
t = (10, 20, 30, 40)
print(len(t))   #returns length of tuple t

#4
t = (5, 10, 15, 20, 25)
print(t[1:4])  #slicing of tuple from index 1 to 3

#5
t1 = (1, 2, 3)
t2 = (4, 5)
print(t1 + t2)   #concatenation of tuples t1 and t2

#6
t = ("A", "B")
print(t * 3)    #repeats the tuple t three times

#7
t = (1, 2, 3)
print(2 in t)      #checks if 2 is present in tuple t
print(10 in t)      #checks if 10 is present in tuple t
