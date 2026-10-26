with open ("p.txt", "r") as f :
    if ("python" in f.read()):
        print("python is present")

    else:
        print("python is not present")