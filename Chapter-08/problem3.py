def fun():
    n = int(input("enter the number: "))
    for i in range(1, n+1):
        print(" "*(n-i), end=" ")
        print("*" * (2*i-1), end=" ")
        print(" "*(n-i), end=" ")
        print(" ")
print(fun())

#its about the "end" function in print statement. it is used to avoid the new line after the print statement. by default it is "\n" which means new line. but we can change it to anything we want. in this case we are using " " which means space. so after each print statement it will print a space instead of a new line.