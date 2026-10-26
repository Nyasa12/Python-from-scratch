a = int(input("Enter your age:"))

if(a>=18):
    print("you are above the age of consent")
    print("you can vote")

elif(a<0):
    print("Age cannot be negative")

elif(a==0):
    print("You are a newborn")

else:
    print("you are below the age of consent")
    print("you cannot vote")
    

print("Keep growing")