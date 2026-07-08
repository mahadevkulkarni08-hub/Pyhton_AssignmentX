def ListSum(arr):
    sum = 0

    for i in arr:
        sum = sum + i

    return sum

size = int(input("Enter number of elements: "))

data = []

for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

print("Addition =", ListSum(data))