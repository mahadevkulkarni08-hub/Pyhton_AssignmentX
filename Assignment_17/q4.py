def SumFactors(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
    return sum

num = int(input("Enter number: "))
print("Addition of factors =", SumFactors(num))