with open("practice.txt","r") as f:
    for line in f:
        print(line)

        lines=f.readlines()
        print(lines)

        with open("love.txt","w") as f:
            f.write("I Love Python")