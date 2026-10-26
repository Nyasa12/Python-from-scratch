friends = ["apple" , "Grapes", 7 , 34.58 , "pappaya"]
print(friends)


#1
friends.append("banana") #adds element at the end
print(friends)

#2
l1 = [5,6,8,32,7,0,65,85,24,52]
l1.sort() #sorts the list permanently
print(l1)

#3
l1.reverse() #reverses the list permanently
print(l1)

#4
l1.insert(2,55) #inserts 55 at index 2
print(l1)

#5
print(l1.pop(3)) #removes element at index 2 and will return the value
l1.pop(3) #removes element at index 2
print(l1)

#6
l1.remove(85) #removes first occurence of 85
print(l1)

#7
print(l1.index(65)) #returns index of first occurence of 65