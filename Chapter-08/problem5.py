#using for loop
n = int(input("enter the number: "))

for  i in range(n, 0, -1):
    print("*"*(i), end="" )
    print("")

#using function
def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n - 1)

pattern(3)