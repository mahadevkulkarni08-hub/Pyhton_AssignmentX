def ChkPrime(no):
    count = 0

    for i in range(1, no + 1):
        if no % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False

num = int(input("Enter number: "))

if ChkPrime(num):
    print("It is Prime Number")
else:
    print("It is Not Prime Number")