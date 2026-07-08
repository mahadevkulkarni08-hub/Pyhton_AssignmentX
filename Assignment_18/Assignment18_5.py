import MarvellousNum

def ListPrime(arr):
    sum = 0

    for i in arr:
        if MarvellousNum.ChkPrime(i):
            sum = sum + i

    return sum

size = int(input("Enter number of elements: "))

data = []

for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

print("Addition of prime numbers =", ListPrime(data))