 #celsius = 5*(F-32)/9
f = int(input("enter the temperature in fahrenheit: "))
def ctf(f):
    c = 5*(f-32)/9
    return c
c = ctf(f)
print(f"{round(c, 2)}°C")