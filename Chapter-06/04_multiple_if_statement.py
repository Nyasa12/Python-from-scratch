a = int(input("Enter your age:"))


#if statement no:1
if(a%2==0):
    print("a is even")


#if statement no:2
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