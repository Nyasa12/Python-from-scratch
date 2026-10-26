f = open("file.txt")

'''f.readlines()

print(f.readlines(), type(f.readlines()))

f.close()   '''

line = f.readline()

while line != "":

    print(line)

    line = f.readline()

    f.close()
