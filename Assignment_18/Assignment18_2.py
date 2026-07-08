def Maximum(arr):
    max = arr[0]

    for i in arr:
        if i > max:
            max = i

    return max

size = int(input("Enter number of elements: "))

data = []

for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

print("Maximum number =", Maximum(data))