with open ("this.txt", "r")as f :
    data1 = f.read()

with open ("this_copy.txt", "r")as f:
    data2 = f.read()

if data1 == data2 :
    print("the content is identical and matches eachother")

else :
    print("the content does not identical and matches eachother")
