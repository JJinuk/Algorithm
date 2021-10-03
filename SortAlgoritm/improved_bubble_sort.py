arr = [3, 31, 48, 73, 8, 11, 20, 29, 65, 15]

def BubbleSort(array):
    n = len(array)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                if swapped == False:
                    break
        print(arr)

print("before:", arr)
BubbleSort(arr)
print("after:", arr)

