def SumDigits(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum

num = int(input("Enter number: "))
print("Addition of digits =", SumDigits(num))