 #cm = inches × 2.54

def itc(i):
    if i==0:
        return 
    c = i *2.54
    return c
i = int(input("Enter the number: "))
c = itc(i)
print(f"{i} inches = {c} cm")