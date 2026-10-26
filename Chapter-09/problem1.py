

f = open("peoms.txt")

c = f.read()
if ("twinkle" in c):
    print("twinkle is present")
else:
    f.close()

print(f)