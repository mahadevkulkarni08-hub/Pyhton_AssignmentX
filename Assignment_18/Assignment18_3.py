def Minimum(arr):
    min = arr[0]

    for i in arr:
        if i < min:
            min = i

    return min

size = int(input("Enter number of elements: "))

data = []

for i in range(size):
    value = int(input("Enter element: "))
    data.append(value)

print("Minimum number =", Minimum(data))