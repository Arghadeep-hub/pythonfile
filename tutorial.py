def moveToEnd(arr, n):
    count = 0
    for i in range(0, n):
        if (arr[i] != 0):
            arr[count], arr[i] = arr[i], arr[count]
            count += 1


def printArray(arr, n):
    for i in range(0, n):
        print(arr[i], end=" ")


arr = [0, 5, 9, 0, 4, 1]
n = len(arr)

print("original Array:", end=" ")
printArray(arr, n)

moveToEnd(arr, n)

print("\nModified Array:", end=" ")
printArray(arr, n) # 5 9 4 1 0 0
