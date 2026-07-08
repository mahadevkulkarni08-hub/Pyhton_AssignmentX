def Pattern(no):
    for i in range(no):
        for j in range(no - i):
            print("*", end=" ")
        print()

num = int(input("Enter number: "))
Pattern(num)