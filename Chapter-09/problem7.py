with open ("p.txt", "r")as f:
    lines = f.readlines()
lineno = 1
for line in lines:
    if ("python" in line ):
        print("python is present. line number : ", {lineno})
        break
else:
    print("python is not present")